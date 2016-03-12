sudo service mysql start

if [ $? -ne 0 ]; then
  echo "mysql start failed"
  exit 1
fi

sleep 3

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

sudo mysql -uroot -e "create database ask"

sleep 3

chmod u+x /home/box/web/ask/manage.py
ask/manage.py syncdb --noinput
