
if __name__ == '__main__':
    import pickle
    from app.data_formatter.zendesk_data_reader import ZendeskDataReader
    reader = ZendeskDataReader("testing/test_data/test_zd_data.xlsx")
    reader.load_wb()
    data = reader.read_all_rows()

    pickle.dump( data, open( "testing/test_data/zdesk_data.p", "wb" ) )
