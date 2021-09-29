from datetime import date, timedelta

# verify input path for excel parse
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