# BLE desktop application for communication with stm32wb microcontroller

## converting .ui to .py:
python -m PyQt5.uic.pyuic -x gui.ui -o gui.py

## converting .qrc to .py
python -m PyQt5.pyrcc_main -o resources_rc.py resources.qrc

## Applying qss to gui
in app.py put path to .qss file
example:  ./images/name.qss 