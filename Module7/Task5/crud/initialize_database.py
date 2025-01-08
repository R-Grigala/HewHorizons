import sqlite3

def initialize_database():
    connection = sqlite3.connect('ecommerce.db')  # Database file name
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Category (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            modified_date TEXT NOT NULL,
            parent_category_id INTEGER,
            FOREIGN KEY (parent_category_id) REFERENCES Category(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ProductModel (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            catalog_description TEXT,
            modified_date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            product_number TEXT NOT NULL,
            color TEXT,
            standard_cost REAL NOT NULL,
            list_price REAL NOT NULL,
            size TEXT,
            weight REAL,
            product_category_id INTEGER NOT NULL,
            product_model_id INTEGER,
            sell_start_date TEXT NOT NULL,
            sell_end_date TEXT,
            discontinued_date TEXT,
            modified_date TEXT NOT NULL,
            FOREIGN KEY (product_category_id) REFERENCES Category(id),
            FOREIGN KEY (product_model_id) REFERENCES ProductModel(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Address (
            id INTEGER PRIMARY KEY,
            line1 TEXT NOT NULL,
            line2 TEXT,
            city TEXT NOT NULL,
            state_province TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            country_region TEXT NOT NULL,
            modified_date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            id INTEGER PRIMARY KEY,
            name_style INTEGER NOT NULL,
            title TEXT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            suffix TEXT,
            company_name TEXT,
            sales_person TEXT,
            email_address TEXT,
            phone TEXT,
            modified_date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CustomerAddress (
            id INTEGER NOT NULL,
            address_id INTEGER NOT NULL,
            address_type TEXT NOT NULL,
            modified_date TEXT NOT NULL,
            customer_id INTEGER NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer(id),
            FOREIGN KEY (address_id) REFERENCES Address(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS `Order` (
            id INTEGER PRIMARY KEY,
            order_number TEXT NOT NULL,
            revision_number INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            ship_date TEXT,
            status INTEGER NOT NULL,
            online_order_flag INTEGER NOT NULL,
            purchase_order_number TEXT,
            account_number TEXT,
            customer_id INTEGER NOT NULL,
            ship_to_address_id INTEGER NOT NULL,
            bill_to_address_id INTEGER NOT NULL,
            ship_method TEXT,
            sub_total REAL NOT NULL,
            tax_amt REAL NOT NULL,
            freight REAL NOT NULL,
            total_due REAL NOT NULL,
            comment TEXT,
            modified_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer(id),
            FOREIGN KEY (ship_to_address_id) REFERENCES Address(id),
            FOREIGN KEY (bill_to_address_id) REFERENCES Address(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS OrderDetail (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            order_qty INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            unit_price_discount REAL NOT NULL,
            line_total REAL NOT NULL,
            modified_date TEXT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES `Order`(id),
            FOREIGN KEY (product_id) REFERENCES Product(id)
        )
    ''')

    connection.commit()
    connection.close()

