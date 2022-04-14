from database.engine import DatabaseEngine
from database.objects.carlocation import CarLocation

class Car:

    @staticmethod
    def load_from_database(plate:str) -> object:
        query = "SELECT * FROM Cars WHERE plate = ?"
        
        DatabaseEngine.connect()
        data = DatabaseEngine.cursor.execute(query, (plate,)).fetchone()
        DatabaseEngine.disconnect()

        if not data: return # Return None if no car is found
        
        return Car(*data)

    @staticmethod
    def load_all() -> list:pass # TODO Implement this

    def __init__(self, ID:int, plate:str, recorded_datetime:int, make:str, manufacture_year:int, emissions:float, fuel_type:str, mot_date:int, car_location:int) -> object:
        self.__ID = ID
        self.__plate = plate
        self.__recorded_datetime = recorded_datetime
        self.__make = make
        self.__manufacture_year = manufacture_year
        self.__emissions = emissions
        self.__fuel_type = fuel_type
        self.__mot_date = mot_date
        self.__car_location = CarLocation.load_from_database(car_location) # TODO CHANGE TO CAR LOCATION OBJECT

    # Getters
    def get_ID(self) -> int: return self.__ID
    def get_plate(self) -> str: return self.__plate
    def get_recorded_datetime(self) -> int: return self.__recorded_datetime
    def get_make(self) -> str: return self.__make
    def get_manufacture_year(self) -> int: return self.__manufacture_year
    def get_emissions(self) -> float: return self.__emissions
    def get_fuel_type(self) -> str: return self.__fuel_type
    def get_mot_date(self) -> str: return self.__mot_date
    def get_car_location(self) -> CarLocation: return self.__car_location
    # TODO ADD GETTER FOR CARLOCATION

    def __repr__(self) -> str:
        return f"<Car - {self.__plate}>"

    

