# import celery and use a rabbitmq backend
from celery import Celery
app = Celery('tasks', backend='amqp', broker='amqp://')

# set up our fib worker function definition
@app.task
def fib(n):
    if n < 0 :
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        result = [0, 1, 1]
	rapp = result.append
        for i in xrange(n-2):
            rapp(result[-1]+result[-2])
        return result
