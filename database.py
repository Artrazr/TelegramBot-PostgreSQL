import psycopg2 

class DatBase:
    
    def __init__(self):
        #подключение к базе данных
        self.connection = psycopg2.connect(database = 'см. readme',
                                           user = 'см. readme',
                                           password = 'см. readme',
                                           host = 'см. readme',
                                           port = 'см. readme')
        self.cursor = self.connection.cursor()
        

#регистрация зрителя       
    def add_viewer(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO viewer (user_id, number) values (%s, %s)"            
            self.cursor.executemany(query, [data])
            self.connection.commit()
 
#проверка зарегистрирован ли зритель в базе           
    def check_viewer(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM viewer WHERE user_id = %s"%user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())
#удаление зрителя из базы
    def remove_viewer(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("DELETE FROM viewer WHERE user_id = %s"%user_id)
            self.connection.commit()
            
#регистрация журналиста  
    def add_jour(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO journ (user_id, number, redaction) values (%s, %s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()
 
#проверка зарегистрирован ли журналист в базе           
    def check_jour(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM journ WHERE user_id = %s"%user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())
            
#удаление журналиста из базы
    def remove_jour(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("DELETE FROM journ WHERE user_id = %s"%user_id)
            self.connection.commit()   
            