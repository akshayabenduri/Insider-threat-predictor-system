import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import requests
import threading
import time


API_URL = "http://127.0.0.1:8000/event"

class InsiderThreatDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("INSIDER THREAT DASHBOARD")
        self.root.geometry("1000x600")
        self.style = tb.Style(theme="darkly")
        
        # Header
        self.header = tb.Label(root, text="INSIDER THREAT DASHBOARD", font=("Helvetica", 20, "bold"), foreground="green")
        self.header.pack(pady=20)

        # Control Buttons (As seen in your PPT Slide 8)
        self.btn_frame = tb.Frame(root)
        self.btn_frame.pack(pady=10)
        
        self.start_btn = tb.Button(self.btn_frame, text="Start Monitoring", bootstyle="success", command=self.start_monitoring)
        self.start_btn.grid(row=0, column=0, padx=10)
        
        self.stop_btn = tb.Button(self.btn_frame, text="Stop Monitoring", bootstyle="danger")
        self.stop_btn.grid(row=0, column=1, padx=10)
        
        self.refresh_btn = tb.Button(self.btn_frame, text="Refresh", bootstyle="info")
        self.refresh_btn.grid(row=0, column=2, padx=10)

      
        columns = ("timestamp", "user", "event", "details", "risk")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center")
            
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

    def start_monitoring(self):
        # Logic to trigger your agents
        print("Monitoring Started...")

if __name__ == "__main__":
    root = tb.Window()
    app = InsiderThreatDashboard(root)
    root.mainloop()