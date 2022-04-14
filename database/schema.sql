-- The cars table stores all of the information on a car collected using the DLVA VES API
CREATE TABLE Cars
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT, -- License plate number
    recorded_datetime INT, -- Date and time plate was recorded UNIX TIME
    make TEXT, -- make of car
    manufacture_year INT, -- Year of manufacture UNIX TIME
    emissions REAL, -- Emissions g/km
    fuel_type TEXT, -- Car fuel type
    mot_date INT, -- Due date of MOT UNIX TIME
    car_location INT, -- Foreign Key of CarLocations record
    FOREIGN KEY (car_location) REFERENCES CarLocations(ID) 
);

-- The location table stores geographical locations of where the data was collected from
CREATE TABLE CarLocations
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    lat REAL, -- Location Latitude
    lon REAL, -- Location Longitude
    location_name TEXT, -- Name of location (street name)
    facing TEXT -- Direction camera is facing (N,E,S,W)
);

-- TEMP
-- Auto populate with some data

-- Location
INSERT INTO CarLocations (lat, lon, location_name, facing)
VALUES (50.2242, -1.2323, "A cool location", "N");


-- Cars
INSERT INTO Cars (plate, recorded_datetime, make, manufacture_year, emissions, fuel_type, mot_date, car_location)
VALUES ("Y18JDA", strftime("%s", "now"), "Ford", 2011, 103.2, "PETROL", 2022, 1);

INSERT INTO Cars (plate, recorded_datetime, make, manufacture_year, emissions, fuel_type, mot_date, car_location)
VALUES ("UDJ128", strftime("%s", "now"), "Vauxhall", 2015, 203.2, "DIESEL", 2022, 1);

INSERT INTO Cars (plate, recorded_datetime, make, manufacture_year, emissions, fuel_type, mot_date, car_location)
VALUES ("XYKLM2", strftime("%s", "now"), "Mini", 2011, 100.4, "PETROL", 2022, 1);