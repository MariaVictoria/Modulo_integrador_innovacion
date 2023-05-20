
CREATE DATABASE Empresa;
USE Empresa;


CREATE TABLE Departamento (
  id_departamento INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL
);


CREATE TABLE Empleado (
  id_empleado INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  id_departamento INT,
  FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);


CREATE TABLE Proyecto (
  id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL
);


CREATE TABLE Asignacion (
  id_asignacion INT PRIMARY KEY AUTO_INCREMENT,
  id_empleado INT,
  id_proyecto INT,
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
  FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto)
);


INSERT INTO Departamento (nombre) VALUES ('Ventas');
INSERT INTO Departamento (nombre) VALUES ('Marketing');
INSERT INTO Departamento (nombre) VALUES ('Finanzas');


INSERT INTO Empleado (nombre, id_departamento) VALUES ('Juan Pérez', 1);
INSERT INTO Empleado (nombre, id_departamento) VALUES ('María López', 1);
INSERT INTO Empleado (nombre, id_departamento) VALUES ('Pedro Gómez', 2);
INSERT INTO Empleado (nombre, id_departamento) VALUES ('Ana Rodríguez', 2);
INSERT INTO Empleado (nombre, id_departamento) VALUES ('Luisa Torres', 3);



INSERT INTO Proyecto (nombre) VALUES ('Proyecto A');
INSERT INTO Proyecto (nombre) VALUES ('Proyecto B');
INSERT INTO Proyecto (nombre) VALUES ('Proyecto C');
INSERT INTO Proyecto (nombre) VALUES ('Proyecto D');
INSERT INTO Proyecto (nombre) VALUES ('Proyecto E');



INSERT INTO Asignacion (id_empleado, id_proyecto) VALUES (1, 1);
INSERT INTO Asignacion (id_empleado, id_proyecto) VALUES (2, 1);
INSERT INTO Asignacion (id_empleado, id_proyecto) VALUES (3, 2);
INSERT INTO Asignacion (id_empleado, id_proyecto) VALUES (4, 3);
INSERT INTO Asignacion (id_empleado, id_proyecto) VALUES (5, 4);




