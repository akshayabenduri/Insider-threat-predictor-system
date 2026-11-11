import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # From your report requirements

class HackingDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("INSIDER THREAT DASHBOARD")
        self.style = tb.Style(theme="darkly")
        
        # Title
        label = ttk.Label(root, text="INSIDER THREAT DASHBOARD", font=("Helvetica", 18), foreground="green")
        label.pack(pady=10)

        # Buttons
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Start Monitoring", bootstyle="success").grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Stop Monitoring", bootstyle="danger").grid(row=0, column=1, padx=5)

        # Table (Treeview)
        columns = ("timestamp", "user", "event", "details", "risk")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.upper())
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

if __name__ == "__main__":
    root = tb.Window()
    app = HackingDashboard(root)
    root.mainloop()