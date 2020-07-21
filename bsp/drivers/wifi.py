from espressif.esp32net import esp32wifi as drv
from wireless import wifi

def init():
    drv.auto_init()
    return drv

def interface():
    return wifi






