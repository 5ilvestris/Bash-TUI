## 🐍 BashTUI.py: Python Interface for Bash dialog Checklist
This script, BashTUI.py, demonstrates how to utilize the powerful dialog utility from the Bash environment within a Python script to create a simple Text User Interface (TUI) checklist.

It allows a user to make multiple selections from a defined list of options, capturing the choices back into the Python environment for further processing.

## 🚀 Features
TUI Checklist: Presents a list of options in a TUI using the dialog command.

Feature Selection: Allows users to select multiple features/options.

Result Capture: Captures the selected options and prints them to the console.

Error Handling: Manages cases where the user cancels the dialog.

Temporary File Management: Uses a temporary file (/tmp/checklist_choices.txt) to capture dialog's output, and ensures it's removed afterward.

💻 Requirements
To run this script, you must have the dialog utility installed on your system. It is commonly available on most Linux distributions.

## Installation (if needed):

#### Debian/Ubuntu:

Bash

sudo apt-get install dialog
#### Red Hat/Fedora/CentOS:

```bash
sudo yum install dialog
# or
sudo dnf install dialog
```
## ⚙️ Usage
Save the provided Python code as BashTUI.py.

Run the script from your terminal:

```bash
python3 BashTUI.py
```
A TUI window will appear:
Use the arrow keys to navigate.
Press the Spacebar to toggle an option on or off (select/deselect).
Press Tab to switch between the "OK" and "Cancel" buttons.
Press Enter to confirm your selection ("OK") or cancel ("Cancel").
The script will clear the screen and print the results.

### Example Output (if AAA and CCC are selected):

```bash
--------- SONUC ---------
 You selected 2 of them.
- AAA
- CCC
```
