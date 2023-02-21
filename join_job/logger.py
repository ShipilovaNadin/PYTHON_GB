# Логгирование
from datetime import datetime as dt
from time import time

def temperature_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.cvs", "a") as file:
        file.write("{};temperature;{}"
                   .format(time, data))

def preassure_logger():
    time = dt.now().strftime("%H:%M")
    with open("log.cvs", "a") as file:
        file.write("{};preassure;{}"
                   .format(time, data))

def wind_speed_logger():
    time = dt.now().strftime("%H:%M")
    with open("log.cvs", "a") as file:
        file.write("{};wind_speed;{}"
                   .format(time, data))
