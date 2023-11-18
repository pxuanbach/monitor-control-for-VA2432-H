# Monitor Control For VA2432-H

## Dependencies

[Python](https://www.python.org/) version 3.8

Controlling the screen based on the following packages
- [screen_brightness_control](https://crozzers.github.io/screen_brightness_control/source.html)
- [monitorcontrol](https://newam.github.io/monitorcontrol/)
- [WMI](https://pypi.org/project/WMI/)
- [screeninfo](https://pypi.org/project/screeninfo/)

CLI application based on the following packages
- [Typer](https://typer.tiangolo.com/)

GUI application based on the following packages
- [Kivy](https://kivy.org/)

## CLI application

### Usage

With exe file

```bash
cli.exe --help
```

With Python file (Must install all the packages in the `requirements.txt`)

```bash
python cli.py --help
```

Example
```bash
cli.exe list

cli.exe brightness --help
cli.exe brightness --method get 1
cli.exe brightness --method set 1 70
```

### Build

I use [PyInstaller](https://pyinstaller.org/en/stable/) to build my CLI application into an exe file.

```bash
pip install pyinstaller

pyinstaller cli.py
```

Then you can find the exe file at the path `dist/cli/cli.exe`.