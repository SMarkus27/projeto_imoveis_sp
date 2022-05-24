import mysql.connector
from itemadapter import ItemAdapter


class OlxPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='user',
            passwd='password',
            database='db'
            )

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS olx_crawl""")
        self.curr.execute("""create table olx_crawl(
                        category text,
                        iptu text,
                        bathrooms text,
                        type_house text,
                        size text,
                        bedrooms text,
                        garage text,
                        condominium text,
                        district text,
                        city text

                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        self.curr.execute(f"""INSERT INTO olx_crawl VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",list((
            item['category'],
            item['iptu'],
            item['bathrooms'],
            item['type_house'],
            item['size'],
            item['bedrooms'],
            item['garage'],
            item['condominium'],
            item['district'],
            item['city'],


                ))
        )

        self.conn.commit()
        