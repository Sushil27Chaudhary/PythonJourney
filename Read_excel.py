import openpyxl

wb = openpyxl.load_workbook('sample_file.xlsx')

sheet = wb.active

# x1 = sheet['A1']
# x2 = sheet['A2']

# #using cell() function  
# x3 = sheet.cell(row=3, column=1)  
# print("The first cell value:",x1.value)  
# print("The second cell value:",x2.value)  
# print("The third cell value:",x3.value)  


cells = sheet['A1','B5']  

for i1, i2 in cells:
    print("{0:5}{1:5}".format(i1.value,i2.value))
