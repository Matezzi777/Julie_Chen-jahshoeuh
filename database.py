import discord
import sqlite3

#################### CONFESSIONALS ####################

def add_confessional(user: discord.Member, channel_id: str) -> None:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"INSERT INTO Confessionals VALUES ({user.id}, {channel_id})"
	cursor.execute(request)
	connexion.commit()
	connexion.close()

def remove_confessional(user: discord.Member) -> None:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"DELETE FROM Confessionals WHERE User_ID={user.id}"
	cursor.execute(request)
	connexion.commit()
	connexion.close()

def get_confessional(user: discord.Member) -> int:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"SELECT Channel_ID FROM Confessionals WHERE User_ID={user.id}"
	cursor.execute(request)
	connexion.commit()
	confessional_id: int = cursor.fetchone()[0]
	connexion.close()
	return (confessional_id)

#################### CONFIGURATION ####################

def set_embed_rgb(id: int, red: int, green: int, blue: int) -> bool:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"UPDATE Config SET Red={red} WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	request: str = f"UPDATE Config SET Green={green} WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	request: str = f"UPDATE Config SET Blue={blue} WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	connexion.close()

#################### ACCESS (READ) ####################

def is_user_in_database(user: discord.Member) -> bool:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"SELECT * FROM Confessionals WHERE User_ID={user.id}"
	cursor.execute(request)
	connexion.commit()
	result: int = cursor.fetchone()
	connexion.close()
	if (result):
		return (True)
	else:
		return (False)

def get_r(id: int) -> int:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"SELECT Red FROM Config WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	red: int = cursor.fetchone()[0]
	connexion.close()
	return (red)

def get_g(id: int) -> int:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"SELECT Green FROM Config WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	green: int = cursor.fetchone()[0]
	connexion.close()
	return (green)

def get_b(id: int) -> int:
	connexion = sqlite3.connect('sqlite.db')
	cursor = connexion.cursor()
	request: str = f"SELECT Blue FROM Config WHERE ID={id}"
	cursor.execute(request)
	connexion.commit()
	blue: int = cursor.fetchone()[0]
	connexion.close()
	return (blue)