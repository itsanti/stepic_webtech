sudo /etc/init.d/mysql start

if [ $? -ne 0 ]; then
  echo "mysql start failed"
  exit 1
fi

sleep 5

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

sleep 5

sudo mysql -uroot -h"127.0.0.1" -P3306 -e "create database ask"
echo "ask database created"

chmod u+x /home/box/web/ask/manage.py
echo -e
echo "run ask/manage.py syncdb --noinput"
