import argparse
import sys
import os
import logging
import requests
from datetime import datetime

AIRPARIF_KEY_ENV = 'ATI_AIRPARIF_KEY'
INSEE_ENV = 'ATI_INSEE'

RET_CODE_OK = 0
RET_CODE_ERROR = 2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', required=False, help='AirParif key')
    parser.add_argument('-i', '--insee', required=False, help='Insee code')
    args = parser.parse_args()

    key = getParamValue(args.key, AIRPARIF_KEY_ENV)
    insee = getParamValue(args.insee, INSEE_ENV)

    payload = {'key': key, 'villes' : insee }
    r = requests.post("http://www.airparif.asso.fr/services/api/1.1/idxville", data=payload)
    if r.status_code != 200:
        logging.error('Unexpected status code: {}'.format(r.status_code))
        return RET_CODE_ERROR

    data = r.json()
    now = datetime.now().replace(hour=12, minute=0, second=0)
    ts = int(datetime.timestamp(now))*(10**9)
    for curInsee in data:
        print('airparif,location={} indice={} {}'.format(
            curInsee['ninsee'],
            curInsee['jour']['indice'],
            ts))

    return RET_CODE_OK


def getParamValue(cliValue, envKey):
    if cliValue:
        return cliValue
    return os.getenv(envKey)


if __name__ == '__main__':
    sys.exit(main())
