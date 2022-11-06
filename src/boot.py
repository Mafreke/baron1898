import senko
import machine
import network

GITHUBURL = "https://github.com/Mafreke/baron1898/blob/master/src/"

OTA = senko.Senko(
  user="Mafreke", # Required
  repo="baron1898", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="src", # Optional: Defaults to "app"
  files = ["boot.py", "main.py"]
)

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
while not wlan.isconnected():      # check if the station is connected to an AP
    wlan.connect('WiFi-2.4-E1B3', 'Amortje2016') # connect to an AP
wlan.config('mac')      # get the interface's MAC address
print(wlan.ifconfig())

if OTA.update():
    print("updated to the latest version! Rebooting...")
    machine.reset()
else:
    print("Version up to date!")