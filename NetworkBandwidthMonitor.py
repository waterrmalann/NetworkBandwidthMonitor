# NetworkBandwidthMonitor.py
# Written by: https://github.com/posetack
# Written on: 15th May, 2020
# Written in: Python 3.7 w/ Tkinter

import tkinter as tk
from psutil import net_io_counters

# Variables for use in the size() function.
KB = float(1024)
MB = float(KB ** 2) # 1,048,576
GB = float(KB ** 3) # 1,073,741,824
TB = float(KB ** 4) # 1,099,511,627,776
def size(B):
	"""Credits: https://stackoverflow.com/a/31631711 (Improved version of it.)"""
	
	B = float(B)
	if B < KB: return f"{B} Bytes"
	elif KB <= B < MB: return f"{B/KB:.2f} KB"
	elif MB <= B < GB: return f"{B/MB:.2f} MB"
	elif GB <= B < TB: return f"{B/GB:.2f} GB"
	elif TB <= B: return f"{B/TB:.2f} TB"

## Constants
WINDOW_SIZE = (400, 400)  # Width x Height
WINDOW_RESIZEABLE = False  # If the window is resizeable or not.
REFRESH_DELAY = 1000 # Window update delay in ms.

## Variables
last_upload, last_download, upload_speed, down_speed = 0, 0, 0, 0

## Initializing
window = tk.Tk()

window.title("Network Bandwidth Monitor")  # Setting the window title.
window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")  # Setting the window size.
window.resizable(width = WINDOW_RESIZEABLE, height = WINDOW_RESIZEABLE)  # We now lock the window.

label_total_upload_header = tk.Label(text = "Total Upload:", font = "Quicksand 12 bold")
label_total_upload_header.pack()
label_total_upload = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_total_upload.pack()

label_total_download_header = tk.Label(text = "Total Download:", font = "Quicksand 12 bold")
label_total_download_header.pack()
label_total_download = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_total_download.pack()

label_total_usage_header = tk.Label(text = "Total Usage:", font = "Quicksand 12 bold")
label_total_usage_header.pack()
label_total_usage = tk.Label(text = "Calculating...\n", font = "Quicksand 12")
label_total_usage.pack()

label_upload_header = tk.Label(text = "Upload:", font = "Quicksand 12 bold")
label_upload_header.pack()
label_upload = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_upload.pack()

label_download_header = tk.Label(text = "Download:", font = "Quicksand 12 bold")
label_download_header.pack()
label_download = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_download.pack()

attribution = tk.Label(text = "\n~ posetack ~", font = "Quicksand 11 italic")
attribution.pack()

# Updating Labels
def update():
	global last_upload, last_download, upload_speed, down_speed
	counter = net_io_counters()

	upload = counter.bytes_sent
	download = counter.bytes_recv
	total = upload + download

	if last_upload > 0:
		if upload < last_upload:
			upload_speed = 0
		else:
			upload_speed = upload - last_upload

	if last_download > 0:
		if download < last_download:
			down_speed = 0
		else:
			down_speed = download - last_download

	last_upload = upload
	last_download = download
	
	label_total_upload["text"] = f"{size(upload)} ({upload} Bytes)"
	label_total_download["text"] = f"{size(download)} ({download} Bytes)"
	label_total_usage["text"] = f"{size(total)}\n"
	
	label_upload["text"] = size(upload_speed)
	label_download["text"] = size(down_speed)
	
	label_total_upload.pack()
	label_total_download.pack()
	label_total_usage.pack()
	label_upload.pack()
	label_download.pack()
	
	window.after(REFRESH_DELAY, update)  # reschedule event in refresh delay.

window.after(REFRESH_DELAY, update)
window.mainloop()
