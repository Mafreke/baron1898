import senko
import machine
import network
from connectwlan import *


OTA = senko.Senko(
  user="Mafreke", # Required
  repo="baron1898", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="src", # Optional: Defaults to "app"
  files = ["main.py"]
}

connected = connectwlan()
if connected:
  if OTA.update():
    print("updated to the latest version! Rebooting...")
    machine.reset()
  else:
    print("Version up to date!")
else:
  print("There was no connection to a network so no updates are downloaded")
