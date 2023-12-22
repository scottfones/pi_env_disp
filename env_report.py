#!/usr/bin/python
import time
from gpiozero import CPUTemperature
from sense_hat import SenseHat

sense = SenseHat()

while True:
    cpu = CPUTemperature()
    cpu_temp = cpu.temperature

    cpu_text_color = [25, 125, 25]
    cpu_back_color = [0, 0, 0]

    if cpu_temp > 50 and cpu_temp < 60:
        cpu_text_color = [140, 120, 0]
    elif cpu_temp >= 60:
        cpu_text_color = [125, 125, 125]
        cpu_back_color = [100, 0, 0]

    sense.show_message(
        f"{cpu_temp:.1f}", text_colour=cpu_text_color, back_colour=cpu_back_color
    )

    time.sleep(0.25)

    case_temp = sense.get_temperature()
    sense.show_message(f"{case_temp:.1f}", text_colour=[100, 100, 100])

    time.sleep(0.25)

    case_humid = sense.get_humidity()
    sense.show_message(f"{case_humid:.1f}", text_colour=[25, 100, 100])

    time.sleep(30)
