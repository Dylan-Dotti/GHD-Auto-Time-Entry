dev_setup:
	./setup.bat

build_exe:
	./app/build.bat

build_ui:
	./app/gui/generate_configure_columns_windows.bat
	./app/gui/generate_main_window.bat

test_zd_reader:
	python -m unittest discover testing/data_formatter

