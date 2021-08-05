
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator

    main_wc = factory.get_sap_main_window_controller()
    main_wc.set_window_foreground()
    main_kc = KeyboardController(main_wc)

    main_nav = SapMainWindowNavigator(main_kc)
    details_nav = main_nav.open_cell_details()
    # navigation in the new window currently doesn't work
    # due to the main window no longer having focus
    details_wc = factory.get_sap_details_window_controller()
    details_wc.wait_for_window_foreground()
    details_kc = KeyboardController(details_wc)
    details_nav.move_to_short_text_field()
    details_kc.write_text('59972, 59973, 59974, 59975, 59976, 59977')
    details_nav.confirm_and_close()
