import traceback
from app.gui.main_window import launch_window
from app.option_preferences.option_prefs_json_interface import OptionPrefsJsonInterface


def main():
    option_prefs_interface = OptionPrefsJsonInterface()
    try:
        option_prefs = option_prefs_interface.load_option_prefs()
    except:
        print(traceback.format_exc())
        option_prefs = None
    try:
        launch_window(option_prefs=option_prefs)
    finally:
        try:
            option_prefs_interface.save_option_prefs(option_prefs)
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    main()