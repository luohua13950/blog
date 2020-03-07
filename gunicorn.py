#!/usr/bin/env python
import multiprocessing
cpu_count = multiprocessing.cpu_count()
bind="127.0.0.1:8080"

backlog=64

worker=cpu_count*2+1

worker_class="gevent"

threads=3

worker_connections=500

timeout=60

keepalive=2

chdir="/root/www/blog"

daemon=False

accesslog="/var/log/gunicorn/access.log"

access_log_format = '%(h)s %(l)s %(m)s %(u)s %(t)s %(l)s %(s)s %(a)s'

errorlog="/var/log/gunicorn/error.log"

loglevel="info"