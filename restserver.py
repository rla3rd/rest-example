import memcache
import json

#falcon rest framework
import falcon

# this is our celery worker
from task import fib

# set up our memcache client
mcd = memcache.Client(['127.0.0.1:11211'])

# set up our rest object
class Fibonacci(object):
    def on_get(self, req, resp, num):
	"""Handles GET requests"""
	# isdigit is only true for positive integers
	if num.isdigit():
	    n = int(num)
	    # check memcache 1st - if it doesnt exist process
    	    jsonFibArr = mcd.get('fibonacci_%s' % n)
    	    if jsonFibArr == None:
		# use delay  to use asynchronous callback over celery
	        async = fib.delay(n)
		fibArr = async.get()
		# jsonify the list returned and stuff back into memcache
		jsonFibArr = json.dumps(fibArr)
	        mcd.set('fibonacci_%s' % n, jsonFibArr)
	    # return our response
	    resp.status = falcon.HTTP_200
            resp.body = jsonFibArr
        else:
            # client submitted an invalid arg, return a 400
	    resp.status = falcon.HTTP_400
	    resp.body = json.dumps({'Bad Request': {'fibonacci': '%s' % num}})

# gunicorn requires 'application' defined
api = application = falcon.API()
api.add_route('/fibonacci/{num}', Fibonacci())
