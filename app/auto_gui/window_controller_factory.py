from typing import List
from app.auto_gui.window_controller import WindowController


def get_sap_main_window_controller() -> WindowController:
    return get_window_controller(['Time Sheet: Data Entry View', 'Time Sheet: Data Entry View SP1 (1)'], 
                      find_window_timeout=10)


def get_sap_details_window_controller() -> WindowController:
    return get_window_controller(['Cell Information'])


def get_sap_confirmat_prot_window_controller() -> WindowController:
    return get_window_controller(['Confirmat. Prompt'])


def get_window_controller(window_names: List[str], find_window_timeout: float = None) -> WindowController:
    wc = WindowController()
    wc.bind_to_window(window_names, find_window_timeout=find_window_timeout)
    return wc