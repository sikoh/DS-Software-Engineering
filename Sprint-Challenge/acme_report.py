from random import randint, sample, uniform
from acme import Product
import pandas as pd

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Gadget']


def generate_products(num_products=30):
    products = []
    for p in range(num_products):
        name = f"{sample(ADJECTIVES, 1)[0]} {sample(NOUNS, 1)[0]}"
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = round(uniform(0.0, 2.5), 1)

        product = Product(name, price=price, weight=weight, flammability=flammability)
        products.append(product)

    return products


def inventory_report(products):
    report_df = pd.DataFrame({
        'Name': [product.name for product in products],
        'Price': [product.price for product in products],
        'Weight': [product.weight for product in products],
        'Flammability': [product.flammability for product in products]
    })

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f"Unique Product Names: {report_df['Name'].nunique()}")
    print(f"Average Price: {round(report_df['Price'].mean(), 2)}")
    print(f"Average Weight: {round(report_df['Weight'].mean(), 2)}")
    print(f"Average Flammability: {round(report_df['Flammability'].mean(), 2)}")


if __name__ == '__main__':
    inventory_report(generate_products())
