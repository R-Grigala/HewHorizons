import csv
import json
import pickle
from typing import List, Any, Type, TypeVar
from datetime import datetime

from relationships import *

# Type variable for generic class handling
T = TypeVar('T')

class BaseModel:
    @staticmethod
    def saveCsv(filename: str, items: List[T]):
        """Save a list of objects to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header (assuming we are dealing with simple attributes)
            writer.writerow(items[0].__dict__.keys())  # Write field names as header
            for item in items:
                writer.writerow(item.__dict__.values())  # Write object values

    @staticmethod
    def loadCsv(file_path: str, class_type) -> List:
        items = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Remove 'subcategories' from row data
                subcategories = row.pop('subcategories', None)
                # Create the instance of the class
                item = class_type(**row)
                # If the class has a subcategories attribute, initialize it
                if hasattr(item, 'subcategories'):
                    item.subcategories = []  # Initialize as empty list or handle accordingly
                items.append(item)
        return items
    
    @staticmethod
    def saveJson(filename: str, items: List[T]):
        """Save a list of objects to a JSON file."""
        with open(filename, 'w') as file:
            # Serialize the objects to JSON (converting datetime objects to string)
            json.dump([item.__dict__ for item in items], file, default=str)

    @staticmethod
    def loadJson(filename: str, class_type: Type[T]) -> List[T]:
        """Load objects from a JSON file into a list of instances of the given class."""
        with open(filename, 'r') as file:
            items_dict = json.load(file)
        return [class_type(**item) for item in items_dict]

    @staticmethod
    def savePickle(filename: str, items: List[T]):
        """Save a list of objects to a pickle file."""
        with open(filename, 'wb') as file:
            pickle.dump([item.__dict__ for item in items], file)

    @staticmethod
    def loadPickle(filename: str, class_type: Type[T]) -> List[T]:
        """Load objects from a pickle file into a list of instances of the given class."""
        with open(filename, 'rb') as file:
            items_dict = pickle.load(file)
        return [class_type(**item) for item in items_dict]


# Create some objects
category1 = Category(1, 'Electronics', datetime.now())
category2 = Category(2, 'Appliances', datetime.now())

product1 = Product(1, 'Smartphone', 'SP-001', 'Black', 500, 1000, 'Medium', 0.3, category1, None, datetime.now(), None, None, datetime.now())

# Save to CSV, JSON, and Pickle
BaseModel.saveCsv('categories.csv', [category1, category2])
BaseModel.saveJson('products.json', [product1])
BaseModel.savePickle('categories.pkl', [category1, category2])

# Load from CSV, JSON, and Pickle
categories_from_csv = BaseModel.loadCsv('categories.csv', Category)
products_from_json = BaseModel.loadJson('products.json', Product)

print(categories_from_csv)
print(products_from_json)