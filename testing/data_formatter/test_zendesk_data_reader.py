
if __name__ == '__main__':
    import pickle
    from app.data_formatter.zendesk_data_reader import ZendeskDataReader
    reader = ZendeskDataReader("testing/test_data/test_zd_data.xlsx")

    # load worksheet, should exit with error if error. 
    reader.load_wb()

    # generate zendesk rows for read zendesk data
    data = reader.read_all_rows()

    # save data for formatter use
    pickle.dump( data, open( "testing/test_data/zdesk_data.p", "wb" ) )
