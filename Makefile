ui: ui_raw/initial_window.ui ui_raw/main_window.ui ui_raw/save_func_dialog.ui
	pyuic5 ui_raw/initial_window.ui -o ui/initial_window.py
	pyuic5 ui_raw/main_window.ui -o ui/main_window.py
	pyuic5 ui_raw/save_dialog.ui -o ui/save_window.py
