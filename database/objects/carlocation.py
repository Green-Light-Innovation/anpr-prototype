from database.engine import DatabaseEngine

class CarLocation:

    @staticmethod
    def load_from_database(ID:int) -> object:
        query = "SELECT * FROM CarLocations WHERE ID = ?;"

        DatabaseEngine.connect()
        data = DatabaseEngine.cursor.execute(query, (ID,)).fetchone()
        DatabaseEngine.disconnect()

        return CarLocation(*data)

    def __init__(self, ID:int, lat:float, lon:float, location_name:str, facing:str) -> object:
        self.__ID = ID
        self.__lat = lat
        self.__lon = lon
        self.__location_name = location_name
        self.__facing = facing

    # Getters
    def get_ID(self) -> int: return self.__ID
    def get_latitude(self) -> float: return self.__lat
    def get_longitude(self) -> float: return self.__lon
    def get_location_name(self) -> str: return self.__location_name
    def get_facing(self) -> str: return self.__facing

    def __repr__(self) -> str:
        return f"<CarLocation - Lat: {self.__lat} Lon: {self.__lon}>"