# Append current path to path.
import sys, os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/IOPi')

import bottle
from bottle import route, request, abort
import timeclock
import testtimeclock
import logging
import logging.config
import json


# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

@route('/time')
def timeclocktime():

	try:
		logging.info('timeclockpath() start')
		time = s.getJSONTime()
		logging.info('timeclockpath() end')
		return time
	except:
		logging.exception('Uncaught exception')
		raise

@route('/test/start', method='PUT')
def testtimeclockStart():

	ts.start()
	return "Started"

@route('/test/stop', method='PUT')
def testtimeclockStop():

	ts.stop()
	return "Stopped"

@route('/test/reset', method='PUT')
def testtimeclockReset():

	ts.reset()
	return "Stopped"

@route('/test/inError', method='PUT')
def testtimeclockinError():

	data = request.body.readline()
	if not data:
        	abort(400, 'No data received')
	entity = json.loads(data)
	if not entity.has_key('inError'):
		abort(400, 'No inError specified')
	error = entity['inError']
	ts.inError(error)

@route('/test/time')
def testtimeclocktime():

	return ts.getJSONTime()


s = timeclock.Timeclock()
ts = testtimeclock.Testtimeclock()

logging.config.fileConfig(os.path.dirname(__file__) + '/logger.cfg') #logfile config
logging.info('Started')
application = bottle.default_app()
