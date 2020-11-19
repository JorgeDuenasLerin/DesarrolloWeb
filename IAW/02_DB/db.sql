
USE gestionaplus;

DROP TABLE IF EXISTS Frutas;
CREATE TABLE Frutas (
  id MEDIUMINT NOT NULL AUTO_INCREMENT,
  nombre varchar(255),
  precio DECIMAL(10,2),
  PRIMARY KEY (id)
);

INSERT INTO Frutas (nombre, precio) VALUES ('Naranja', 1.99);
INSERT INTO Frutas (nombre, precio) VALUES ('Manzana', 2.19);
INSERT INTO Frutas (nombre, precio) VALUES ('Plátano', 2.00);
INSERT INTO Frutas (nombre, precio) VALUES ('Uva', 1.89);
INSERT INTO Frutas (nombre, precio) VALUES ('Melón', 1.75);
