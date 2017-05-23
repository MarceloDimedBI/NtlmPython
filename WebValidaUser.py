#!/usr/bin/python
# -*- coding: utf-8 -*-
############################################################################################################
# Nome: webValidaUser.py
# Descricao: Procedimento para criar um servico que valida os users.
# Autor: Douglas Piero Sironi
# Data: 23/05/2017
# Versao: 2.0
############################################################################################################

from bottle import route, run, template, response,static_file, post, request
import json
import requests
from requests_ntlm import HttpNtlmAuth
import logging
import logging.handlers
from daemon import runner

path="/tmp/"
logDir=path+"/WebValidaUsers.log"


@post('/valida')
def valida():

	logger.info(request.json['username']+' ********** ')
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type,application/json, X-Requested-With, X-CSRF-Token'

	session = requests.Session()
	# result = session.get('http://<server>/QvAJAXZfc//Authenticate.aspx',auth=HttpNtlmAuth('<domain>\\'+username,password))
	result = session.get('http://<server>/QvAJAXZfc//Authenticate.aspx',auth=HttpNtlmAuth('<domain>\\'+request.json['username'],request.json['password']))
	logger.info(result)
	return json.dumps({'retorno':result.status_code})
############################################################################################################
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(
              logDir, maxBytes=2097152, backupCount=5)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Iniciando o servico de autenticacao via https.")
############################################################################################################
app = Bottle()
############################################################################################################
