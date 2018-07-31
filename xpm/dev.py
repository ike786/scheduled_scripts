from methods_general import *  # custom methods
from methods_xpm_reports import *  # custom xpm reports methods
from bs4 import BeautifulSoup


capacitySoup = download_xpm_staff_capacity("E:\\TempPath\\")

tables = capacitySoup.findChildren('table')

rows = tables[0].findChildren(['th', 'tr'])

# for row in rows:
#     cells = row.findChildren('td')
#     for cell in cells:
#         value = cell.string
#         if value is not None:
#             print("The value in this cell is " + str(value))

for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.find(text=True)
        if text is not None:
            print(text)