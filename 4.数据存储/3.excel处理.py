# Excel文件处理：
import random

import xlrd
import xlwt
from xlrd.sheet import Cell

'''Sheet相关的操作：'''
# workbook = xlrd.open_workbook("成绩表.xlsx")

# 获取所有的sheet名字
# print(workbook.sheet_names())

# 根据索引获取指定的sheet对象
# sheet = workbook.sheet_by_index(0)
# print(sheet.name)

# 根据名称获取指定的sheet对象
# sheet = workbook.sheet_by_name("2班")
# print(sheet.name)

# 获取所有的sheet对象
# sheets = workbook.sheets()
# for sheet in sheets:
#     print(sheet.name)

# 获取指定sheet的行数和列数
# sheet = workbook.sheet_by_index(0)
# print({"rows": sheet.nrows, "cols": sheet.ncols})

'''Cell相关的操作：'''

# 1.获取指定行和列的cell对象
# sheet = workbook.sheet_by_index(0)
# cell = sheet.cell(1, 1)
# print(cell.value)

# 2.获取指定行的某几列的cell对象
# cells = sheet.row_slice(1, 0, 4)
# for cell in cells:
# 	print(cell.value)

# 3.获取指定列的某几行的cell对象
# cells = sheet.col_slice(0, 1, sheet.nrows)
# for cell in cells:
# 	print(cell.value)

# 4.获取指定行和列的值
# cell_value = sheet.cell_value(0,1)
# print(cell_value)

# 5.获取指定行的某几列的值
# cell_values = sheet.row_values(1, 1, sheet.ncols)
# print(cell_values)

# 6.获取指定列的某几行的值
# cell_values = sheet.col_values(1,1,sheet.nrows)
# print(cell_values)

'''Cell中常用的数据类型：'''

# 1. 文本类型
# sheet = workbook.sheet_by_index(0)
# cell = sheet.cell(0, 0)
# print(cell.ctype)
# print(xlrd.XL_CELL_TEXT)

# 2. 数值类型
# cell = sheet.cell(1, 1)
# print(cell.ctype)
# print(xlrd.XL_CELL_NUMBER)

# 3. 日期时间类型
# cell = sheet.cell(19,0)
# print(cell.ctype)
# print(xlrd.XL_CELL_DATE)

# 4. 布尔类型
# cell = sheet.cell(19,0)
# print(cell.ctype)
# print(xlrd.XL_CELL_BOOLEAN)

# 5. 空白数据类型
# cell = sheet.cell(1, 1)
# print(cell.ctype)
# print(xlrd.XL_CELL_EMPTY)

'''

## 写入Excel文件：
1. 导入xlwt模块。
2. 创建一个Workbook对象。
3. 创建一个Sheet对象。
4. 使用sheet.write方法把数据写入到Sheet下指定行和列中。如果想要在原来workbook对象上添加新的cell，那么需要调用put_cell来添加。
5. 保存成Excel文件。

## 编辑Excel文件：
1. 先读取原来的Excel文件。
2. 然后在读取的sheet上面进行cell的修改，可以使用sheet.put_cell(row,col,ctype,value,None)方法实现。
3. 再重新创建一个新的excel文件，然后把之前读取到的数据写入到新的excel文件中。
'''

# 写入Excel文件
# workbook = xlwt.Workbook()
# sheet = workbook.add_sheet("sheet1")
# headers = ['姓名', '语文', '英语', '数学']
# for index, header in enumerate(headers):
# 	sheet.write(0, index, header)
#
# names = ['张三', '李四', '王五']
# for index, name in enumerate(names):
# 	sheet.write(index + 1, 0, name)
#
# for row in range(1, 4):
# 	for col in range(1, 4):
# 		sheet.write(row, col, random.randint(1, 100))
#
# workbook.save("成绩表1.xls")

# 编辑
rwb = xlrd.open_workbook('成绩表.xlsx')
rsheet = rwb.sheet_by_index(0)

# 求所有学生的科目总分
rsheet.put_cell(0, 4, xlrd.XL_CELL_TEXT, "总分", None)
nrows = rsheet.nrows
for row in range(1, nrows):
	grades = rsheet.row_values(row, 1, 4)
	print(grades)
	total = sum(grades)
	rsheet.put_cell(row, 4, xlrd.XL_CELL_NUMBER, total, None)

# 求每个科目的平均分
nrows = rsheet.nrows
ncols = rsheet.ncols
for col in range(1, 5):
	grades = rsheet.col_values(col, 1, nrows)
	print(grades)
	avg = sum(grades) / len(grades)
	rsheet.put_cell(nrows, col, xlrd.XL_CELL_NUMBER, round(avg, 2), None)

wwb = xlwt.Workbook()
wsheet = wwb.add_sheet("sheet1")
nrows = rsheet.nrows
nclos = rsheet.ncols
for row in range(0, nrows):
	for col in range(0, nclos):
		wsheet.write(row, col, rsheet.cell_value(row, col))
wwb.save('test.xls')
