#!/usr/bin/python
# -*- coding: utf-8 -*-
############################################################################################################
# Nome: webValidaUser.py
# Descricao: Procedimento para criar um servico que valida os users.
# Autor: Douglas Piero Sironi
# Data: 23/05/2017
# Versao: 2.0
############################################################################################################

import bottle
import json
import requests
from requests_ntlm import HttpNtlmAuth
from bottle import Bottle, request, response, run
import logging
import logging.handlers



path="c:/tmp/"
logDir=path+"/WebValidaUsers.log"

logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(
              logDir, maxBytes=2097152, backupCount=5)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Iniciando o servico de autenticacao via https.")
def log(msg):
	logger.info(msg)
	

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors
	
	
##########################################################################################################
app = Bottle()
@app.route('/valida', method=['OPTIONS', 'POST'])
@enable_cors
def valida():
	try:
		session = requests.Session()
		log(request.json['username']+":"+"*************")
		# result = session.get('http://<server>/QvAJAXZfc//Authenticate.aspx',auth=HttpNtlmAuth('<domain>\\'+username,password))
		result = session.get('http://<server>/QvAJAXZfc//Authenticate.aspx',auth=HttpNtlmAuth('<domain>\\'+request.json['username'],request.json['password']))
		log(result)
	except:
		print "Unexpected error:"
		raise	
	return json.dumps({'retorno':result.status_code})
############################################################################################################
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8000,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))
############################################################################################################
