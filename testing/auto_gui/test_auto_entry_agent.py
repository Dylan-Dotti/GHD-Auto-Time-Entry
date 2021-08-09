
if __name__ == '__main__':
    from app.auto_gui.auto_entry_agent import AutoEntryAgent
    from app.data_formatter.sap_data_row import SapDataRow, DateEntry

    def generate_data_row(act, wbs, unit, date_entries):
        data_row = SapDataRow(act, wbs, unit, None, None)
        for entry in date_entries:
            data_row.add_time(entry)
        return data_row

    def get_test_michelin_row():
        act = '10000'
        wbs = 'S-005230.01.02.01'
        unit = 'M'
        date_entries = [
            DateEntry('180', '44841, 44842, 44843'),
            DateEntry('95', '44841, 44842, 44843'),
            DateEntry('42', '44841, 44842, 44843'),
            DateEntry('29', '44841, 44842, 44843'),
            DateEntry('7', '44841, 44842, 44843'),
            None,
            None
        ]
        return generate_data_row(act, wbs, unit, date_entries)

    def get_test_rainbird_row():
        act = '10000'
        wbs = 'S-005310.01.02.01'
        unit = 'M'
        date_entries = [
            DateEntry('180', '44841, 44842, 44843'),
            DateEntry('180', '44478, 44479, 44480'),
            None,
            None,
            None,
            DateEntry('180', '44841, 44842, 44843'),
            DateEntry('180', '44841, 44842, 44843')
        ]
        return generate_data_row(act, wbs, unit, date_entries)

    print(get_test_michelin_row())

    # Generate data rows
    data_rows = [
        get_test_michelin_row(),
        get_test_rainbird_row()
    ]
    # run
    # AutoEntryAgent(data_rows).execute()
