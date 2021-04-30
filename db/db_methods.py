import pymysql


class DataBaseHelpers:

    __instance = None

    def __init__(self):
        self.connection = pymysql.connect(
            host="172.17.0.1",
            user="root",
            passwd="1111",
            database="pet_store"
        )

    def get_connection(self):
        return self.connection

    def close_connection(self):
        return self.connection.close()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = DataBaseHelpers()
        return cls.__instance


class PetTable:

    def __init__(self):
        self.db_connect = DataBaseHelpers().get_instance().get_connection()

    def create_pet_table(self):
        cursor = self.db_connect.cursor()
        sql = """CREATE TABLE pet (pet_id VARCHAR(255), pet_name VARCHAR(255), pet_status VARCHAR(255))"""
        cursor.execute(sql)

    def delete_pet_table(self):
        cursor = self.db_connect.cursor()
        sql = """DROP TABLE pet"""
        cursor.execute(sql)
        self.db_connect.commit()

    def insert_values_into_pet_table(self):
        cursor = self.db_connect.cursor()
        sql = """INSERT INTO pet (pet_id, pet_name, pet_status) VALUES (%s, %s, %s)"""
        values = (9222968140498034000, "Boris", "available")
        cursor.execute(sql, values)
        self.db_connect.commit()

    def get_variable_from_table(self, variable_name):
        cursor = self.db_connect.cursor()
        sql = f"""SELECT {variable_name} FROM pet"""
        cursor.execute(sql)
        return cursor.fetchone()[0]


class UserTable:

    def __init__(self):
        self.db_connect = DataBaseHelpers.get_instance().get_connection()

    def create_user_table(self):
        cursor = self.db_connect.cursor()
        sql = """CREATE TABLE user (user_id VARCHAR (255), username VARCHAR (255), firstname VARCHAR (255), 
        lastname VARCHAR (255), email VARCHAR (255), passwd VARCHAR (255), phone_number VARCHAR (255))"""
        cursor.execute(sql)
        self.db_connect.commit()

    def delete_user_table(self):
        cursor = self.db_connect.cursor()
        sql = """DROP TABLE user"""
        cursor.execute(sql)
        self.db_connect.commit()

    def insert_values_into_user_table(self):
        cursor = self.db_connect.cursor()
        sql = """INSERT INTO user (user_id, username, firstname, lastname, email, passwd, phone_number) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (9222968140498, "Max_K", "Max", "Korbut", "max@mail.com", 1111, "+375 29 111-11-11")
        cursor.execute(sql, values)
        self.db_connect.commit()

    def get_variable_from_table(self, variable_name):
        cursor = self.db_connect.cursor()
        sql = f"""SELECT {variable_name} FROM user"""
        cursor.execute(sql)
        return cursor.fetchone()[0]
