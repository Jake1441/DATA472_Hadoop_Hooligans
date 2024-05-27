import download_workbook
import get_groundwater_link
from pyvirtualdisplay import Display

def get_lawa_groundwater() -> dict:
    with Display(visable=False, size=(1280, 800)):
        download_link = get_groundwater_link.lawa_download_link_groundwater()
        data_dict = download_workbook.download_excel_workbook(download_link)

        return data_dict


if __name__ == "__main__":
    data = get_groundwater_link()  #Example of how to access the dfs
    for _, df in data.items():
        print(df)