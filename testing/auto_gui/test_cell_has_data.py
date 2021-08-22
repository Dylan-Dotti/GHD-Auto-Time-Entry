
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from app.auto_gui.auto_entry_agent import AutoEntryAgent
    from app.auto_gui.keyboard_controller import KeyboardController

    main_wc = factory.get_sap_main_window_controller()
    main_wc.set_window_foreground()
    main_kc = KeyboardController(main_wc)
    agent = AutoEntryAgent(main_kc, None, [])
    print(agent._test_cell_has_data())
    