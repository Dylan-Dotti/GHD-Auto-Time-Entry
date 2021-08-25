
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator


    main_wc = factory.get_sap_main_window_controller()
    main_wc.set_window_foreground()
    main_kc = KeyboardController(main_wc)
    main_nav = SapMainWindowNavigator(main_kc)
    reset_nav, reset_kc = main_nav.delete_all_entries()
