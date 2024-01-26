# this is a test
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/cmillsy/chessboard1/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

from machine import Pin, Timer
led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
