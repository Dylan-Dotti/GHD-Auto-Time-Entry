

if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory

    wc = factory.get_sap_main_window_controller()
    wc.set_window_foreground()
    wc.wait_for_window_foreground()