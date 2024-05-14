import ecandata
import ecanwrangle
from downloadWellData import get_and_download_well_info
from getObservationLink import get_obs_link
from ecandata import get_ecan_data
from downloadCsv import download_excel_workbook


"""Main script for the creation of water reports for ecan data"""

def create_water_reports():

    # Get the Ecan data from their api, this graps all the current wells/bores in use even the ones we don't care about
    all_ecan_data = ecandata.get_ecan_data()

    #Using the ecanwrangle file to filter out the rows (the wells/bores) that we don't need because people aren't drinking the water from these
    wrangled_ecan_data = ecanwrangle.clean_ecan(all_ecan_data)
    #Finally using the well search to take all of the wells/bores and write their latest information, this function just returns a dummy value of 1
    ids = wrangled_ecan_data['Well_No'].tolist()
    print(ids)
    get_and_download_well_info(ids)


create_water_reports()
