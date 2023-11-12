from enum import Enum
from typing import Optional

class ColorPresetEnum(str, Enum):
	Warm = "4"
	Native = "5"
	Cool = "6"
	Bluish = "8"
	UserColor = "11"


class MonitorInfo():
	def __init__(
		self,
		index, 
		Availability,
		Caption,
		ConfigManagerErrorCode,
		ConfigManagerUserConfig,
		CreationClassName,
		Description,
		DeviceID,
		MonitorManufacturer,
		MonitorType,
		Name,
		PixelsPerXLogicalInch,
		PixelsPerYLogicalInch,
		PNPDeviceID,
		ScreenHeight,
		ScreenWidth,
		Status,
		SystemCreationClassName,
		SystemName
	) -> None:
		self.index = index
		self.Availability = Availability
		self.Caption = Caption
		self.ConfigManagerErrorCode = ConfigManagerErrorCode
		self.ConfigManagerUserConfig = ConfigManagerUserConfig
		self.CreationClassName = CreationClassName
		self.Description = Description
		self.DeviceID = DeviceID
		self.MonitorManufacturer = MonitorManufacturer
		self.MonitorType = MonitorType
		self.Name = Name
		self.PixelsPerXLogicalInch = PixelsPerXLogicalInch
		self.PixelsPerYLogicalInch = PixelsPerYLogicalInch
		self.PNPDeviceID = PNPDeviceID
		self.ScreenHeight = ScreenHeight
		self.ScreenWidth = ScreenWidth
		self.Status = Status
		self.SystemCreationClassName = SystemCreationClassName
		self.SystemName = SystemName

	index: Optional[int]
	Availability: Optional[int]
	Caption: Optional[str]
	ConfigManagerErrorCode: Optional[int]
	ConfigManagerUserConfig: Optional[bool]
	CreationClassName: Optional[str]
	Description: Optional[str]
	DeviceID: Optional[str]
	MonitorManufacturer: Optional[str]
	MonitorType: Optional[str]
	Name: Optional[str]
	PixelsPerXLogicalInch: Optional[int]
	PixelsPerYLogicalInch: Optional[int]
	PNPDeviceID: Optional[str]
	ScreenHeight: Optional[int]
	ScreenWidth: Optional[int]
	Status: Optional[str]
	SystemCreationClassName: Optional[str]
	SystemName: Optional[str]
	IsPrimary: Optional[bool] = None
	Brightness: Optional[int] = None
	Contrast: Optional[int] = None
	ColorPreset: Optional[ColorPresetEnum] = None
	
	def resp_color_preset(self):
		dict = {
			"4": "[4] Warm",
			"5": "[5] Native",
			"6": "[6] Cool",
			"8": "[8] Bluish",
			"11": "[11] User Color",
		}
		return  dict[self.ColorPreset] if self.ColorPreset else None
	
	def __repr__(self):
		return \
			f"Monitor {self.index}\n"\
			+ f"Name: {self.Caption}\n"\
			+ f"Description: {self.Description}\n"\
			+ f"DeviceID: {self.DeviceID}\n"\
			+ f"ScreenHeight: {self.ScreenHeight}\n"\
			+ f"ScreenWidth: {self.ScreenWidth}\n"\
			+ f"Status: {self.Status}\n"\
        	+ f"IsPrimary: {self.IsPrimary}\n"\
        	+ f"Brightness: {self.Brightness}\n"\
        	+ f"Contrast: {self.Contrast}\n"\
        	+ f"ColorPreset: {self.resp_color_preset()}\n"
	
   
def convert_win32_to_monitor(index, win32_monitor) -> MonitorInfo:
	return MonitorInfo(
		index=index,
		Availability=win32_monitor.Availability,
		Caption=win32_monitor.Caption,
		ConfigManagerErrorCode=win32_monitor.ConfigManagerErrorCode,
		ConfigManagerUserConfig=win32_monitor.ConfigManagerUserConfig,
		CreationClassName=win32_monitor.CreationClassName,
		Description=win32_monitor.Description,
		DeviceID=win32_monitor.DeviceID,
		MonitorManufacturer=win32_monitor.MonitorManufacturer,
		MonitorType=win32_monitor.MonitorType,
		Name=win32_monitor.Name,
		PixelsPerXLogicalInch=win32_monitor.PixelsPerXLogicalInch,
		PixelsPerYLogicalInch=win32_monitor.PixelsPerYLogicalInch,
		PNPDeviceID=win32_monitor.PNPDeviceID,
		Status=win32_monitor.Status,
		SystemCreationClassName=win32_monitor.SystemCreationClassName,
		SystemName=win32_monitor.SystemName,
		ScreenHeight=win32_monitor.ScreenHeight,
		ScreenWidth=win32_monitor.ScreenWidth,
	)
