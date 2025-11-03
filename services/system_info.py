import psutil
import platform
import socket
from datetime import datetime

class SystemInfoServices:
    @staticmethod
    def get_system_info():
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            cpu_freq = psutil.cpu_freq()


            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()

            disk = psutil.disk_usage('/')

            disk_io = psutil.disk_io_counters()


            boot_time = datetime.fromtimestamp(psutil.boot_time())
            uptime = datetime.now() = boot_time

            info = {
                'system':{
                    'os': f"{platform.system()} {platform.release()}",
                    'version': platform.version(),
                    'architecture': platform.architecture()[0],
                    'hostname': socket.gethostname(),
                    'boot_time': boot_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'uptime': str(uptime).split('.')[0]
                },
                'cpu':{
                    'usage': f"{cpu_percent}%",
                    'cores': cpu_count,
                    'frequency': f"{cpu_freq.current:.2f} Mhz" if cpu_freq else "N/A"
                },
                'memory':{
                    'total': f"{memory.total/(1024**3):.2f} GB",
                    'used': f"{memory.used/(1024**3):.2f} GB",

                }



            }