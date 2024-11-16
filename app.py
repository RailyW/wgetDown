import os
import tarfile
import hashlib
from flask import Flask, send_file, after_this_request, abort, Response

app = Flask(__name__)

TAR_FILE_PATH = os.path.join(os.getcwd(), 'wgetFiles.tar')


@app.route('/')
def welcome():
    return 'Welcome to wgetDown page. Access "/download" to download all files.'


@app.route('/download')
def download_all_files():
    if os.path.exists(TAR_FILE_PATH):
        os.remove(TAR_FILE_PATH)

    public_folder = os.path.join(os.getcwd(), 'public')

    with tarfile.open(TAR_FILE_PATH, 'w') as tar:
        for root, dirs, files in os.walk(public_folder):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, public_folder))

    @after_this_request
    def remove_tar_file(response):
        try:
            os.remove(TAR_FILE_PATH)
        except Exception as e:
            app.logger.error("Error removing or closing tar file", e)
        return response

    return send_file(TAR_FILE_PATH, as_attachment=True, download_name='wgetFiles.tar')

@app.route('/download/<filename>')
def download_single_file(filename):
    public_folder = os.path.join(os.getcwd(), 'public')
    file_path = os.path.join(public_folder, filename)

    if not os.path.exists(file_path):
        abort(404, description=f"File '{filename}' not found.")

    return send_file(file_path, as_attachment=True)

@app.route('/md5/<filename>')
def get_file_md5(filename):
    public_folder = os.path.join(os.getcwd(), 'public')
    file_path = os.path.join(public_folder, filename)

    if not os.path.exists(file_path):
        abort(404, description=f"File '{filename}' not found.")

    # 计算文件的 MD5
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)

    md5_result = md5_hash.hexdigest()

    return Response(md5_result + '\n', mimetype='text/plain')

@app.errorhandler(404)
def not_found_error(error):
    return Response(str(error.description) + '\n', status=404, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
