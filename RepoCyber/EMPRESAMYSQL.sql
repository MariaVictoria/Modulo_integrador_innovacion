CREATE DATABASE BigBread;
USE BigBread;


-- Crear tabla de productos
CREATE TABLE Productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2) NOT NULL
);

-- Crear tabla de ingredientes
CREATE TABLE Ingredientes (
  id_ingrediente INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);

-- Crear tabla de producción
CREATE TABLE Produccion (
  id_produccion INT PRIMARY KEY AUTO_INCREMENT,
  id_producto INT,
  fecha DATE NOT NULL,
  cantidad INT NOT NULL,
  FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

-- Crear tabla de ingredientes utilizados en la producción
CREATE TABLE Ingredientes_Produccion (
  id_produccion INT,
  id_ingrediente INT,
  cantidad DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (id_produccion) REFERENCES Produccion(id_produccion),
  FOREIGN KEY (id_ingrediente) REFERENCES Ingredientes(id_ingrediente)
);



