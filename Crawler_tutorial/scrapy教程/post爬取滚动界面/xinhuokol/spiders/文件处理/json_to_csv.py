
import csv
import json

rows = []
for line in open('xinhuo.json', 'r',encoding='utf8'):
    rows.append(json.loads(line))

f = open('sample.csv', 'w',encoding='utf8')
csv_write = csv.writer(f)

# writerow: 按行写入，　writerows: 是批量写入
# 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
csv_write.writerow(rows[0].keys())

for row in rows:
    csv_write.writerow(row.values())
f.close()