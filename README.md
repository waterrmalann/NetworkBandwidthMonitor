# Network Bandwidth Monitor

A simple application written in Python using Tkinter for monitoring real-time internet usage and speeds for both download and upload. It should run on both Windows (tested on Windows 10 and 7) and Linux (tested on Ubuntu 20.04.1) systems as long as Python and Tkinter are installed (not sure about Mac).

I wrote it as a console application to monitor my internet back when I had a data cap. I recently gave it a simple UI using Tkinter after learning a bit. I do think that my code is bad since I still have a lot to learn, so just keep that in mind if you're gonna go through it.

## Requirements

- [Python](https://www.python.org/) 3.7 or above.
- [Psutil](https://pypi.org/project/psutil/) (for network statistics)
- Tkinter (for the GUI)
- [Quicksand](https://www.dafont.com/quicksand.font) (pretty nice font)

### Freezing (Windows)

You can freeze the source to exe. I personally use [PyInstaller](https://www.pyinstaller.org/).
Run the following console command for the best results:
`pyinstaller NetworkBandwidthMonitor.py --onefile --noconsole`

### Todos

- Persistent statistics that doesn't get reset when the computer is restarted. (and a reset button)
- Config file instead of hardcoded configuration variables.

License
----

MIT License
