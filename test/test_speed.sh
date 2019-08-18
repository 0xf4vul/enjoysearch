#!/usr/bin/env sh

echo "search web skeleton.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://search.readmorejoy.com/static/skeleton.css'


echo "img bootbox.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'http://img.readmorejoy.com/static/bootbox.min.js'
echo "img smtp.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'http://img.readmorejoy.com/static/smtp.js'
echo "img skeleton.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'http://img.readmorejoy.com/static/skeleton.css'
echo "img skeleton.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'http://img.readmorejoy.com/static/skeleton.min.css'


echo "cdn"
echo "web skeleton.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/skeleton/2.0.4/skeleton.min.css'
echo "web bootstrap.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/twitter-bootstrap/4.1.2/css/bootstrap.min.css'
echo "web jquery.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js'
echo "web bootstrap.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/twitter-bootstrap/4.1.2/js/bootstrap.min.js'
echo "web bootbox.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/bootbox.js/4.4.0/bootbox.min.js'

echo "web self smtp.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://smtpjs.com/v3/smtp.js'
