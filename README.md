# Python File Upload Server

This python script allows for files to be uploaded to a system via a Flask python server. 

This server accepts `POST` requests to the uri `/upload`. 

The file being uploaded to the server should be passed via a variable named `file` in the POST request. 

### Example of upload:

Without SSL

`curl -F 'file=@<file_to_upload>' http://<server>:<port>/upload`

With SSL

`curl -F 'file=@<file_to_upload>' http://<server>:<port>/upload -k`

## Setup:

`./setup.sh`

This will install the required python packages.

## Commands: 

- `-ip [IP Address]` The ip address of the machine hosting the server. (Default is 0.0.0.0)

- `-p [PORT]` The port you wan your server to run on. (Default is 8080)

- `-d [Directory]` The directory where you want to files to be stored.

- `-s` or `--ssl` Run the server with SSL enabled (server will use self-signed certs)

```
usage: python_file_upload.py [-h] [-ip IP Adddress] [-p PORT] [-d Directory]
                             [-s]

optional arguments:
  -h, --help       show this help message and exit
  -ip IP Adddress  IP you want server to run on. Default is 0.0.0.0
  -p PORT          Port you want server to run on. Default is 8080
  -d Directory     Directory to store uploaded files Default is current
                   location
  -s, --ssl        Run with ssl

  ```

  