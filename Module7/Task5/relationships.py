from datetime import datetime
from typing import List, Optional

class Category:
    def __init__(self, category_id: int, name: str, modified_date: datetime, parent_category: Optional['Category'] = None):
        self.category_id = category_id
        self.name = name
        self.modified_date = modified_date
        self.parent_category = parent_category
        self.subcategories: List['Category'] = []

    def add_subcategory(self, subcategory: 'Category'):
        self.subcategories.append(subcategory)

class ProductModel:
    def __init__(self, model_id: int, name: str, catalog_description: Optional[str], modified_date: datetime):
        self.model_id = model_id
        self.name = name
        self.catalog_description = catalog_description
        self.modified_date = modified_date

class Product:
    def __init__(self, product_id: int, name: str, product_number: str, color: Optional[str], standard_cost: float,
                 list_price: float, size: Optional[str], weight: Optional[float], product_category: Category,
                 product_model: Optional[ProductModel], sell_start_date: datetime, sell_end_date: Optional[datetime],
                 discontinued_date: Optional[datetime], modified_date: datetime):
        self.product_id = product_id
        self.name = name
        self.product_number = product_number
        self.color = color
        self.standard_cost = standard_cost
        self.list_price = list_price
        self.size = size
        self.weight = weight
        self.product_category = product_category
        self.product_model = product_model
        self.sell_start_date = sell_start_date
        self.sell_end_date = sell_end_date
        self.discontinued_date = discontinued_date
        self.modified_date = modified_date

class Address:
    def __init__(self, address_id: int, line1: str, line2: Optional[str], city: str, state_province: str,
                 postal_code: str, country_region: str, modified_date: datetime):
        self.address_id = address_id
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country_region = country_region
        self.modified_date = modified_date

class Customer:
    def __init__(self, customer_id: int, name_style: int, title: Optional[str], first_name: str, middle_name: Optional[str],
                 last_name: str, suffix: Optional[str], company_name: Optional[str], sales_person: Optional[str],
                 email_address: Optional[str], phone: Optional[str], modified_date: datetime):
        self.customer_id = customer_id
        self.name_style = name_style
        self.title = title
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.suffix = suffix
        self.company_name = company_name
        self.sales_person = sales_person
        self.email_address = email_address
        self.phone = phone
        self.modified_date = modified_date
        self.addresses: List['CustomerAddress'] = []
        self.orders: List['Order'] = []

    def add_address(self, address: 'CustomerAddress'):
        self.addresses.append(address)

    def add_order(self, order: 'Order'):
        self.orders.append(order)

class CustomerAddress:
    def __init__(self, customer: Customer, address: Address, address_type: str, modified_date: datetime):
        self.customer = customer
        self.address = address
        self.address_type = address_type
        self.modified_date = modified_date

class OrderDetail:
    def __init__(self, order_detail_id: int, product: Product, order_qty: int, unit_price: float, unit_price_discount: float,
                 modified_date: datetime):
        self.order_detail_id = order_detail_id
        self.product = product
        self.order_qty = order_qty
        self.unit_price = unit_price
        self.unit_price_discount = unit_price_discount
        self.line_total = unit_price * (1 - unit_price_discount) * order_qty
        self.modified_date = modified_date

class Order:
    def __init__(self, order_id: int, order_number: str, revision_number: int, order_date: datetime, ship_date: Optional[datetime],
                 status: int, online_order_flag: int, purchase_order_number: Optional[str], account_number: Optional[str],
                 customer: Customer, ship_to_address: Address, bill_to_address: Address, ship_method: Optional[str],
                 sub_total: float, tax_amt: float, freight: float, comment: Optional[str], modified_date: datetime):
        self.order_id = order_id
        self.order_number = order_number
        self.revision_number = revision_number
        self.order_date = order_date
        self.ship_date = ship_date
        self.status = status
        self.online_order_flag = online_order_flag
        self.purchase_order_number = purchase_order_number
        self.account_number = account_number
        self.customer = customer
        self.ship_to_address = ship_to_address
        self.bill_to_address = bill_to_address
        self.ship_method = ship_method
        self.sub_total = sub_total
        self.tax_amt = tax_amt
        self.freight = freight
        self.total_due = sub_total + tax_amt + freight
        self.comment = comment
        self.modified_date = modified_date
        self.order_details: List[OrderDetail] = []

    def add_order_detail(self, order_detail: OrderDetail):
        self.order_details.append(order_detail)