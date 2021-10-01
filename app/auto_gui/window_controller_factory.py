from app.auto_gui.window_controller import WindowController


def get_sap_main_window_controller() -> WindowController:
    return WindowController('Time Sheet: Data Entry View', 
                            alternate_names=['Time Sheet: Data Entry View SP1 (1)'],
                            find_window_timeout=10)


def get_sap_details_window_controller() -> WindowController:
    return WindowController('Cell Information')


def get_sap_confirmat_prot_window_controller() -> WindowController:
    return WindowController('Confirmat. Prompt')