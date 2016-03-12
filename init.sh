sudo service mysql start

if [ $? -ne 0 ]; then
  echo "mysql start failed"
  exit 1
fi

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

sudo mysql -uroot -e "create database ask"

chmod u+x /home/box/web/ask/manage.py
/home/box/web/ask/manage.py syncdb
