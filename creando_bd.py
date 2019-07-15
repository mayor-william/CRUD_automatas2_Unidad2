
import sqlite3
try:
	bd = sqlite3.connect("base_de_datos.db")
	cursor = bd.cursor()
	tablas = [
		"""
			CREATE TABLE IF NOT EXISTS articulos(
				descripcion TEXT NOT NULL,
				precio TEXT NOT NULL
			);
		"""
	]
	for tabla in tablas:
		cursor.execute(tabla);
	print("Tablas creadas correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)