import ftplib
import ipaddress
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
import threading

def check_ftp_anonymous_login(ip, output_text):
    try:
        ftp = ftplib.FTP(ip)
        ftp.login()
        output_text.insert(tk.END, f"[+] Anonymous login successful on {ip}\n")
        ftp.quit()
        return True
    except ftplib.error_perm:
        output_text.insert(tk.END, f"[-] Anonymous login failed on {ip}\n")
        return False
    except Exception as e:
        output_text.insert(tk.END, f"[!] Error connecting to {ip}: {e}\n")
        return False

def scan_ip_range(start_ip, end_ip, output_text, scan_button, on_scan_complete):
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)
    for ip_int in range(int(start), int(end) + 1):
        ip = str(ipaddress.ip_address(ip_int))
        check_ftp_anonymous_login(ip, output_text)
    on_scan_complete(scan_button)

def create_gui():
    root = tk.Tk()
    root.title("Anonymous FTP Scanner")
    root.configure(bg="black")

    def scan():
        start_ip = start_ip_entry.get()
        end_ip = end_ip_entry.get()
        scan_button.config(state=tk.DISABLED)
        output_text.delete(1.0, tk.END)
        threading.Thread(target=scan_ip_range, args=(start_ip, end_ip, output_text, scan_button, on_scan_complete)).start()

    def on_scan_complete(scan_button):
        scan_button.config(state=tk.NORMAL)
        messagebox.showinfo("Scan Complete", "Scanning of IP range is complete.")

    title_label = tk.Label(root, text="Anonymous FTP Scanner", fg="red", bg="black", font=("Helvetica", 16))
    title_label.pack(pady=10)

    start_ip_label = tk.Label(root, text="Start IP Address:", fg="red", bg="black")
    start_ip_label.pack()
    start_ip_entry = tk.Entry(root, width=30)
    start_ip_entry.pack(pady=5)

    end_ip_label = tk.Label(root, text="End IP Address:", fg="red", bg="black")
    end_ip_label.pack()
    end_ip_entry = tk.Entry(root, width=30)
    end_ip_entry.pack(pady=5)

    scan_button = tk.Button(root, text="Scan", command=scan, bg="red", fg="black", activebackground="darkred")
    scan_button.pack(pady=10)

    output_text = scrolledtext.ScrolledText(root, width=50, height=15, bg="black", fg="red", insertbackground="red")
    output_text.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
