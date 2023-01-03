max_requests = 30
max_requests_jitter = 30
bind = '127.0.0.1:8000'
deamon = True
worker_connections = 5
workers = 3
threads = 3
worker_class = 'uvicorn.workers.UvicornWorker'

# gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log main:app --bind 0.0.0.0:8000 --workers 3