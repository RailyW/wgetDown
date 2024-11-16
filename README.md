# How to run

```
pip install -r requirements.txt
python app.py
```

# File Management

All the files are in `/public`.

# API Document

> backend as: 192.168.10.10:9000

## /download

Download all the files in a `.tar`.

```cmd
curl -o file.tar http://192.168.10.10:9000/download
```

## /download/<filename>

Download target file.

```cmd
curl http://192.168.10.10:9000/download/<filename>
```

## /md5/<filename>

Get md5 value of target file. Same as `md5sum <filename>`.

```cmd
curl http://192.168.10.10:9000/md5/<filename>
```
