import os 
import platform
import subprocess
import time

class PowerManager:
    @staticmethod
    def shutdown(delay = 30):
        try:
            system = platform.system().lower()
            if system == "windows":
                result = subprocess.run(f"shutdown /s /t {delay}",shell=True,capture_output=True,text=True)
                if result.returncode == 0:
                    return {
                        'succes':True,
                        'message': f"PC shutdown as {delay} seconds",
                        'delay': delay,
                        'cancel_command': "shutdown /a"
                    }
                else:
                    return {
                        'succes':False,
                        'message': f"Shutdown error {result.stderr}"
                    }
                
            elif system == "linux":
                cmd = f"shutdown -h +{delay // 60}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': f'✅ Компьютер выключится через {delay} секунд',
                        'delay': delay,
                        'cancel_command': 'shutdown -c'
                    }
                else:
                    return {
                        'success': False,
                        'error': f'Ошибка выключения: {result.stderr}'
                    }
            
            elif system == "darwin":  # macOS
                cmd = f"sudo shutdown -h +{delay// 60}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': f'✅ Компьютер выключится через {delay} секунд',
                        'delay': delay,
                        'cancel_command': 'sudo killall shutdown'
                    }
                else:
                    return {
                        'success': False,
                        'error': f'Ошибка выключения: {result.stderr}'
                    }
            else:
                return {
                    'success': False,
                    'error': f'Неподдерживаемая система: {system}'
                }
        except Exception as e:
             return {
                'success': False,
                'error': f'Исключение при выключении: {str(e)}'
            }
        

    @staticmethod
    def cancel_shutdown():

        try:
            system = platform.system().lower()
            
            if system == "windows":
                cmd = "shutdown /a"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': '⏹️ Запланированное выключение отменено'
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Не удалось отменить выключение (возможно, не было запланировано)'
                    }
                    
            elif system in ["linux", "darwin"]:
                cmd = "shutdown -c"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': '⏹️ Запланированное выключение отменено'
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Не удалось отменить выключение (возможно, не было запланировано)'
                    }
            else:
                return {
                    'success': False,
                    'error': f'Неподдерживаемая система: {system}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Исключение при отмене выключения: {str(e)}'
            }

    @staticmethod
    def hibernate():
        try:
            system = platform.system().lower()
            
            if system == "windows":
                cmd = "shutdown /h"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': '💤 Компьютер переходит в режим гибернации'
                    }
                else:
                    return {
                        'success': False,
                        'error': f'Ошибка гибернации: {result.stderr}'
                    }
                    
            elif system == "linux":
                cmd = "systemctl hibernate"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {
                        'success': True,
                        'message': '💤 Компьютер переходит в режим гибернации'
                    }
                else:
                    return {
                        'success': False,
                        'error': f'Ошибка гибернации: {result.stderr}'
                    }
            else:
                return {
                    'success': False,
                    'error': f'Гибернация не поддерживается в системе: {system}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Исключение при гибернации: {str(e)}'
            }