workers = 1
worker_class = 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker'
pidfile= '{{ pid }}'
debug = True
loglevel = 'debug'
errorlog = '{{ log }}/gunicorn.log'
