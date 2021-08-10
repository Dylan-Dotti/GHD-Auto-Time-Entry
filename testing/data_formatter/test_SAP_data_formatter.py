
if __name__ == '__main__':
    import pickle
    from app.data_formatter.SAP_data_formatter import DataFormatter

    test_data = pickle.load( open( "testing/test_data/zdesk_data.p", "rb" ) )
    formatter = DataFormatter(test_data)

    formatter.merge_wbs_elements()
    # print(formatter.collector_container)

    formatter.create_merge_rows()
    # for merge_row in formatter.merge_rows:
    #     print(merge_row.tickets)

    sap_rows = formatter.create_sap_rows()
    for page in sap_rows:
        for row in page.data:
            print(row.to_sap_str())