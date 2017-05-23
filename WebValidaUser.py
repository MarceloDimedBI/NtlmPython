from bottle import route, run, template, response,static_file
import json
import requests
from requests_ntlm import HttpNtlmAuth
	
	

@route('/valida/<username>/<password>')
def valida(username,password):
	print username+' '+password
	
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

	session = requests.Session()
	result = session.get('http://<server>/QvAJAXZfc//Authenticate.aspx',auth=HttpNtlmAuth('<domain>\\'+username,password))
	
	return json.dumps({'retorno':result.status_code})	
	
run(host='0.0.0.0', port=8000)
