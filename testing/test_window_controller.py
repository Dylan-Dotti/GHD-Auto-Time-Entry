

if __name__ == '__main__':
    from app.auto_gui.sap_main_window_controller import SapMainWindowController

    wc = SapMainWindowController()
    wc.set_window_foreground()
    wc.wait_for_window_foreground()