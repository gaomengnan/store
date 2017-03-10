import sys
import os
import multiprocessing


workers = multiprocessing.cpu_count()*2+1
timeout = 30
graceful_timeout = 30
worker_class='gevent'
loglevel = 'info'
debug = True
bind = "127.0.0.1:8080" 
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
