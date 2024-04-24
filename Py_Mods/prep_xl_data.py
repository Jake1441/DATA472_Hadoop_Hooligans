import openpyxl

xl_file = openpyxl.load_workbook("Ideas\\household-living-costs-price-indexes-june-2020-quarter.xlsx")
print(xl_file)
dataframe1 = xl_file["1.01"]

i = 0
new_data = []
for row in dataframe1.iter_rows():
    if i == 8 or i > 10:
        for cell in row:
            row_values = [cell.value for cell in row if cell.value is not None]
        new_data.append(row_values)
    i += 1
