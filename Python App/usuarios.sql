-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-05-2023 a las 13:41:06
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `usuarios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `Id` int(200) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `fecha` date NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `color` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`Id`, `nombre`, `fecha`, `direccion`, `color`) VALUES
(1, 'Karla Aguilar', '0000-00-00', 'Chimaltenango', 'Gris'),
(2, 'Gabriela Banegas', '0000-00-00', 'Chimaltenango', 'Negro'),
(3, 'David Argueta', '0000-00-00', 'Chimaltenago', 'verde'),
(4, 'Marvin Castillo', '0000-00-00', 'Patzicia', 'Azul'),
(5, 'Joel Mendez', '0000-00-00', 'Chimaltenango', 'Rojo'),
(6, 'Jose Garcia', '0000-00-00', 'San Martin', 'Amarillo'),
(7, 'Fredy', '0000-00-00', 'Zaragoza', 'Celeste'),
(8, 'Delmy Lopez', '0000-00-00', 'Chimaltenago', 'Rosado'),
(9, 'Otto Linares', '0000-00-00', 'Comalapa', 'Blanco'),
(10, 'Manuel Camey', '0000-00-00', 'Chimaltenango', 'Naranja');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestros`
--

CREATE TABLE `maestros` (
  `Id` int(200) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `curso` varchar(200) NOT NULL,
  `jornada` varchar(200) NOT NULL,
  `cursos` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `maestros`
--

INSERT INTO `maestros` (`Id`, `nombre`, `curso`, `jornada`, `cursos`) VALUES
(1, 'Moises Satz', 'Practica de taller', 'Ambas', 2),
(2, 'Erick Poz', 'Economia industrial', 'Matutina', 1),
(3, 'Jose Elel', 'Literatura y filosofia', 'Ambas', 2),
(4, 'Ingrid', 'Ingles', 'Matutina', 1),
(5, 'Glendy Perez', 'Psicobiologia y seminario', 'Ambas', 2),
(6, 'Rolman Solano', 'Quimica', 'Matutina', 1),
(7, 'Wilfredo Calan', 'Matemática', 'Matutina', 1),
(8, 'Marcos Saquil', 'Fisica fundamental', 'Matutina', 1),
(9, 'Floridalma Azurdia', 'Lab de quimica', 'ambas', 1),
(10, 'Raissa Lopez', 'Teologia', 'ambas', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `Id` int(200) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `usuario` varchar(200) NOT NULL,
  `correo` varchar(200) NOT NULL,
  `contra` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `Id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `maestros`
--
ALTER TABLE `maestros`
  MODIFY `Id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `registro`
--
ALTER TABLE `registro`
  MODIFY `Id` int(200) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
