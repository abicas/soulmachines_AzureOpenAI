# Gunicorn configuration file
import multiprocessing

max_requests = 100
max_requests_jitter = 50

log_file = "-"

host = "0.0.0.0"
port = "8000"
bind = f"{host}:{port}"

worker_class = "uvicorn.workers.UvicornWorker"
workers = (multiprocessing.cpu_count()) + 1