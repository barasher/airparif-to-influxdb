#! /bin/bash

rm -rf work/*

key=${ATI_AIRPARIF_KEY?"No Airparif key specified"}
insee=${ATI_INSEE?"No INSEE code specified"}
iurl=${ATI_IDB_URL?"No InfluxDB URL specified"}
idb=${ATI_IDB_DB?"No database specified"}

python3 crawler.py > work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi

./pusher -t 30s -u $iurl -d $idb -f work/data.txt
status=$?
if [ $status -ne 0 ]; then
    exit 1
fi
