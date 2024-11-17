import psutil
import time


def log_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    with open("results/performance_logs/system_usage.txt", "a") as f:
        f.write(f"Time: {time.ctime()}, CPU: {cpu}%, Memory: {memory}%\n")
    print(f"CPU Usage: {cpu}%, Memory Usage: {memory}%")
