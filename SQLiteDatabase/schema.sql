DROP table if EXISTS cyberassets CASCADE;
DROP table if EXISTS serialnumbers CASCADE;


CREATE TABLE cyberassets (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(256)
    type VARCHAR(256)
    os VARCHAR(30
);

CREATE TABLE serialnumber (
    id SERIAL PRIMARY KEY NOT NULL,
    cyberassets_id INT NOT NULL REFERENCES cyberassets(id),
    number INT
);


INSERT INTO cyberassets(name, type, os)	
        VALUES ('Bill PC', 'PC' 'Windows');
INSERT INTO cyberassets(name, type, os)	
        VALUES ('Sally Server', 'Server' 'Linux');
INSERT INTO cyberassets(name, type, os)		
        VALUES ('Bill PC', 'Networking Equipment' 'Linux');
INSERT INTO cyberassets(name, type, os)	
        VALUES ('Lang PC', 'PC' 'Apple');
		
INSERT INTO serialnumber(number, cyberassets_id)	
        VALUES (15528375, 1);
INSERT INTO serialnumber(name, cyberassets_id)	
        VALUES (666772727, 2);
INSERT INTO serialnumber(name, cyberassets_id)	
        VALUES (5522727, 3);
INSERT INTO department(name, cyberassets_id)	
        VALUES (88484848, 4);

