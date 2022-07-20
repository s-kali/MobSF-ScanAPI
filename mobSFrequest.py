import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

api_url = 'http://localhost:8000'
api_key = '7dcd5dcc80ae5eab5a85b79bff81e775c9cb483c426da44d0476ef113c3bfb58'

malware_name = 'example.apk'
malware_path = ''

def upload_file():
	multipart_data = MultipartEncoder(fields={'file': (
							malware_name,
							open(malware_path,'rb'),
							'application/octet-stream')})

	header = {
		'Content-Type': multipart_data.content_type,
		'Authorization': api_key
		}

	response = requests.post(api_url+'/api/v1/upload',
			  headers=header,
			  data=multipart_data
			)
	print(response.text)
	return(response.text)

def scan_file(upload_response):
	rtext = json.loads(upload_response)

	header = {
		'Authorization': api_key
		}

	response = requests.post(api_url+'/api/v1/scan', data=rtext, headers=header)
	print(response.text)

def json_response(upload_response):
	header = {'Authorization':api_key}
	hash_val = {"hash": json.loads(upload_response)["hash"]}
	response = requests.post(api_url+'/api/v1/report_json', data=hash_val, headers=header)
	print(response.text)
	return(response.text)

#resp_val = upload_file()
#scan_file(resp_val)
#json_response(resp_val)
