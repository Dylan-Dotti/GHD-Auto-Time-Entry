import unittest
from app.data_formatter.readers.Data_Row import DataRow
from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader

class TestZendeskReader(unittest.TestCase):

    def test_success_creates_reader_instance(self):
        reader = ZendeskDataReader("testing/test_data/zd_data/good_zd_data.xlsx")
        self.assertIsInstance(reader, ZendeskDataReader)
        self.assertIsNone(reader.data)
        self.assertIsNone(reader.header)
        self.assertIsNone(reader.month)
        self.assertIsNone(reader.users)

    def test_fails_create_reader_instance(self):
        with self.assertRaises(AssertionError) as context:
            reader = ZendeskDataReader("bad_path")
        self.assertTrue("Input is not a file or an excel spreadsheet." in str(context.exception))

    def test_success_reader_loads_wb(self):
        reader = ZendeskDataReader("testing/test_data/zd_data/good_zd_data.xlsx")
        reader.load_wb()
        self.assertIsNotNone(reader.data)
        self.assertIsNotNone(reader.header)
        self.assertIsNotNone(reader.month)
        self.assertIsNotNone(reader.users)

    def test_fails_reader_loads_wb(self):
        with self.assertRaises(RuntimeError) as context:
            reader = ZendeskDataReader("testing/test_data/zd_data/bad_excel.xlsx")
            reader.load_wb()
        self.assertTrue("Failed to parse excel with error:" in str(context.exception))   

    def test_success_creates_rows(self):
        reader = ZendeskDataReader("testing/test_data/zd_data/good_zd_data.xlsx")
        reader.load_wb()
        data = reader.read_all_rows()
        self.assertIsInstance(data[0], DataRow)

    # we're missing a required column 
    def test_fails_creates_rows(self):
        with self.assertRaises(RuntimeError) as context:
            reader = ZendeskDataReader("testing/test_data/zd_data/malformed_zd_data.xlsx")
            reader.load_wb()
            data = reader.read_all_rows()
        self.assertTrue("One of the required header fields is not present in the input spreadsheet." in str(context.exception)) 

if __name__ == '__main__':
    unittest.main()
