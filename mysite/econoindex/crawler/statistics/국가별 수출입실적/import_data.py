#!/usr/bin/env python

import json
import os
import re
import sqlite3
import argparse
import pendulum


def to_number(s):
    return int(re.sub('[, ]', '', s))


def to_timestamp(d):
    return int(pendulum.from_format(d, 'YYYY.MM', tz='Asia/Seoul').in_tz('UTC').int_timestamp)


def find_duplicate(cur, timestamp, import_count, export_count):
    r = cur.execute('select * from econoindex_importexport where timestamp=? and imp_count=? and exp_count=?',
                    (timestamp, import_count, export_count))
    row = r.fetchone()
    if row:
        return row[0]

    return 0


def preprocess_value(item):
    try:
        item['priodTitle'] = to_timestamp(item['priodTitle'])
    except (TypeError, ValueError):
        pass

    item["cntyNm"].strip()
    item["impCnt"] = to_number(item["impCnt"])
    item["impUsdAmt"] = to_number(item["impUsdAmt"])
    item["expCnt"] = to_number(item["expCnt"])
    item["expUsdAmt"] = to_number(item["expUsdAmt"])
    item["cmtrBlncAmt"] = to_number(item["cmtrBlncAmt"])
    return item


def import_data(database_path, data_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    #path = 'data/fixture'
    files = os.listdir(data_path)
    item_count = 0
    for f in files:
        fp = os.path.join(data_path, f)
        if os.path.isdir(fp):
            continue

        with open(fp) as fd:
            data = json.load(fd)

        for item in data['items']:
            #       "cntyNm": "미국",
            #       "priodTitle": "2000.01",
            #       "expCnt": "              45,538",
            #       "expUsdAmt": "           2,609,788",
            #       "impCnt": "              52,999",
            #       "impUsdAmt": "           2,217,025",
            #       "cmtrBlncAmt": "             392,763",
            # print(item['cntyNm'])
            newitem = preprocess_value(item)
            if newitem['priodTitle'] == '총계':
                continue

            pk = find_duplicate(cur, newitem['priodTitle'], newitem["impCnt"], newitem["expCnt"])
            if pk > 0:
                print(f'Record exists with pk={pk}')
                continue

            cur.execute(
                'INSERT INTO econoindex_importexport(timestamp, country, note, exp_amount, exp_count, imp_amount, imp_count, balance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (
                    newitem['priodTitle'],
                    newitem["cntyNm"],
                    None,
                    newitem["expUsdAmt"],
                    newitem["expCnt"],
                    newitem["impUsdAmt"],
                    newitem["impCnt"],
                    newitem["cmtrBlncAmt"],
                )
                )
            item_count += 1

    if item_count > 0:
        con.commit()

    con.close()

    return item_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='국가별 수출입실적 데이터 수집/저장')
    parser.add_argument('--database-path', type=str, help='File path of sqlite database ', required=True)
    parser.add_argument('--data-path', type=str, help='Directory path holding json files', required=True)
    args = parser.parse_args()

    item_count = import_data(args.database_path, args.data_path)

    print(f'Inserted {item_count} records')
