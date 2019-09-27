#gunicorn -w 8 -b 0.0.0.0:4000 service:app
gunicorn -w 12 -b 0.0.0.0:4000 service:app --reload -t 500 -D --access-logfile /var/log/gunicorn.log
