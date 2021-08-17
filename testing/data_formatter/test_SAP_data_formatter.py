
from datetime import date


if __name__ == '__main__':
    import pickle
    from app.data_formatter.SAP_data_formatter import DataFormatter

    test_data = pickle.load( open( "testing/test_data/zdesk_data.p", "rb" ) )
    formatter = DataFormatter(test_data)

    formatter.merge_wbs_elements()

    # create pages for a provided month. 
    pages = formatter.create_pages(date.today().month)
    
    merge_rows = formatter.create_merge_rows()
    # for merge_row in formatter.merge_rows:
    #     print(merge_row.tickets)

    sap_rows = formatter.create_sap_rows(pages, merge_rows)

    with open('testing/test_data/test_output.txt', 'w+') as f:
        for page in sap_rows:
            f.write(f"{str(page.startDate)}\n")
            for row in page.data:
                f.write(f"{row.to_sap_str()}\n")
            f.write(f"{str(page.endDate)}\n")