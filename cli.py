import typer
from typing_extensions import Annotated
from rich import print

from core.monitor_control import (
    get_all_displays, 
    set_display_brightness, 
    set_display_contrast,
    set_display_color_preset
)
from core.monitor_info import ColorPresetEnum


app = typer.Typer(
    name="VA2432-H Monitor Control", 
    help="This is a CLI application that supports adjusting brightness, "\
        + "contrast, and pre-set color settings for the monitor instead of "\
        + "using physical buttons.",
    pretty_exceptions_short=False
)


@app.command()
def list_display():
    """
    Show information for all active displays.
    """
    monitors = get_all_displays()
    for monitor in monitors:
        print(monitor.__repr__())
    return


@app.command()
def brightness(
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[int, typer.Argument(help="New brightness value (typically 0-100)")]
):
    """
    Sets the brightness level of display to a given value.
    """
    success = set_display_brightness(display_index, value)
    if success:
        return print("Change Brightness success!")
    return


@app.command()
def contrast(
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[int, typer.Argument(help="New contrast value (typically 0-100)")]
):
    """
    Sets the monitors back-light contrast.
    """
    success = set_display_contrast(display_index, value)
    if success:
        return print("Change Contrast success!")
    return


@app.command()
def color_preset(
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[ColorPresetEnum, typer.Argument(
        help="New ColorPreset value in ColorPresetEnum",
        metavar="ColorPresetEnum"
    )] = ColorPresetEnum.Native
):
    """
    Sets the color preset of display to a given value.\n
    ColorPresetEnum: \n
        4: "Warm"\n
        5: "Native"\n
        6: "Cool"\n
        8: "Bluish"\n
        11: "User Color"
    """
    success = set_display_color_preset(display_index, int(value))
    if success:
        return print("Change ColorPreset success!")
    return


if __name__ == "__main__":
    app()