import ecandata
import ecanwrangle
import wellsearch

"""Just a scrap file to tie the pieces of the Ecan together. Can adapt this or just copy over to the proper main"""


# Get the Ecan data from their api, this graps all the current wells/bores in use even the ones we don't care about
all_ecan_data = ecandata.get_ecan_data()

#Using the ecanwrangle file to filter out the rows (the wells/bores) that we don't need because people aren't drinking the water from these
wrangled_ecan_data = ecanwrangle.clean_ecan(all_ecan_data)

#Finally using the well search to take all of the wells/bores and write their latest information, this function just returns a dummy value of 1
ids = wrangled_ecan_data['Well_No'].tolist()
wellsearch.get_and_download_well_info(ids)



