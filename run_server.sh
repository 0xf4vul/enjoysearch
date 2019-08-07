#gunicorn -w 4 -b 0.0.0.0:4000 service:app
gunicorn -w 4 -b 0.0.0.0:4000 service:app --reload -t 500 -D --access-logfile /var/log/gunicorn.log
