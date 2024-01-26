# this is a test200
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin, Timer

firmware_url = "https://raw.githubusercontent.com/cmillsy/chessboard1/main/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=30, mode=Timer.PERIODIC, callback=blink)
