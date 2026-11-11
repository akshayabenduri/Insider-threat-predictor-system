import os
import time
import requests
import psutil 

API_URL = "http://127.0.0.1:8000/event"

def monitor_usb():
    print("USB Monitoring Agent Active...")
    recorded_drives = set([d.device for d in psutil.disk_partitions()])
    
    while True:
        current_drives = set([d.device for d in psutil.disk_partitions()])
        new_drives = current_drives - recorded_drives
        
        if new_drives:
            for drive in new_drives:
                payload = {
                    "user": os.getlogin(),
                    "event": "usb_insert",
                    "details": f"Drive {drive} detected"
                }
                try:
                    requests.post(API_URL, json=payload, timeout=2)
                    print(f"[!] Alert: USB Inserted - {drive}")
                except Exception as e:
                    print(f"Failed to alert backend: {e}")
        
        recorded_drives = current_drives
        time.sleep(2)

if __name__ == "__main__":
    monitor_usb()