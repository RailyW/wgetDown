import os
import tarfile
from flask import Flask, send_file, after_this_request

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
