from typing import Literal
import typer
from typing_extensions import Annotated
from rich import print

from core.monitor_control import (
    get_all_displays, 
    get_display_brightness,
    set_display_brightness,
    get_display_contrast, 
    set_display_contrast,
    get_display_color_preset,
    set_display_color_preset,
    get_all_color_presets
)
from core.monitor_info import ColorPresetEnum, MethodEnum


app = typer.Typer(
    name="VA2432-H Monitor Control", 
    help="This is a CLI application that supports adjusting brightness, "\
        + "contrast, and pre-set color settings for the monitor instead of "\
        + "using physical buttons.",
    pretty_exceptions_short=False
)


@app.command()
def list():
    """
    Show information for all active displays.
    """
    monitors = get_all_displays()
    for monitor in monitors:
        print(monitor.__repr__())
    return


@app.command()
def list_color_preset(
    display_index: Annotated[int, typer.Argument(help="Index of monitors")]
):
    """
    Show all available color presets.
    """
    color_presets = get_all_color_presets(display_index)
    if len(color_presets) > 0:
        [print(c[0]) for c in color_presets]
    return


@app.command()
def brightness(
    method: Annotated[
        MethodEnum, typer.Option(case_sensitive=False)
    ] = MethodEnum.GET,
    *,
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[int, typer.Argument(
        help="<Method SET> New brightness value (typically 0-100)"
    )] = 80
):
    """
    Get or Set the brightness level of display to a given value.
    """
    if method == MethodEnum.SET:
        success = set_display_brightness(display_index, value)
        if success:
            return print("Change Brightness success!")
    elif method == MethodEnum.GET:
        result = get_display_brightness(display_index)
        if result != -1:
            return print(f"Brightness: {result}")
    return


@app.command()
def contrast(
    method: Annotated[
        MethodEnum, typer.Option(case_sensitive=False)
    ] = MethodEnum.GET,
    *,
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[int, typer.Argument(
        help="<Method SET> New contrast value (typically 0-100)"
    )] = 50
):
    """
    Get or Set the monitors back-light contrast.
    """
    if method == MethodEnum.SET:
        success = set_display_contrast(display_index, value)
        if success:
            return print("Change Contrast success!")
    elif method == MethodEnum.GET:
        result = get_display_contrast(display_index)
        if result != -1:
            return print(f"Contrast: {result}")
    return

@app.command()
def color_preset(
    method: Annotated[
        MethodEnum, typer.Option(case_sensitive=False)
    ] = MethodEnum.GET,
    *,
    display_index: Annotated[int, typer.Argument(help="Index of monitors")],
    value: Annotated[ColorPresetEnum, typer.Argument(
        help="<Method SET> New ColorPreset value in ColorPresetEnum",
        metavar="ColorPresetEnum"
    )] = ColorPresetEnum.Native
):
    """
    Get or Set the color preset of display to a given value.\n
    ColorPresetEnum: \n
        4: "Warm"\n
        5: "Native"\n
        6: "Cool"\n
        8: "Bluish"\n
        11: "User Color"
    """
    if method == MethodEnum.SET:
        success = set_display_color_preset(display_index, int(value))
        if success:
            return print("Change ColorPreset success!")
    elif method == MethodEnum.GET:
        color = get_display_color_preset(display_index)
        if color != "":
            return print(f"ColorPreset: {color}")
    return


if __name__ == "__main__":
    app()