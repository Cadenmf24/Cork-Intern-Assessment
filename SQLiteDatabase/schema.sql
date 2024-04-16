DROP table if EXISTS cyberassets;
DROP table if EXISTS serialnumbers;


CREATE TABLE cyberassets (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(256),
    type VARCHAR(256),
    os VARCHAR(30)
);

CREATE TABLE serialnumbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cyberassets_id INTEGER REFERENCES cyberassets(id),
    serialNumber INTEGER
);


INSERT INTO cyberassets(name, type, os)	
        VALUES ('Bill PC', 'PC', 'Windows');
INSERT INTO cyberassets(name, type, os)	
        VALUES ('Sally Server', 'Server', 'Linux');
INSERT INTO cyberassets(name, type, os)		
        VALUES ('Bill PC', 'Networking Equipment', 'Linux');
INSERT INTO cyberassets(name, type, os)	
        VALUES ('Lang PC', 'PC', 'Apple');
		
INSERT INTO serialnumbers(serialNumber, cyberassets_id)	
        VALUES (15528375, 1);
INSERT INTO serialnumbers(serialNumber, cyberassets_id)	
        VALUES (666772727, 2);
INSERT INTO serialnumbers(serialNumber, cyberassets_id)	
        VALUES (5522727, 3);
INSERT INTO serialnumbers(serialNumber, cyberassets_id)	
        VALUES (88484848, 4);

