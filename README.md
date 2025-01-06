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
wget -O file.tar http://192.168.10.10:9000/download
```
Run the following command to decompress the tar file.

```cmd
tar -xvf file.tar
```

## /download/\<filename\>

Download target file.

```cmd
wget http://192.168.10.10:9000/download/<filename>
```

## /md5/\<filename\>

Get md5 value of target file. Same as `md5sum <filename>`.

```cmd
wget -O <filename>.md5 http://192.168.10.10:9000/md5/<filename>
```

Run the following command to view md5 value.
```cmd
cat <filename>.md5
```
