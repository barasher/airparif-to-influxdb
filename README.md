# Airparif to InfluxDB (airparif-to-influxdb)

**Airparif to InfluxDB** is a Docker image that stores an [Airparif](https://www.airparif.asso.fr/) polution status to [InfluxDB](https://docs.influxdata.com/influxdb/).

## Image building
 
```
docker build -t barasher/airparif-to-influxdb:latest .
```

## Execution

key=${ATI_AIRPARIF_KEY?"No Airparif key specified"}
insee=${ATI_INSEE?"No INSEE code specified"}
iurl=${ATI_IDB_URL?"No InfluxDB URL specified"}
idb=${ATI_IDB_DB?"No database specified"}

Environment variables :
- **ATI_AIRPARIF_KEY**: Airparis API key, required
- **ATI_INSEE**: INSEE town code (**not the postal code**), required
- **ATI_IDB_URL**: InfluxDB URL, required (ex : http://192.168.0.2:8086)
- **ATI_IDB_DB**: InfluxDB database, required

INSEE code ode retrieved [here](https://www.insee.fr/fr/information/4316069).

```
docker run --rm
  --env ATI_AIRPARIF_KEY=[Airparis API key]
  --env ATI_INSEE=[INSEE town code]
  --env OTI_IDB_URL=[InfluxDB URL]
  --env OTI_IDB_DB=[InfluxDB database]
  barasher/airparif-to-influxdb:latest
```
