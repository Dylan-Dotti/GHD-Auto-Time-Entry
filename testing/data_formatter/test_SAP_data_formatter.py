
from datetime import date


if __name__ == '__main__':
    import pickle
    from app.data_formatter.SAP_data_formatter import SAPDataFormatter

    # generated from test_zendesk_data_reader
    test_data = pickle.load(open("testing/test_data/zdesk_data.p", "rb"))

    # create pages for a provided month
    pages = SAPDataFormatter.create_pages(date.today().month)

    # create a new formatter instance with the test data
    formatter = SAPDataFormatter(test_data)
    

    merge_rows = formatter.create_merge_rows()

    # fill the pages with the merge rows
    complete_sap_pages = formatter.merge_to_sap(pages, merge_rows)

    # save data to validate
    with open('testing/test_data/test_output.txt', 'w+') as f:
        for page in complete_sap_pages:
            f.write(f"{str(page.startDate)}\n")
            for row in page.data:
                f.write(f"{row.to_sap_str()}\n")
            f.write(f"{str(page.endDate)}\n")