DROP TABLE IF EXISTS weather;


CREATE TABLE IF NOT EXISTS weather (
    time TIMESTAMP NOT NULL,
    temperature_2m FLOAT NOT NULL , 
    latitude FLOAT NOT NULL , 
    longitude FLOAT NOT NULL , 
    city VARCHAR(100) NOT NULL,
    PRIMARY KEY (time , latitude , longitude)  
);