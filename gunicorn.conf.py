max_requests = 1000
max_requests_jitter = 50
bind = '127.0.0.1:8000'
log_file = "gunicorn-access.log"
workers = 3
threads = 3
worker_class = 'uvicorn.workers.UvicornWorker'

# gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log main:app --bind 0.0.0.0:8000 --workers 3