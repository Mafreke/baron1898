import senko
import machine
from connectwlan import *


OTA = senko.Senko(
  user="Mafreke", # Required
  repo="baron1898", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="src", # Optional: Defaults to "app"
  files = ["boot.py", "main.py"]
)

connected = connectwlan()

if OTA.update() and connected is True:
    print("updated to the latest version! Rebooting...")
    machine.reset()
else:
    print("Version up to date!")