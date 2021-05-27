# -*- coding: UTF-8 -*-
import csv
import numpy as np
import os
from datetime import datetime, timedelta

def time_convert(timestamp):
    year = '20' + timestamp.split(' ')[0].split('/')[2]
    month = timestamp.split(' ')[0].split('/')[0]
    day = timestamp.split(' ')[0].split('/')[1]
    today = year + '/' + month + '/' + day + ' ' + timestamp.split(' ')[1]
    return datetime.strptime(today, "%Y/%m/%d %H:%M:%S")


def revise_data(data):
    row = data.copy()
    for i in range(1, len(row)):
        if row[i] != '' and row[i] != '無資料' and row[i] != '設備維護中':
            row[i] = round(float(row[i]), 2)
    return row


def transform_data(data):
    for i in range(len(data)):
        if i != 0:
            data[i] = revise_data(data[i])
            data[i][0] = time_convert(data[i][0])
    return data


def export(file, data):
    new_list = data.copy()
    with open('export/{file}'.format(file=file), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in new_list:
            writer.writerow(row)


if __name__ == '__main__':
    if not os.path.isdir('data'):
        raise ('原始資料data資料夾不存在')
    if not os.path.isdir('export'):
        os.mkdir('export')
    for root, dirs, files in os.walk('data'):
        for file in files:
            data = list()
            with open('data/{file}'.format(file=file), newline='', encoding='utf-8') as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                print(rows)
                for row in rows:
                    data.append(row)
            data = transform_data(data)
            export(file, data)
            print('finish:', file)
