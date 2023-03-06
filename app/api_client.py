import requests
from app.models import Station


class GbfsClient:
    gbfs_json_url: str = 'https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json'
    headers: dict = {'Client-Identifier': 'daniel-bymonitor'}

    def __init__(self):
        """ Validate gbfs_json_url, set up URLs we need and create a map for id to name conversion. """
        self._validate_input()
        self._station_information_url = self._get_feed("station_information")
        self._station_status_url = self._get_feed("station_status")
        self._id_to_name = self._create_id_to_name_map()

    def get_station_status_data(self) -> [Station]:
        """ Retrieves the data from the station_status url, includes the station name.
            Returns a list of Station objects """
        return [Station(**station, name=self._id_to_name[station['station_id']]) for station in
                requests.get(self._station_status_url, headers=self.headers).json()['data']['stations']]

    def _create_id_to_name_map(self) -> dict:
        """ Calls station_information_url and returns dictionary with id as key and name as value """
        return {station['station_id']: station['name'] for station in
                requests.get(self._station_information_url, headers=self.headers).json()['data']['stations']}

    def _validate_input(self) -> None:
        """ Verify that we are using a correct URL """
        if not requests.get(self.gbfs_json_url, headers=self.headers).status_code == 200:
            raise RuntimeError(f"Unable to connect to url: '{self.gbfs_json_url}'")

    def _get_feed(self, feed_name) -> str:
        """ Read the auto discovery file, and fetch the gbfs url. Return the url for the feed name provided """
        try:
            return [f for f in requests.get(self.gbfs_json_url, headers=self.headers).json()['data']['nb']['feeds'] if
                    f['name'] == feed_name][0]['url']
        except (KeyError, IndexError):
            raise RuntimeError(f"Unable to retrieve '{feed_name}' from gbfs url: '{self.gbfs_json_url}'")


if __name__ == '__main__':
    client = GbfsClient()
    client.get_station_status_data()
