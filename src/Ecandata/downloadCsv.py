import os
import requests
import time


def download_excel_workbook(IDs):
    """Takes the url of the direct csv download link (and the ID) and downloads the csv into a folder called well_data"""
    baseurl = """https://www.ecan.govt.nz/data/water-quality-data/exportallsample/"""
    directory = os.getcwd()

    if not os.path.basename(directory) == "well_data":
        os.makedirs("well_data", exist_ok=True)
        os.chdir("well_data")

    directory = os.path.join(directory, "well_data")
    for ID in IDs:
        try:
            print(f"Downloading content for code {ID}")
            n_ID = ID.replace("/", "_")
            url = baseurl + n_ID
            print(url)
            response = requests.get(url)
            file_path = os.path.join(directory, f"{n_ID}.csv")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"File was written at location {file_path}")
            time.sleep(1.7)
        except Exception as e:
            print(
                f"There was an error downloading the file for {ID} at address: {url}, with error {e}"
            )


# ids = ["BW24/0039", "K38/0088", "M35_6639", "L35_0558"]
# download_excel_workbook(ids)
