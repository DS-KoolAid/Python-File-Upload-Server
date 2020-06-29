import os
import logging
from flask import Flask, flash, request
import argparse

PORT=8080

HOST='0.0.0.0'

UPLOAD_FOLDER = '.'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def landing_page():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post action='/upload' enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    logger.debug("triggered")
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'you need to pass me a file in the file variable'
        file = request.files['file']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded'
    return 'You need to pass me a file with a post request (data variable "file")'


def main():
    global PORT,HOST
    parser=argparse.ArgumentParser()
    parser.add_argument('-ip',action="store",help="IP you want server to run on. Default is 0.0.0.0",metavar=('IP Adddress'))
    parser.add_argument('-p',action="store",help="Port you want server to run on. Default is 8080",metavar=('PORT'))
    parser.add_argument('-d',action="store",help="Directory to store uploaded files Default is current location",metavar=('Directory'))
    parser.add_argument('-s','--ssl',action="store_true",help="Run with ssl")
    args=parser.parse_args()
    if args.p:
        PORT = args.p
    if args.ip:
        HOST=args.ip
    ssl_run=args.ssl
    if ssl_run==True:
        app.run(host=HOST,port=PORT,ssl_context='adhoc')
    else:
        app.run(host=HOST,port=PORT)

if __name__=="__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    main()


