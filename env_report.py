#!/usr/bin/python
import time
from gpiozero import CPUTemperature
from sense_hat import SenseHat


def construct_inner(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        x, x, x, x, x, x, x, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, x, x, o, o, x,
        x, o, o, x, x, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, x, x, x, x, x, x, x,
    ]

    return ring


def construct_mid(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, o, o, o, o, o, o, o,
        o, x, x, x, x, x, x, o,
        o, x, x, x, x, x, x, o,
        o, x, x, o, o, x, x, o,
        o, x, x, o, o, x, x, o,
        o, x, x, x, x, x, x, o,
        o, x, x, x, x, x, x, o,
        o, o, o, o, o, o, o, o,
    ]

    return ring


def construct_outer(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
        x, x, o, o, o, o, x, x,
        x, x, o, o, o, o, x, x,
        x, x, o, o, o, o, x, x,
        x, x, o, o, o, o, x, x,
        x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x,
    ]

    return ring


def detailed_display(
    colour_bg: list[int], colour_fg: list[int], cpu_temp: float, sense: SenseHat
):
    sense.show_message(
        f"{cpu_temp:.1f}",
        text_colour=colour_fg,
        back_colour=colour_bg,
    )

    time.sleep(0.25)

    case_temp = sense.get_temperature()
    sense.show_message(f"{case_temp:.1f}", text_colour=[100, 100, 100])

    time.sleep(0.25)

    case_humid = sense.get_humidity()
    sense.show_message(f"{case_humid:.1f}", text_colour=[25, 100, 100])


def simple_display(colour_bg: list[int], colour_fg: list[int], sense: SenseHat):
    secs = time.localtime(time.time()).tm_sec

    ring = []
    if secs < 20:
        ring = construct_outer(colour_bg, colour_fg)
    elif secs < 40:
        ring = construct_mid(colour_bg, colour_fg)
    else:
        ring = construct_inner(colour_bg, colour_fg)

    sense.set_pixels(ring)


def main():
    cpu = CPUTemperature()
    sense = SenseHat()

    while True:
        colour_fg = [25, 125, 25]
        colour_bg = [0, 0, 0]

        cpu_temp = cpu.temperature
        if cpu_temp > 50 and cpu_temp < 60:
            colour_fg = [140, 120, 0]
        elif cpu_temp >= 60:
            colour_fg = [125, 125, 125]
            colour_bg = [100, 0, 0]

        if sense.stick.get_events():
            detailed_display(colour_bg, colour_fg, cpu_temp, sense)
        else:
            simple_display(colour_bg, colour_fg, sense)

        time.sleep(1)


if __name__ == "__main__":
    main()
