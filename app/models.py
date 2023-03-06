from pydantic import BaseModel, Field


class Station(BaseModel):
    """
    Represents response data that is returned by the REST API. FastAPI will generate a OpenAPI compliant JSON schema
    from this model. The alias in Field class allows us to create an instance with a different name for each of the
    attributes.
    """

    station_name: str = Field(alias='name', title='Station name', description='The name of the station')
    docks_available: int = Field(alias='num_docks_available', title='Docks available',
                                 description='The number of docks available at the station')
    bikes_available: int = Field(alias='num_bikes_available', title='Bikes available',
                                 description='The number of bikes available')


class GetStationsResponse(BaseModel):
    """ Response data returned by the REST API. """
    stations: list[Station]
