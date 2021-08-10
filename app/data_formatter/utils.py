from datetime import date, timedelta

'''
**** DON'T DELETE ****
this is the SAP test paste format, it works. don't change spaces here at all.

TEST	 	 	 	TEST	 	 	 		 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST

Zendesk Header:
"Updater name","Ticket Organization Name", "Support WBS Element", "Ticket Form", "Region", "Ticket ID", "Update - Timestamp", "Update - Date", "Ticket Handling Time"

SAP Header:
None, "ACCTYPE", None, "COST_CENTER", "WBS_ELEMENT", None, None, None, None, None, None, "MON", None, None, "TUES", None, None, "WED", None, None, "THURS", None, None, "FRI", None, None, "SAT", None, None, "SUN", None, None
'''

def verify_path(p: str) -> bool: 
    if p.exists() and p.is_file() and (str(p).endswith(".xlsm") or str(p).endswith(".xlsx")):
        return True
    return False

'''
  if first monday is not the first, go back a week to get first monday
  get corresponding sunday
'''
def date_ranges(month):
    year = date.today().year
    d = date(year, month, 7)
    offset = -d.weekday() #weekday = 0 means monday
    d = d + timedelta(offset)

    if d.day != 1:
        # if it isn't the first of the month, go 7 days back
        d = d - timedelta(days=7)
    
    while d.month == month or d.month + 1 == month:
        yield d, (d + timedelta(days=6))
        d += timedelta(days=7)