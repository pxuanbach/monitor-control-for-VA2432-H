
from typing import List, Optional
import monitorcontrol.monitorcontrol as mc
import screen_brightness_control as sbc
import screeninfo as si
import wmi
from core.monitor_info import MonitorInfo, ColorPresetEnum, convert_win32_to_monitor


def get_all_displays() -> List[MonitorInfo]:
	w = wmi.WMI()
	win32_monitors = w.query("SELECT * FROM Win32_DesktopMonitor")
	results = []
	mc_monitors = mc.get_monitors()
	si_monitors = si.get_monitors()
	for i, m in enumerate(win32_monitors):
		monitor = convert_win32_to_monitor(i, m)

		# get brightness
		b = sbc.get_brightness(display=i)
		monitor.Brightness = b[0]

		# get contrast, color preset
		try:
			with mc_monitors[i]:
				monitor.Contrast = mc_monitors[i].get_contrast()
				monitor.ColorPreset = str(mc_monitors[i].get_color_preset())
		except:
			pass
		
		# this monitor is primary
		monitor.IsPrimary = si_monitors[i].is_primary
		results.append(monitor)
	return results


def set_display_brightness(display_index: int, value: int):
    """Sets the brightness level of display to a given value.

    Args:
        display_index (int): Index of monitors.
        value (int): New brightness value (typically 0-100).
    """
    try:
        sbc.set_brightness(value=value, display=display_index)
    except Exception as e:
        print(str(e))
        return False
    return True


def set_display_contrast(display_index: int, value: int):
    """Sets the monitors back-light contrast.

    Args:
        display_index (int): Index of monitors.
        value (int): New contrast value (typically 0-100).
    """
    mc_monitors = mc.get_monitors()
    try:
        with mc_monitors[display_index]:
            mc_monitors[display_index].set_contrast(value)
    except Exception as e:
        print(str(e))
        return False
    return True


def set_display_color_preset(display_index: int, value: int):
    """Sets the monitors color preset.

    Args:
        display_index (int): Index of monitors.
        value (int): An integer color preset from ColorPresetEnum
    """
    mc_monitors = mc.get_monitors()
    try:
        with mc_monitors[display_index]:
            mc_monitors[display_index].set_color_preset(value)
    except Exception as e:
        print(str(e))
        return False
    return True