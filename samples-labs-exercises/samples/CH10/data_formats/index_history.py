from collections import OrderedDict
from typing import List, Dict, Iterator
import csv

IndexList = List[OrderedDict]

def csv_to_list(csvfile: str) -> IndexList:
    with open(csvfile, encoding = 'Big5') as f:
        fieldnames = ['日期', '開盤指數', '最高指數', '最低指數', '收盤指數']
        reader = csv.DictReader(f, fieldnames = fieldnames)
        return list(reader)[2:]

def row_with_fields(row: OrderedDict, fields: List) -> Dict:
    return {field : row[field] for field in fields}

def index_with_fields(indexlt: IndexList, fields: List) -> Iterator:
    return (row_with_fields(origin_row, fields) for origin_row in indexlt)

csvfile = input('CSV檔案名稱：')
fields = input('查詢欄位：').split(",")
indexlt = csv_to_list(csvfile)

for name in fields:
    print(name, end = '\t\t\t')
print()

for row in index_with_fields(indexlt, fields):
    for name in fields:
        print(row[name], end = '\t\t')
    print()
