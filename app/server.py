from fastapi import FastAPI
from app.models import GetStationsResponse
from app.api_client import GbfsClient

app = FastAPI()
client = GbfsClient()


@app.get("/get_stations", response_model=GetStationsResponse)
async def get_stations():
    return GetStationsResponse(stations=client.get_station_status_data())


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """ Added as a quick fix to ignore any requests for /favicon.ico """
    return None


if __name__ == '__main__':
    test = client.get_station_status_data()
