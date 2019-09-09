#!/usr/bin/env sh

# echo ""
# curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' ''

echo "current"

echo "readmorejoy.com reward.css "
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://www.readmorejoy.com/static/reward.css'

echo "readmorejoy.com  skeleton.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://www.readmorejoy.com/static/skeleton.css'

echo "bootstrapcdn bootstrap.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'


echo "cloudflare jquery.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'

echo "bootstrapcdn bootstrap.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'

echo "cloudflare bootbox.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdnjs.cloudflare.com/ajax/libs/bootbox.js/5.3.2/bootbox.min.js'

echo "smtp.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://www.readmorejoy.com/static/smtp.js'

echo ""
echo "old"

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


echo "bootcss web skeleton.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/skeleton/2.0.4/skeleton.min.css'
echo "bootcss web bootstrap.min.css"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/twitter-bootstrap/4.1.2/css/bootstrap.min.css'
echo "bootcss web jquery.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js'
echo "bootcss web bootstrap.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/twitter-bootstrap/4.1.2/js/bootstrap.min.js'
echo "bootcss web bootbox.min.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://cdn.bootcss.com/bootbox.js/4.4.0/bootbox.min.js'

echo "web self smtp.js"
curl -o /dev/null -s -w '%{time_connect}:%{time_starttransfer}:%{time_total}\n' 'https://smtpjs.com/v3/smtp.js'
