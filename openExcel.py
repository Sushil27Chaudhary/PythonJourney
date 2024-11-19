from openpyxl import Workbook
import time

wb = Workbook()
sheet = wb.active

# sheet['A1'] = 87  
# sheet['A2'] = "Devansh"  
# sheet['A3'] = 41.80  
# sheet['A4'] = 10  

# now = time.strftime("%X")
# nows =  time.strftime("%x")

# sheet['A5'] = nows +" "+ now

# wb.save("sample_file.xlsx")


data = (
    (11,34,340),
    (11,44,344),
    (11,35,344),
    (11,36,354),
    (11,64,314),
    (11,74,124),
    ("Peter",'Andrew',45.62),
)

now = time.strftime("%X")

for i in data :
    sheet.append(i)

now = time.strftime("%X")
sheet['A8'] = "time "+" "+ now
wb.save("sample_file.xlsx")

