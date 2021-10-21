from datetime import date, timedelta

# verify path is valid
def verify_path(p: str) -> bool: 
    if p.exists() and p.is_file():
        return True
    return False

# verify input path is valid and excel
def verify_path_excel(p: str) -> bool:
    if verify_path(p) and (str(p).endswith(".xlsm") or str(p).endswith(".xlsx")):
        return True
    return False

'''
  If first monday is not the first of the month, go back a week.
  We have to do this because SAP begins a page on a monday, not the beginning of the month.
  
  returns generator of (data of Monday, date of following Sunday)
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