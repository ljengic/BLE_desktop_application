python -m PyQt5.uic.pyuic -x ./package/main_app/gui.ui -o ./package/main_app/gui.py
python -m PyQt5.uic.pyuic -x ./package/home/gui_home.ui -o ./package/home/gui_home.py
python -m PyQt5.uic.pyuic -x ./package/ble/gui_ble.ui -o ./package/ble/gui_ble.py
python -m PyQt5.uic.pyuic -x ./package/patients/gui_patients.ui -o ./package/patients/gui_patients.py
python -m PyQt5.uic.pyuic -x ./package/measure/gui_measure.ui -o ./package/measure/gui_measure.py
python -m PyQt5.uic.pyuic -x ./package/results/gui_results.ui -o ./package/results/gui_results.py