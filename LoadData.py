# import xlrd
# import csv
# import Preprocessing as pre
#
#
# def preprocessing(sentence):
#     sentence = pre.caseFolding(sentence)
#     token = pre.tokenization(sentence)
#     token = pre.stopwordRemoval(token)
#     token = pre.lemmatization(token)
#     return token
#
#
# workbook = xlrd.open_workbook('Dataset.xlsx')
# worksheet = workbook.sheet_by_index(0)
#
# data = []
# label = []
# for i in range(1, worksheet.nrows):
#     if worksheet.cell(i, 4).value != 0:
#         data.append(worksheet.cell(i, 3).value)
#         label.append(int(float(worksheet.cell(i, 4).value)))
#
# temp = []
# bag = []
# for i in range(len(data)):
#     data[i] = preprocessing(data[i])
#     temp.append(data[i])
#
# for i in range(len(temp)):
#     for j in range(len(temp[i])):
#         bag.append(temp[i][j])
#
# bag = list(set(bag))
#
# term = []
# term.append(bag)
# for i in range(len(data)):
#     temp = []
#     for j in range(len(bag)):
#         if bag[j] in data[i]:
#             temp.append(1)
#         else:
#             temp.append(0)
#     temp.append(label[i])
#     term.append(temp)
#
# with open("Data.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(term)

# import csv
#
#
# with open('Data.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     data = []
#     for row in reader:
#         data.append(row)
#
# # print(data[1][len(data[0])-1])
# print(len(data[0]))
# print(len(data[1]))
