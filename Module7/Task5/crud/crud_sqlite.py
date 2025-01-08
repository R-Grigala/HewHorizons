import sqlite3
from typing import List, Dict, Any, Optional
from Module7.Task5.crud.initialize_database import initialize_database

class BaseRepository:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

    def _execute_query(self, query: str, params: tuple = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def create(self, fields: List[str], values: tuple):
        fields_str = ", ".join(fields)
        placeholders = ", ".join(["?" for _ in fields])
        query = f"INSERT INTO {self.table_name} ({fields_str}) VALUES ({placeholders})"
        self._execute_query(query, values)

    def get_all(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name}"
        cursor = self._execute_query(query)
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_by_id(self, record_id: int) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        cursor = self._execute_query(query, (record_id,))
        result = cursor.fetchone()
        if result:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, result))
        return None

    def update(self, record_id: int, fields: List[str], values: tuple):
        set_clause = ", ".join([f"{field} = ?" for field in fields])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
        self._execute_query(query, values + (record_id,))

    def delete_by_id(self, record_id: int):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._execute_query(query, (record_id,))

class ProductRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Product")

class ProductModelRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "ProductModel")

class CategoryRepository(BaseRepository):
    def __init__(self, db_name: str):
        super().__init__(db_name, "Category")

    def get_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE name = ?"
        cursor = self._execute_query(query, (name,))
        result = cursor.fetchone()
        if result:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, result))
        return None


if __name__ == "__main__":

    initialize_database()

    db_name = "ecommerce.db"
    category_repo = CategoryRepository(db_name)
    product_model_repo = ProductModelRepository(db_name)
    product_repo = ProductRepository(db_name)

    category_repo.create(
        fields=["name", "modified_date", "parent_category_id"],
        values=("Smartphones", "2025-01-01", 1)
    )

    product_model_repo.create(
        fields=["name", "catalog_description", "modified_date"],
        values=('Samsung Galaxy S22', 'Flagship smartphone from Samsung', "2025-01-01")
    )

    product_repo.create(
        fields=["name", "product_number", "color", "standard_cost", "list_price", "size", "weight", 
                "product_category_id", "product_model_id", "sell_start_date", "sell_end_date", 
                "modified_date"],
        values=('iPhone 14 Pro', 'IP14P001', 'Silver', 999.99, 1099.99, '6.1', 0.2, 1, 1, '2025-01-05', '2025-12-31', '2025-01-06')
    )

    # Get all products
    products = product_repo.get_all()
    print(products)

    # Get product by ID
    product = product_repo.get_by_id(1)
    print(product)

    # Update a product
    product_repo.update(
        record_id=1,
        fields=["list_price"],
        values=(25.99,)
    )

    # Delete a product
    product_repo.delete_by_id(1)

    # Get all products
    products = product_repo.get_all()
    print(products)