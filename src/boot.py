import senko
import machine
import network

OTA = senko.Senko(
    user="Fre",
    repo="baronsim",
    files=["boot.py", "main.py", "/lib"]
)

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('WiFi-2.4-E1B3', 'Amortje2016') # connect to an AP
wlan.config('mac')      # get the interface's MAC address
print(wlan.ifconfig())

if OTA.update():
    print("updated to the latest version! Rebooting...")
    machine.reset()
