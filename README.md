
# USB Automation 🔌💻

A lightweight Python script that automates a task when **your personal USB drive** is connected. It works by verifying the **Volume Name**, **Serial Number**, and **Size** of the USB, ensuring only your device can trigger the action.

---

## 🔍 Features

- Detects **your unique USB** using:
  - `VolumeName`
  - `VolumeSerialNumber`
  - USB size
- Triggers a **custom action** (e.g., open a file) when your USB is detected.
- Built using native **Windows tools** like `wmic` and Python’s `os.popen()`.

---

## 💡 Use Case

Ideal for:

- **Personal automation**: Launch a file, script, or program only when your USB is plugged in.
- **Security-sensitive environments**: Ensure only a specific, authenticated USB can trigger automation.
- **Portable automation tools**: Carry your automation on a USB drive and have it run automatically on plug-in.

---

## 🧠 How It Works

1. Continuously scans for USB drives using `wmic`.
2. Compares connected USBs with your configured:
   - **Volume Name** (`MY NAME`)
   - **Serial Number** (`C6A7547D`)
   - **Size** (`30748426240` bytes)
3. Once a match is found, it:
   - Flags the USB as authenticated.
   - Executes a custom action (e.g., opens `E:/java.txt`).

---

## 🔧 Installation

1. Ensure you are on **Windows** with **Python 3.x** installed.
2. Clone or download this project.
3. Update the script with:
   - Your USB's **Volume Name**
   - **Serial Number**
   - **Size**
   - Desired **file path** to execute.

---

## ▶️ Usage

Run the script in a terminal or double-click the `.py` file:

```bash
python usb_automation.py
```

---

## 🧪 Example Code

```python
import os

class Usb_Automation:
    def __init__(self):
        self.this_is_my_usb = False

    def First_level_security(self):
        while not self.this_is_my_usb:
            v = os.popen(
                'wmic logicaldisk where drivetype=2 get description, volumename, volumeserialnumber, size'
            ).readlines()
            for i in v:
                if 'Removable Disk  30748426240  MY NAME     C6A7547D            \n' == i:
                    self.this_is_my_usb = True
                    os.startfile('E:/java.txt')

start = Usb_Automation()
start.First_level_security()
```

---

## ⚙️ Configuration

Change the following values in the script to match your USB:

- **Volume Name**: Replace `"MY NAME"`
- **Serial Number**: Replace `"C6A7547D"`
- **Size**: Replace `30748426240`
- **Target File Path**: Replace `'E:/java.txt'`

To find your USB’s details, run this command in PowerShell:

```powershell
Get-WmiObject Win32_LogicalDisk | Format-List VolumeName,VolumeSerialNumber,Size
```

---

## 📦 Requirements

- **OS**: Windows
- **Python**: 3.x
- **Permissions**:
  - Access to `wmic`
  - Read permissions for the target file

---

## 🛠 Troubleshooting

- **File not opening?** Ensure the file path is correct and accessible.
- **USB not recognized?** Double-check the volume name, serial, and size.
- **Script not running?** Ensure Python is installed and added to PATH.

---

## 👤 Contributors

**Ellalan (whitedevilprogrammer)**  
[GitHub Profile »](https://github.com/whitedevilprogrammer)

---

## 📄 License

This project is released under the **MIT License**. See `LICENSE` file for details.
