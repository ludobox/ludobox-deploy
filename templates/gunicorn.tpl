bind = 'unix:{{ socket }}'
workers = 2
pidfile= '{{ pid }}'
debug = True
loglevel = 'info'
errorlog = '{{ log }}/gunicorn.log'
