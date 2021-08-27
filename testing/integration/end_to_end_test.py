
if __name__ == '__main__':
    import app.auto_gui.window_controller_factory as factory
    from datetime import date
    from app.auto_gui.keyboard_controller import KeyboardController
    from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator
    from app.auto_gui.auto_entry_agent import AutoEntryAgent
    from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader
    from app.data_formatter.formatters.data_formatter_factory import DataFormatterFactory

    # data formatting
    zendesk_reader = ZendeskDataReader('C:\\Users\\h4dottd\\Downloads\\Current_Month_08152021_1858.xlsx')
    zendesk_reader.load_wb()
    zendesk_rows = zendesk_reader.read_all_rows()

    # get a formatter
    formatter_factory = DataFormatterFactory()
    data_formatter = formatter_factory.get_formatter('ZENDESK')
    # create pages for a provided month
    pages = data_formatter.create_pages(date.today().month)
    # create a new formatter instance with the test data
    zdt_formatter = data_formatter(zendesk_rows, pages)
    # format zendesk data to SAP
    zdt_formatter.format()
    # get SAP pages
    formatted_data = zdt_formatter.formatted_data()
    data = formatted_data[1].data

    # auto entry
    main_wc = factory.get_sap_main_window_controller()
    main_kc = KeyboardController(main_wc)
    main_nav = SapMainWindowNavigator(main_kc)
    entry_agent = AutoEntryAgent(main_kc, main_nav, data)
    main_wc.set_window_foreground()
    entry_agent.execute(False)
