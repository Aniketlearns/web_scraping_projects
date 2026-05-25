# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import sqlite3

from quotes.models import db_connect, create_table, Quote
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem

class QuotesPipeline:
    def __init__(self):
        engine=db_connect()  
        create_table(engine)
        self.Session=sessionmaker(bind=engine)
        pass

    def process_item(self, item, spider):
        session = self.Session()
        quote=Quote()
        quote.Quotes=str(item['quote'])
        quote.Author=str(item['author'])
        # quote.Author=str(item['author'][0])
        quote.Tags=str(item['tags'][0])
        try:
            session.add(quote)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
    
class DuplicatePipeline:
    def __init__(self):
        engine=db_connect()  
        create_table(engine)
        self.Session=sessionmaker(bind=engine)



    def process_item(self, item, spider):
        session = self.Session()
        exist_quote = session.query(Quote).filter_by(Quotes=str(item['quote'])).first()
        if exist_quote is not None:
            raise DropItem('Duplicate item detected %s' %str(item['quote']))
            session.close()
        else:
            return item
            session.close()