"""Main script for Sourcing the Ecan Data, Run as a module"""
from .ecanwrangle import clean_ecan
from .ecandata import get_ecan_data
from .downloadCsv import download_excel_workbook
from .getCsvDownloadLink import get_csv_download_link
import time

SCRAP_DELAY = 2



def create_water_reports() -> None:
    """Query Ecan API and build up a dataframe of Wells, then create a list of well links and ids and iteratively 
        Scrap the data on each well from the Ecan website. Creates a folder of csvs one for each well"""
    all_ecan_data = get_ecan_data()
    
    wrangled_ecan_data = clean_ecan(all_ecan_data)
    codes = wrangled_ecan_data['Well_No'].tolist() 
    links = wrangled_ecan_data['Link'].tolist()
    #print(codes)
    #print(links)
    for link,code in zip(links, codes):
        try:
            csv_link = get_csv_download_link(link) 
            download_excel_workbook(csv_link, code)
            time.sleep(SCRAP_DELAY)
        except Exception as e:
             print(f"There was an error: {e} when trying to download the code: {code}")
    


#create_water_reports()
