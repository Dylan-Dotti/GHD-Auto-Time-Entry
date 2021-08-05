
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_window_navigator import SapWindowNavigator

    wc = factory.get_sap_main_window_controller()
    wc.set_window_foreground()
    wc.wait_for_window_foreground()

    nav = SapWindowNavigator()
    details_nav = nav.open_cell_details()
    # navigation in the new window currently doesn't work
    # due to the main window no longer having focus
    details_nav.move_to_short_text_field()
    kc = KeyboardController(wc)
    kc.write_text('59972, 59973, 59974, 59975')
    details_nav.confirm_and_close()
