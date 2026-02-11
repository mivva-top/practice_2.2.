import psutil
import time

print("Системный монитор")
print("Нажмите Stop для остановки")

try:
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()

        print(f"CPU: {cpu_percent}% (ядер: {cpu_count})")

        memory = psutil.virtual_memory()
        memory_total_gb = memory.total / (1024 ** 3)
        memory_used_gb = memory.used / (1024 ** 3)
        memory_percent = memory.percent

        print(f"RAM: {memory_percent}% ({memory_used_gb:.1f} GB из {memory_total_gb:.1f} GB)")

        disk = psutil.disk_usage('/')
        disk_total_gb = disk.total / (1024 ** 3)
        disk_used_gb = disk.used / (1024 ** 3)
        disk_percent = disk.percent

        print(f"DISK: {disk_percent}% ({disk_used_gb:.1f} GB из {disk_total_gb:.1f} GB)")

        print()
        time.sleep(2)

except KeyboardInterrupt:
    print("Мониторинг остановлен")
except ImportError:
    print("Установите psutil: pip install psutil")