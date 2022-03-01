import traceback
from app.gui.main_window import launch_window
from app.option_preferences.option_prefs_json_interface import OptionPrefsJsonInterface


def main():
    print('GHD Auto Time Entry, v1.1.1')

    option_prefs_interface = OptionPrefsJsonInterface()

    # load option prefs
    try:
        option_prefs = option_prefs_interface.load_option_prefs()
    except:
        print('\n', traceback.format_exc(), '\n')
        option_prefs = None

    # launch app
    try:
        launch_window(option_prefs=option_prefs)
    except:
        print('\n', 'App crashed due to exception: ', '\n', traceback.format_exc(), '\n')
    finally:
        # save option prefs after running app
        try:
            option_prefs_interface.save_option_prefs(option_prefs)
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    main()