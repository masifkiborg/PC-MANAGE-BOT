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
                    'available':f"{memory.available/(1024**3):.2f} GB",
                    'usage': f"{memory.percent}%"

                },
                'swap': {
                    'total':f"{swap.total/(1024**3):.2f} GB",
                    'used': f"{swap.used/(1024**3):.2f} GB",
                    'usage': f"{swap.percent}%"
                },
                'disk':{
                    'total':f"{disk.total/(1024**3):.2f} GB",
                    'used': f"{disk.used/(1024**3):.2f} GB",
                    'free': f"{disk.free/(1024//3):.2f} GB",
                    'usage': f"{disk.percent}%"
                }
                
            }

            return info
        except Exception as e:
            return {'error': f"error get system info: {str(e)}"}
    @staticmethod
    def get_run_processess(limit=10):
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            
            processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
            return processes[:limit]
        except Exception as e:
            return f"Erorr get process {str(e)}"
