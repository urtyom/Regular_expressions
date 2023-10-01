import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

list_surename = []
for row in contacts_list[1:]:

  pattern_1 = r"(\+7)(495)(\d+)"
  find_n_1 = re.findall(pattern_1, row[5])
  if find_n_1!=None:
    for tes in find_n_1:
      l_f_1 = list(tes)
      row[5] = (f'{l_f_1[0]}({l_f_1[1]})'
      f'{l_f_1[2][0:3]}-{l_f_1[2][3:5]}-{l_f_1[2][5:]}')

  pattern_2 = r"(\+7|8)\s*\(*(\d+)[\s)|-]*(\d+)[\s-](\d{4})"
  find_n_2 = re.findall(pattern_2, row[5])
  if find_n_2!=None:
    for tes in find_n_2:
      l_f_2 = list(tes)
      row[5] = f'+7({l_f_2[1]}){l_f_2[2]}-{l_f_2[3][0:2]}-{l_f_2[3][2:]}'

  pattern_3 = (r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]+(\d+)[\s-]+(\d+)"
  "|((\s+[\s(])|\s)доб\. (\d{4})([\s)]*)")
  find_n_3 = re.findall(pattern_3, row[5])
  if len(find_n_3) > 1:
    f_n_1 = find_n_3[0]
    f_n_2 = find_n_3[1]
    row[5] = f'+7({f_n_1[1]}){f_n_1[2]}-{f_n_1[3]}-{f_n_1[4]} доб.{f_n_2[-2]}'
  else:
    for tes in find_n_3:
      l_f_4 = list(tes)
      row[5] = f'+7({l_f_4[1]}){l_f_4[2]}-{l_f_4[3]}-{l_f_4[4]}'

  full_name = row[0]+row[1]+row[2]
  full_name_1 = full_name.replace(' ', '')
  name_split = ''.join(full_name_1)
  res_list = re.findall('[А-Я][^А-Я]*', name_split)

  if len(res_list) > 2:
    row[0] = res_list[0]
    row[1] = res_list[1]
    row[2] = res_list[2]
  else:
    row[0] = res_list[0]
    row[1] = res_list[1]

  list_surename.append(row[0])
  for row_2 in contacts_list[1:]:
    if row[0] == row_2[0]:
  #     if row[0] == None:
  #       row[0] = row_2[0]
  #     if row[1] == None:
  #       row[1] = row_2[1]
      if row[2] == '':
        row[2] = row_2[2]
      if row[3] == '':
        row[3] = row_2[3]
      if row[4] == '':
        row[4] = row_2[4]
      if row[5] == '':
        row[5] = row_2[5]
      if row[6] == '':
        row[6] = row_2[6]

con_dict = {}
con_list = []

for i in contacts_list:
  con_dict[i[0]] = [i[1], i[2], i[3], i[4], i[5], i[6]]

for x, y in con_dict.items():
  y.insert(0, x)
  con_list.append(y)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(con_list)
