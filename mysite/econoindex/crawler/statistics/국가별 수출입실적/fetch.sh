#!/bin/bash

sed "s/999998/$1/" <form-data-template.txt | sed "s/999999/$2/" > form-data.txt

# form-data 는 devtools 에서 payload 탭 -> view source
curl -X POST -d "@form-data.txt" https://unipass.customs.go.kr/ets/hmpg/retrieveCntyPrImexAcrsLst.do | jq > "response-$1-$2.json"

