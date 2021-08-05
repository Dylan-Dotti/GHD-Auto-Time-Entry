from app.auto_gui.window_controller import WindowController


def get_sap_main_window_controller() -> WindowController:
    return WindowController('Time Sheet: Data Entry View')


def get_sap_details_window_controller() -> WindowController:
    return WindowController