#!/usr/bin/env python

# 관세청 수출입 무역통계
# https://unipass.customs.go.kr/ets/index.do

import pendulum
import subprocess

# 2000.1 ~ 2022.3
ti = pendulum.from_format("200001", "YYYYMM")
t_now = pendulum.now(tz='Asia/Seoul')

while ti < t_now:
    s = ti.format("YYYYMM")

    cmd = f'sed "s/999998/{s}/" <form-data-template.txt | sed "s/999999/{s}/" > form-data.txt'
    subprocess.run(cmd, shell=True)

    cmd = f'curl -X POST -d "@form-data.txt" https://unipass.customs.go.kr/ets/hmpg/retrieveCntyPrImexAcrsLst.do | jq > data/response-{s}.json'
    subprocess.run(cmd, shell=True)

    ti = ti.add(months=1)
