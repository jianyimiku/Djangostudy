>在Djanggo中创建一个同级问价夹uwsgi
>
>```python
>[uwsgi]
>socket= 127.0.0.1:8001
>chdir = /root/nsb
>wsgi-file = /root/nsb/nsb/wsgi.py
>master = true
>processes = 10
>threads = 2
>```
>
>nginx
>
>```python
>upstream django {
>server 127.0.0.1:443;
>}
>
>server {
>listen  443 ssl;
>server_name www.hoboj.cn;
>ssl on;
>ssl_certificate /etc/nginx/1933939_www.hoboj.cn.pem;
>ssl_certificate_key /etc/nginx/1933939_www.hoboj.cn.key;
>client_max_body_size 50M;
>#charset utf-8;
>access_log  /root/https.access.log;
>error_log /root/https.error.log;
>location / {
>uwsgi_pass     127.0.0.1:8001;
>include       /etc/nginx/uwsgi_params;
>}
>location /media/ {
> alias /root/nsb/upload/;
>}
>location /static/ {
> alias /root/nsb/static/;
>}   
>}
>
>
>```
>
>nginx启动：
>
>sudo systemctl start nginx.service
>
>sudo systemctl stop nginx.service
>
>数据库需要django-envrion包

