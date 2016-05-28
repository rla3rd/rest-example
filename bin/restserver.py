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
    	    fibArr = mcd.get('fibonacci_%s' % n)
    	    if fibArr == None:
	        fibArr = fib(n)
	        mcd.set('fibonacci_%s' % n, fibArr)
	    # return our response
	    resp.status = falcon.HTTP_200
            resp.body = json.dumps(fibArr)
        else:
            # client submitted an invalid arg, return a 400
	    resp.status = falcon.HTTP_400
	    resp.body = json.dumps({'Bad Request': {'fibonacci': '%s' % num}})

# gunicorn requires 'application' defined
api = application = falcon.API()
api.add_route('/fibonacci/{num}', Fibonacci())
