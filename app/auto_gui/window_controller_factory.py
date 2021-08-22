from app.auto_gui.window_controller import WindowController


def get_sap_main_window_controller() -> WindowController:
    try:
        return WindowController('Time Sheet: Data Entry View SP1 (1)')
    except:
        return WindowController('Time Sheet: Data Entry View')


def get_sap_details_window_controller() -> WindowController:
    return WindowController('Cell Information')


def get_sap_confirmat_prot_window_controller() -> WindowController:
    return WindowController('Confirmat. Prompt')