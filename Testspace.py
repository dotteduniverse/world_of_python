"""
Data Generator for Retail Enrichment Pipeline
Run: pip install pandas faker
"""

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# ---------- CONFIGURATION ----------
NUM_CUSTOMERS = 500
NUM_PRODUCTS = 50
NUM_STORES = 20
NUM_TRANSACTIONS = 10000
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 4, 6)

# Realistic loyalty tier distribution (%)
TIER_DIST = {'Gold': 0.15, 'Silver': 0.25, 'Bronze': 0.40, 'None': 0.20}

# Realistic product categories & brands
CATEGORIES = {
    'Electronics': ['Apple', 'Samsung', 'Sony', 'Dell', 'Logitech', 'Bose'],
    'Apparel': ['Nike', 'Adidas', 'Uniqlo', 'Zara', 'Levis', 'Under Armour'],
    'Home Goods': ['IKEA', 'Contigo', 'OXO', 'Cuisinart', 'Keurig'],
    'Fitness': ['Manduka', 'Fitbit', 'Garmin', 'Peloton', 'Theragun']
}

# Realistic product name templates per category
PROD_NAME_TEMPLATES = {
    'Electronics': ['Wireless Mouse', 'Bluetooth Keyboard', 'USB-C Hub', 'Ultra HD Monitor', 'Noise Cancelling Headphones', 'Smartwatch', 'Tablet', 'Laptop Stand'],
    'Apparel': ['Cotton T-Shirt', 'Running Shorts', 'Hoodie', 'Sneakers', 'Baseball Cap', 'Leggings', 'Windbreaker'],
    'Home Goods': ['Stainless Water Bottle', 'Coffee Maker', 'Non-stick Pan', 'Bath Towel', 'Desk Lamp', 'Storage Bin'],
    'Fitness': ['Yoga Mat', 'Resistance Bands', 'Dumbbell Set', 'Foam Roller', 'Jump Rope', 'Water Bottle']
}

# Store cities with realistic state mapping
CITIES_STATES = [
    ('New York', 'NY'), ('Los Angeles', 'CA'), ('Chicago', 'IL'), ('Houston', 'TX'),
    ('Phoenix', 'AZ'), ('Philadelphia', 'PA'), ('San Antonio', 'TX'), ('San Diego', 'CA'),
    ('Dallas', 'TX'), ('Austin', 'TX'), ('Boston', 'MA'), ('Seattle', 'WA'),
    ('Denver', 'CO'), ('Miami', 'FL'), ('Atlanta', 'GA'), ('Portland', 'OR')
]

# ---------- GENERATE DIMENSION TABLES ----------

def generate_customers(n):
    customers = []
    tiers = []
    for _ in range(n):
        tier = np.random.choice(list(TIER_DIST.keys()), p=list(TIER_DIST.values()))
        customers.append(f"CUST_{fake.unique.random_number(digits=5)}")
        tiers.append(tier)
    df = pd.DataFrame({
        'customer_id': customers,
        'customer_name': [fake.name() for _ in range(n)],
        'loyalty_tier': tiers,
        'region': [fake.state() for _ in range(n)]   # realistic region from US state
    })
    return df

def generate_products(n):
    products = []
    for i in range(n):
        cat = random.choice(list(CATEGORIES.keys()))
        brand = random.choice(CATEGORIES[cat])
        name_template = random.choice(PROD_NAME_TEMPLATES[cat])
        product_name = f"{brand} {name_template}"
        if random.random() > 0.8:  # add a variant
            product_name += f" {random.choice(['Pro', 'Lite', 'Plus', 'Max'])}"
        products.append({
            'product_id': f"PROD_{fake.unique.random_number(digits=4)}",
            'product_name': product_name,
            'category': cat,
            'brand': brand
        })
    return pd.DataFrame(products)

def generate_stores(n):
    stores = []
    selected_cities = random.sample(CITIES_STATES, min(n, len(CITIES_STATES)))
    # if we need more stores than unique city-state combos, repeat with suffix
    for i in range(n):
        city, state = selected_cities[i % len(selected_cities)]
        store_name = f"{city} {fake.word().capitalize()} {random.choice(['Market', 'Plaza', 'Store', 'Outlet'])}"
        stores.append({
            'store_id': f"STORE_{fake.unique.lexify(text='???_??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{i}",
            'store_name': store_name,
            'city': city,
            'state': state
        })
    return pd.DataFrame(stores)

# ---------- GENERATE TRANSACTIONS (FACT TABLE) ----------

def generate_transactions(num, customers_df, products_df, stores_df, start_date, end_date):
    transactions = []
    date_range = (end_date - start_date).days
    
    for _ in range(num):
        cust = customers_df.sample(1).iloc[0]
        prod = products_df.sample(1).iloc[0]
        store = stores_df.sample(1).iloc[0]
        
        # realistic quantity: 1-5 for electronics, 1-10 for others
        if prod['category'] == 'Electronics':
            qty = np.random.choice([1, 1, 1, 2, 2, 3])  # mostly 1
        else:
            qty = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p=[0.3,0.2,0.15,0.1,0.1,0.05,0.03,0.03,0.02,0.02])
        
        # unit price based on category
        base_price = {
            'Electronics': random.uniform(20, 1500),
            'Apparel': random.uniform(10, 120),
            'Home Goods': random.uniform(5, 200),
            'Fitness': random.uniform(15, 300)
        }.get(prod['category'], 50)
        # add brand multiplier
        brand_multiplier = 1.0
        if prod['brand'] in ['Apple', 'Sony', 'Bose', 'Peloton']:
            brand_multiplier = 1.3
        elif prod['brand'] in ['Nike', 'Adidas']:
            brand_multiplier = 1.2
        unit_price = round(base_price * brand_multiplier + random.uniform(-5, 5), 2)
        unit_price = max(0.99, unit_price)
        
        # transaction date - more recent dates slightly more likely
        rand_days = int(np.random.exponential(scale=date_range/3))
        rand_days = min(rand_days, date_range)
        trans_date = start_date + timedelta(days=rand_days)
        trans_date = trans_date.replace(hour=random.randint(9,21), minute=random.randint(0,59), second=random.randint(0,59))
        
        transactions.append({
            'transaction_id': f"TXN_{fake.unique.random_number(digits=8)}",
            'customer_id': cust['customer_id'],
            'product_id': prod['product_id'],
            'transaction_date': trans_date.strftime('%Y-%m-%d %H:%M:%S'),
            'quantity': qty,
            'unit_price': unit_price,
            'store_id': store['store_id']
        })
    return pd.DataFrame(transactions)

# ---------- MAIN GENERATION ----------
if __name__ == "__main__":
    print("Generating dimension tables...")
    customers = generate_customers(NUM_CUSTOMERS)
    products = generate_products(NUM_PRODUCTS)
    stores = generate_stores(NUM_STORES)
    
    print("Generating transactions...")
    transactions = generate_transactions(NUM_TRANSACTIONS, customers, products, stores, START_DATE, END_DATE)
    
    # Save to CSV
    customers.to_csv("customer_dim.csv", index=False)
    products.to_csv("product_dim.csv", index=False)
    stores.to_csv("store_dim.csv", index=False)
    transactions.to_csv("raw_transactions.csv", index=False)
    
    print(f"Generated {len(customers)} customers, {len(products)} products, {len(stores)} stores, {len(transactions)} transactions.")
    print("Files saved: customer_dim.csv, product_dim.csv, store_dim.csv, raw_transactions.csv")