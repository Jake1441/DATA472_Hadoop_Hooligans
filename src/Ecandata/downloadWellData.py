import downloadCsv
import getCsvDownloadLink
import getObservationLink
import time


SCRAP_DELAY = 2  #seconds

def get_and_download_well_info(codes):
    """Main function for this script, brings everyone together. Given a list-like of well codes, it will create a folder called well_data and download the most recent csv reports into that folder"""
    for code in codes:
        try:
            well_link, ID = getObservationLink.get_obs_link(code)
            csv_link, ID = getCsvDownloadLink.get_csv_download_link(well_link, ID)
            downloadCsv.download_excel_workbook(csv_link, ID)
            time.sleep(SCRAP_DELAY) # don't get banned that would be bad
        except Exception as e:
             print(f"There was an error: {e} when trying to download the code: {code}")
    return 1

# if __name__ == "__main__":
#     example_codes = ['I39/0007',
#     'H38/0004',
#     'J40/0217',
#     'N33/0212', 
#     'K37/0243',
#     'CB19/5076',
#     'K38/0066',
#     'K38/0066',
#     'BW24/0274'] # Some codes for testing if you want to
#     get_and_download_well_info(example_codes)