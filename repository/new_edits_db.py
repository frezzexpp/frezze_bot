import psycopg2
from configs.config import Bot_config

cfg_db = Bot_config()

class PostgreSql_new_edit:
    def __init__(self):
        self.connect = psycopg2.connect(
            host=cfg_db.host,
            user=cfg_db.user,
            database=cfg_db.database,
            password=cfg_db.password
        )
        self.cursor = self.connect.cursor()


    def select_data(self):
        self.cursor.execute(f"""
            SELECT edit_name, edit_url, edit_file
            FROM new_edits
        """)

        return self.cursor.fetchall()

obj = PostgreSql_new_edit()
print(obj.select_data())