import os
import tempfile
from PIL import ImageGrab
import io

class Screenshot:
    @staticmethod
    def take_screenshot():
        try:
            screenshot = ImageGrab.grab()
            buffer = io.BytesIO()
            screenshot.save(buffer,format='PNG')
            buffer.seek(0)
            return buffer.getvalue()
        
        except Exception as e:
            print(f"Take screenshot error{e}")
            return None