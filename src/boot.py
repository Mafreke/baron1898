import senko
import machine

OTA = senko.Senko(
  user="Mafreke", # Required
  repo="baron1898", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="src", # Optional: Defaults to "app"
  files = ["boot.py", "main.py"]
)

import connectwlan

if OTA.update():
    print("updated to the latest version! Rebooting...")
    machine.reset()
else:
    print("Version up to date!")