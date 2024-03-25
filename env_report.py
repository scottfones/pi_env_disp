#!/usr/bin/python
import time
from gpiozero import CPUTemperature
from sense_hat import SenseHat
from pathlib import Path


def construct_boxes_a(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        x, x, x, x, x, x, x, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, x, x, x, x, x, x, x,
    ]
    return ring


def construct_boxes_b(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, o, o, o, o, o, o, o,
        o, x, x, x, x, x, x, o,
        o, x, o, o, o, o, x, o,
        o, x, o, o, o, o, x, o,
        o, x, o, o, o, o, x, o,
        o, x, o, o, o, o, x, o,
        o, x, x, x, x, x, x, o,
        o, o, o, o, o, o, o, o,
    ]
    return ring


def construct_boxes_c(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, x, x, x, x, o, o,
        o, o, x, o, o, x, o, o,
        o, o, x, o, o, x, o, o,
        o, o, x, x, x, x, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    return ring


def construct_boxes_d(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, x, x, o, o, o,
        o, o, o, x, x, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    return ring


def construct_columns_inner(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
        o, x, o, x, o, x, o, x,
    ]
    return ring


def construct_columns_outer(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
        x, o, x, o, x, o, x, o,
    ]
    return ring


def construct_field_inner(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
    ]
    return ring


def construct_field_outer(colour_bg: list[int], colour_fg: list[int]):
    o = colour_bg
    x = colour_fg

    # fmt: off
    ring = [
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
        x, o, x, o, x, o, x, o,
        o, x, o, x, o, x, o, x,
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
    ring = []
    ring_seq = [
        construct_boxes_a,
        construct_boxes_b,
        construct_boxes_b,
        construct_boxes_c,
        construct_boxes_c,
        construct_boxes_d,
        construct_boxes_d,
        construct_boxes_c,
        construct_boxes_c,
        construct_boxes_b,
        construct_boxes_b,
        construct_boxes_a,
    ]
    secs = time.localtime(time.time()).tm_sec % len(ring_seq)
    ring = ring_seq[secs](colour_bg, colour_fg)

    sense.set_pixels(ring)


def soda_display(sense: SenseHat, soda_count: int):
    sense.show_message("+1", text_colour=[92, 64, 51])
    sense.show_message(f"Refills: {soda_count}", text_colour=[92, 64, 51])


def soda_write(soda_count: int, soda_file: Path):
    with open(soda_file, "w") as f:
        f.write(str(soda_count))


def main():
    cpu = CPUTemperature()
    sense = SenseHat()
    soda_count = 0
    soda_file = Path("/home/scott/Applications/EnvDisplay/pi_env_disp/soda_count.txt")

    if soda_file.exists():
        with open(soda_file) as f:
            soda_count = int(f.readline().strip())
    else:
        soda_file.touch()
        with open(soda_file, "w") as f:
            f.write("0")

    while True:
        colour_fg = [0, 50, 0]
        colour_bg = [0, 0, 0]

        cpu_temp = cpu.temperature
        if cpu_temp > 55 and cpu_temp < 65:
            colour_fg = [140, 120, 0]
        elif cpu_temp >= 65:
            colour_fg = [125, 0, 0]
            colour_bg = [50, 0, 0]

        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    detailed_display(colour_bg, colour_fg, cpu_temp, sense)
                elif event.direction == "left":
                    soda_count += 1
                    soda_display(sense, soda_count)
                    soda_write(soda_count, soda_file)
                elif event.direction == "right":
                    soda_display(sense, soda_count)

        simple_display(colour_bg, colour_fg, sense)

        time.sleep(1)


if __name__ == "__main__":
    main()
