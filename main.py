import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import mobSFrequest

ALLOWED_EXTENSIONS = set(['apk', 'zip', 'ipa', 'appx'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#resp = jsonify({'message' : 'File successfully uploaded'})
		#resp.status_code = 201
		filefullpath = app.config['UPLOAD_FOLDER']+filename
		print('filefullpath', filefullpath)
		mobSFrequest.malware_path=filefullpath
		mobSFresp_val=mobSFrequest.upload_file()
		mobSFrequest.scan_file(mobSFresp_val)
		resp=mobSFrequest.json_response(mobSFresp_val)
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are apk, zip, ipa, appx'})
		resp.status_code = 400
		return resp


if __name__ == "__main__":
    app.run()
