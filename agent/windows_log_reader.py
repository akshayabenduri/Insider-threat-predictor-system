import win32evtlog
import os

def read_security_logs():
    server = 'localhost'
    log_type = 'Security'
    handle = win32evtlog.OpenEventLog(server, log_type)
    
    # Logic to filter for Event IDs like 4624 (Login) or 4625 (Failure)
    # as described in your "Algorithm Implementation" [cite: 471]
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    for event in events:
        if event.EventID in [4624, 4625]:
            print(f"Detected Auth Event ID: {event.EventID}")

if __name__ == "__main__":
    read_security_logs()