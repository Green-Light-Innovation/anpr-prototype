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

    def __init__(self, ID:str, plate:str, recorded_datetime:int, make:str, manufacture_year:int, emissions:float, fuel_type:str, mot_date:int, car_location:str) -> object:
        self.__ID = ID
        if not ID: self.__ID = DatabaseEngine.gen_id() # If no ID is specified, gen a new one

        self.__plate = plate
        self.__recorded_datetime = recorded_datetime
        self.__make = make
        self.__manufacture_year = manufacture_year
        self.__emissions = emissions
        self.__fuel_type = fuel_type
        self.__mot_date = mot_date
        self.__car_location = CarLocation.load_from_database(car_location) # TODO CHANGE TO CAR LOCATION OBJECT

    # Getters
    def get_ID(self) -> str: return self.__ID
    def get_plate(self) -> str: return self.__plate
    def get_recorded_datetime(self) -> int: return self.__recorded_datetime
    def get_make(self) -> str: return self.__make
    def get_manufacture_year(self) -> int: return self.__manufacture_year
    def get_emissions(self) -> float: return self.__emissions
    def get_fuel_type(self) -> str: return self.__fuel_type
    def get_mot_date(self) -> str: return self.__mot_date
    def get_car_location(self) -> CarLocation: return self.__car_location
    
    def save_to_database(self) -> None:
        """ Save the object's data to the database """

        # SQL query to insert new record into Cars table
        query = """
        INSERT INTO Cars (ID, plate, recorded_datetime, make, manufacture_year, emissions, fuel_type, mot_date, car_location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        DatabaseEngine.connect() # Connect to the database
        
        # Execute the SQL query with given parameters
        DatabaseEngine.cursor.execute(query, (
            self.__ID,
            self.__plate,
            self.__recorded_datetime,
            self.__make,
            self.__manufacture_year,
            self.__emissions,
            self.__fuel_type,
            self.__mot_date,
            self.__car_location.get_ID()
        ))

        DatabaseEngine.commit() # Commit changes made to the table
        DatabaseEngine.disconnect() # Disconnect from the database

    def __repr__(self) -> str:
        return f"<Car - {self.__plate}>"

    

