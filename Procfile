#web: python gunicorn_django -b 0.0.0.0:$PORT --preload djpclient_example/settings.py
#web: gunicorn_django -b 0.0.0.0:$PORT -w 9 -k gevent --max-requests 250 --preload djpclient_example/settings.py
web: gunicorn djpclient_example.wsgi -b 0.0.0.0:$PORT