from app.option_preferences.column_layout.column_names import *
from app.option_preferences.column_layout.sap_column import SapColumn


DEFAULT_COLUMN_LAYOUT = [
    SapColumn(ACTTYP, True, True),
    SapColumn(ACTIVITY_TYPE, True, False),
    SapColumn(PROJECT, False, False),
    SapColumn(REC_CCTR, True, True),
    SapColumn(RECEIVER_WBS, True, True),
    SapColumn(AATYPE, True, True),
    SapColumn(ATT_ABS_TYPE, True, False),
    SapColumn(PROJECT_DESCRIPTION, True, False),
    SapColumn(WBS_DESCRIPTION, True, False),
    SapColumn(MU, True, True),
    SapColumn(TOTAL, True, False),
    SapColumn(MONDAY, True, True),
    SapColumn(MONDAY_FROM, True, True),
    SapColumn(MONDAY_TO, True, True),
    SapColumn(TUESDAY, True, True),
    SapColumn(TUESDAY_FROM, True, True),
    SapColumn(TUESDAY_TO, True, True),
    SapColumn(WEDNESDAY, True, True),
    SapColumn(WEDNESDAY_FROM, True, True),
    SapColumn(WEDNESDAY_TO, True, True),
    SapColumn(THURSDAY, True, True),
    SapColumn(THURSDAY_FROM, True, True),
    SapColumn(THURSDAY_TO, True, True),
    SapColumn(FRIDAY, True, True),
    SapColumn(FRIDAY_FROM, True, True),
    SapColumn(FRIDAY_TO, True, True),
    SapColumn(SATURDAY, True, True),
    SapColumn(SATURDAY_FROM, True, True),
    SapColumn(SATURDAY_TO, True, True),
    SapColumn(SUNDAY, True, True),
    SapColumn(SUNDAY_FROM, True, True),
    SapColumn(SUNDAY_TO, True, True)
]