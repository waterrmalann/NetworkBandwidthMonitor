# Network Bandwidth Monitor

A simple Python application with an equally simple windows native UI designed with the Tkinter module. The program is made for monitoring network bandwith monitor, it calculates the average speed, data usage for both downloads and uploads and total usage statistics. I originally made the program as a console application to monitor my internet back when I had a data cap. I recently gave it simple UI using Tkinter after learning it a bit, I do think my code is really bad as I still have a lot to learn, so be advised if you're gonna go through it.

## Requirements

- [Python](https://www.python.org/) 3.7 or above.
- [Psutil](https://pypi.org/project/psutil/) (for network statistics)
- Tkinter (for the GUI)
- [Quicksand](https://www.dafont.com/quicksand.font) (pretty nice font)

### Notes

This program is written specifically to run on Windows platforms. I have not tested this on other platforms and it most likely won't even work (It seems to run fine on Windows 7, 8, and 10 systems).

### Freezing

You can freeze the source to exe. I personally use and recommend [PyInstaller](https://www.pyinstaller.org/).
Run the following console command for the best results:
`pyinstaller NetworkBandwidthMonitor.py --onefile --noconsole`

### Todos

- Persistent statistics that doesn't get reset when the computer is restarted. (and a reset button)
- Config file instead of hardcoded configuration variables.

License
----

MIT License
