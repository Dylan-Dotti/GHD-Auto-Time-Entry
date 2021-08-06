# DON'T DELETE 
'''
this is the SAP test paste format, it works. don't change spaces here at all
TEST	 	 	 	TEST	 	 	 		 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST
'''

zendesk_header = ["Updater name","Ticket Organization Name", "Support WBS Element", "Ticket Form", "Region", "Ticket ID", "Update - Timestamp", "Update - Date", "Ticket Handling Time"]

# keep in mind a whole row in SAP is a week, a column is a wbs element
sap_header = [None, "ACCTYPE", None, "COST_CENTER", "WBS_ELEMENT", None, None, None, None, None, None, "MON", None, None, "TUES", None, None, "WED", None, None, "THURS", None, None, "FRI", None, None, "SAT", None, None, "SUN", None, None]

def verify_path(p: str) -> bool: 
    if p.exists() and p.is_file() and (str(p).endswith(".xlsm") or str(p).endswith(".xlsx")):
        return True
    return False