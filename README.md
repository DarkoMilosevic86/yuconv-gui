YuConv GUI is a submodule of the YuConv package and enables the use of YuConv through a graphical user interface.

## Download YuConv GUI

You can download YuConv GUI from the page [https://github.com/DarkoMilosevic86/yuconv-gui/releases](https://github.com/DarkoMilosevic86/yuconv-gui/releases)

## Contribution

You can also contribute to the development of YuConv GUI or report issues in the following ways:

### Cloning the repository

Since YuConv GUI is a submodule of the YuConv package, you can clone the repository using the following command:

```
git clone --recurse https://github.com/DarkoMilosevic86/yuconv.git
```

### Building YuConv GUI

To build YuConv GUI, please follow these steps:

* Creating a virtual environment (VENV)

To install the required packages, you first need to create a virtual environment (VENV), which can be done as follows:

```
cd yuconv/gui
python -m venv .venv
cd .venv/scripts
activate
```

* Installing required packages

Once you have created and activated the virtual environment (VENV), you need to update PIP and install the necessary packages from the requirements.txt file:

```
python -m pip install --upgrade pip
pip install -r ../../requirements.txt
```

This way, you have installed all the required packages. 

Note:
As you may have noticed, `../../` is used to navigate two directories up from the `scripts` directory, as the requirements.txt file is located in the `gui` directory.
Now you can test the GUI using the command:

```
python gui.py
```

You can also build an executable `.exe` program using pyinstaller using the following command:

```
pyinstaller --noconsole --icon="res/icon.ico" --version-file="res/version.txt" gui.py
```

To build the installer, you need to install the NSIS (Nullsoft Scriptable Install System) and to compile the `installer.nsi` script.

### Reporting issues

You can report issues with YuConv GUI on the [YuConv Issues](https://github.com/DarkoMilosevic86/yuconv/issues) page.
