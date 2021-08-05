
if __name__ == '__main__':
    import win32gui as wgui
    import app.auto_gui.window_controller_factory as factory
    import time

    main_window = factory.get_sap_main_window_controller()
    main_window.set_window_foreground()
    time.sleep(.2)
    details_window = factory.get_sap_details_window_controller()
    print(main_window.is_window_foreground())
    print(details_window.is_window_foreground())