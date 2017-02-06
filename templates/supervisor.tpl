[program:{{ domain }}]

directory={{ app_dir }}
environment=PYTHONPATH={{ venv_path}}/bin

command={{venv_path}}/bin/gunicorn 'ludobox.webserver:app' -c {{gunicorn_conf}}
;command=ludobox start

;user=www-data
autostart=true
autorestart=true

redirect_stderr=true
stopsignal=QUIT
exitcodes=0
