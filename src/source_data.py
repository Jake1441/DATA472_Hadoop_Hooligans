from Ecandata import ecanmain
from Lawadata import lawa_main

def source_data():
    """Main file for downloading the external data, Lawa data returns as a Dictionary of DF objects,
    Ecan Data is downloaded in the folder well_data"""
    print("Starting data sourcing")
    lawa_main.get_lawa_groundwater()
    ecanmain.create_water_reports()
    print("Finished data sourcing")
    


print(source_data())