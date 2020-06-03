import xlsxwriter

rests = list()
owners = list()
layoffs = list()

filename = 'restaurants.txt'

with open (filename) as fin:
    numLines = 1
    for line in fin:
        if numLines%3 == 1:
            rests.append(line.strip())
        if numLines%3 == 2:
            owners.append(line.strip())
        if numLines%3 == 0:
            layoffs.append(line.strip())
        numLines += 1

workbook = xlsxwriter.Workbook('restaurant-data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1', rests)
worksheet.write_column('B1', owners)
worksheet.write_column('C1', layoffs)

workbook.close()

print(rests)
print(owners)
print(layoffs)
