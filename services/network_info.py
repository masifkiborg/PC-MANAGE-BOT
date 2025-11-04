import psutil
import requests
import socket

class NetworkInfoService:
    @staticmethod
    def get_net_info():
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            try:
                external_ip = requests.get("https://api.ipify.org",timeout=5).text
            except Exception as e:
                return f"IP get error {str(e)}"
            
            net_io = psutil.net_io_counters()
            net_stats = {
                'bytes_sent': f"{net_io.bytes_sent / (1024**2):.2f} MB",
                'bytes_recv':f"{net_io.bytes_recv / (1024**2):.2f} MB",
                'packets_sent':net_io.packets_sent,
                'packets_recv':net_io.packets_recv
            }

            interfaces = {}
            for interface_name, interface_adressess in psutil.net_if_addrs().items():
                interfaces[interface_name] = []
                for address in interface_adressess:
                    if address.family == socket.AF_INET:
                        interfaces[interface_name].append({'address':address.address,'netmask':address.netmask})

            info = {
                'local_ip': local_ip,
                'external_ip': external_ip,
                'hostname': hostname,
                'network_stats': net_stats,
                'interfaces': interfaces
            }
            return info
        except Exception as e:
            return {'error': f"Get networtk info error {str(e)}"}
        