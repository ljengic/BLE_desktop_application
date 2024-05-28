python -m PyQt5.uic.pyuic -x ./package/main_app/gui.ui -o ./package/main_app/gui.py
python -m PyQt5.uic.pyuic -x ./package/home/gui_home.ui -o ./package/home/gui_home.py
python -m PyQt5.uic.pyuic -x ./package/ble/gui_ble.ui -o ./package/ble/gui_ble.py
python -m PyQt5.uic.pyuic -x ./package/ble/gui_not_connected.ui -o ./package/ble/gui_not_connected.py
python -m PyQt5.uic.pyuic -x ./package/measure/gui_measure.ui -o ./package/measure/gui_measure.py
python -m PyQt5.uic.pyuic -x ./package/medicine/gui_add_medication.ui -o ./package/medicine/gui_add_medication.py
python -m PyQt5.uic.pyuic -x ./package/medicine/gui_medicine.ui -o ./package/medicine/gui_medicine.py
python -m PyQt5.uic.pyuic -x ./package/results/gui_results.ui -o ./package/results/gui_results.py
python -m PyQt5.uic.pyuic -x ./package/graphs/gui_graph_widget.ui -o ./package/graphs/gui_graph_widget.py
python -m PyQt5.uic.pyuic -x ./package/graphs/gui_check_box_widget.ui -o ./package/graphs/gui_check_box_widget.py
python -m PyQt5.uic.pyuic -x ./package/patients/gui_select_patient.ui -o ./package/patients/gui_select_patient.py
python -m PyQt5.uic.pyuic -x ./package/patients/gui_invalid_data.ui -o ./package/patients/gui_invalid_data.py


python -m PyQt5.pyrcc_main -o ./images/resources_rc.py ./images/resources.qrc
::copy "./images/resources_rc.py" "./resources_rc.py"