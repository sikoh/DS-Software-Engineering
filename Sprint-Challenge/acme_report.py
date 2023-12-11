from acme import Product
import random
import pandas as pd

def generate_products(list1=None, list2=None, n_products=30):
    """
    Takes a list of adjectives and a list of nouns as the first and second parameters
    and generates as many random names of products as indicated in the 3rd parameter (default 30).
    """
    list1 = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved', 'Magic']
    list2 = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Pen', 'Cube', 'Trap']
    return [f"{random.choice(list1)} {random.choice(list2)}" for p in range(n_products)]

def inventory_report(p_list):
    """
    Takes a list of product names, then instantiates each using the Product class,
    assigns random values to the features of each product, and returns a summary report using a DataFrame.
    """
    report_dic = {'id': [], 'Name': [], 'Price': [], 'Weight': [], 'Flammability': []}

    for product_name in p_list:
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = round(random.uniform(0.0, 2.5), 1)

        prod = Product(product_name)
        prod.price = price
        prod.weight = weight
        prod.flammability = flammability

        report_dic['id'].append(prod.identifier)
        report_dic['Name'].append(prod.name)
        report_dic['Price'].append(prod.price)
        report_dic['Weight'].append(prod.weight)
        report_dic['Flammability'].append(prod.flammability)

    report_df = pd.DataFrame(report_dic)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f"Unique Product Names: {report_df['Name'].nunique()}")
    print(f"Average Price: {round(report_df['Price'].mean(), 2)}")
    print(f"Average Weight: {round(report_df['Weight'].mean(), 2)}")
    print(f"Average Flammability: {round(report_df['Flammability'].mean(), 2)}")

# Example usage
inventory_report(generate_products())
