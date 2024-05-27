import ecandata
import ecanwrangle
from getObservationLink import get_obs_link
from ecandata import get_ecan_data
from downloadCsv import download_excel_workbook
from pyvirtualdisplay import Display
import getObservationLink
import getCsvDownloadLink
import downloadCsv
import time
import random

"""Main script for the creation of water reports for ecan data"""
DELAY_LOWER, DELAY_UPPER = 2.0, 2.5
def create_water_reports() -> None:
    
    # Get the Ecan data from their api, this graps all the current wells/bores in use even the ones we don't care about
    all_ecan_data = ecandata.get_ecan_data()

    #Using the ecanwrangle file to filter out the rows (the wells/bores) that we don't need because people aren't drinking the water from these
    wrangled_ecan_data = ecanwrangle.clean_ecan(all_ecan_data)
    #Finally using the well search to take all of the wells/bores and write their latest information, this function just returns a dummy value of 1
    codes = wrangled_ecan_data['Well_No'].tolist() #codes are the well IDS
    print(f"Found {len(codes)} many codes")
    for code in codes:
        try:
            well_link, ID = getObservationLink.get_obs_link(code)
            csv_link, ID = getCsvDownloadLink.get_csv_download_link(well_link, ID)
            downloadCsv.download_excel_workbook(csv_link, ID)
            time.sleep(random.uniform(DELAY_LOWER,DELAY_UPPER)) # don't get banned that would be bad, also don't let them catch us 
        except Exception as e:
             print(f"There was an error: {e} when trying to download the code: {code}")
    


create_water_reports()
