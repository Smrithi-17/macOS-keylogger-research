# macOS Keylogger for Cybersecurity Research

*Disclaimer:* This keylogger is intended for educational and cybersecurity research purposes only. The use of this software for any unauthorized or illegal activities is strictly prohibited. The author is not responsible for any misuse of this code. Ensure you have explicit permission before running this on any system you do not own.

## Purpose

This project demonstrates a basic keylogger implementation on macOS using Python and the pynput library. It logs keystrokes to a text file for educational exploration of system monitoring techniques.

## Features

* Captures standard keyboard input.
* Logs special keys (e.g., Shift, Ctrl, Tab).
* Saves keystrokes with timestamps to a log file.
* Exits when the Escape key is pressed.

## Limitations

* This is a basic implementation and may not capture all types of input (e.g., mouse clicks, clipboard data).
* It might be detectable by antivirus software or other security tools.
* Persistence and stealth features are not implemented in this basic version.

## Installation

1.  Ensure you have Python 3 installed.
2.  Clone this repository: git clone https://github.com/Smrithi-17/macOS-keylogger-research.git
3.  Navigate to the project directory: cd macOS-keylogger-research
4.  Create and activate a virtual environment (recommended):
    bash
    python3 -m venv keylogger_env
    source keylogger_env/bin/activate
    
5.  Install the pynput library:
    bash
    pip install pynput
    

## Usage

1.  Run the keylogger script: python keylogger.py
2.  Keystrokes will be logged to a file named keylog-YYYYMMDD-HHMMSS.txt in the same directory.
3.  To stop the keylogger, press the Esc key in the terminal where the script is running.

## Ethical Considerations

It is crucial to understand the ethical and legal implications of using keyloggers. *Never use this software without explicit permission on systems you do not own.* Unauthorized use can lead to severe legal consequences. This project is purely for educational purposes to understand how such tools work and how to defend against them.

## License

 [MIT License]
