if __name__ == '__main__':
    import pickle
    from app.data_formatter.formatters.data_formatter_factory import DataFormatterFactory
    from datetime import date

    # generated from test_zendesk_data_reader
    test_data = pickle.load(open("testing/test_data/zdesk_data.p", "rb"))

    # get a formatter factory
    formatter_factory = DataFormatterFactory()

    # get a class of the sap formatter
    data_formatter = formatter_factory.get_formatter('ZENDESK')

    # create pages for a provided month, class method
    pages = data_formatter.create_pages(date.today().month)

    # create a new formatter instance with the test data
    zdt_formatter = data_formatter("Logan Enright", test_data, pages)
    
    # format zendesk data to SAP
    zdt_formatter.format()

    # get formatted data
    formatted_data = zdt_formatter.formatted_data()

    # save data to validate
    with open('testing/test_data/test_output.txt', 'w+') as f:
        for page in formatted_data:
            f.write(f"{str(page.startDate)}\n")
            for row in page.data:
                f.write(f"{row.to_sap_str()}\n")
            f.write(f"{str(page.endDate)}\n")