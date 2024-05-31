import os
import sqlite3
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from scrapy.exceptions import DropItem


class SQLitePipeline:
    def __init__(self):
        self.connection = sqlite3.connect('computers.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS computers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                computer_name TEXT,
                processor TEXT,
                gpu TEXT,
                motherboard TEXT,
                ram TEXT,
                UNIQUE (computer_name, processor, gpu, motherboard, ram)
            )
        """)

    def process_item(self, item, spider):
        self.store_item(item)
        return item

    def store_item(self, item):
        self.cursor.execute("""
            INSERT OR IGNORE INTO computers (computer_name, processor, gpu, motherboard, ram)
            VALUES (?, ?, ?, ?, ?)
        """, (
            item['computer_name'],
            item['processor'],
            item['gpu'],
            item['motherboard'],
            item['ram']
        ))
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()


class JsonSchemaValidationPipeline:
    def __init__(self):
        schema_path = os.path.join(os.path.dirname(__file__), 'computer_schema.json')
        with open(schema_path) as f:
            self.schema = json.load(f)

    def process_item(self, item, spider):
        try:
            validate(item, self.schema)
        except ValidationError as e:
            raise DropItem(f"JSON Schema validation failed: {e}")
        return item
