# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
import sqlite3
#
class FlickzeePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("flickzee.db")
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS flickzee""")
        self.curr.execute("""create table flickzee(
        Movie_Name text,
        Movie_Url text,
        Image_Name text
        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into flickzee values(?,?,?)""",(
          item['Movie_Name'][0],
          item['Movie_Url'][0],
          item['Image_Name'][0]

        ))
        self.conn.commit()

