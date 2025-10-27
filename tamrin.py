product_list = [
    {"id": 1, "name": "mobile", "quantity": 5, "price": "400"},
    {"id": 2, "name": "laptop", "quantity": 5, "price": "800"},
    {"id": 3, "name": "SPEAKER", "quantity": 11, "price": "700"},
    {"id": 4, "name": "mOnitor", "quantity": 3, "price": "600"},
    {"id": 5, "name": "mouse", "quantity": 6, "price": "350"},
    {"id": 6, "name": "keyboard", "quantity": 4, "price": "200"},
    {"id": 7, "name": "toUCh", "quantity": 9, "price": "800"},
]

# map / filter / ...
# اجازه ی استفاده از for ندارید

# تبدیل price ها به عدد
def cast_price_to_float(product):
    product["price"] = float(product["price"])
    return product

converted_price = list(map(cast_price_to_float,product_list))
print(converted_price)

# اضافه کردن total به هر دیکشنری
def add_total(product):
    product["total"] = product["quantity"] * product["price"]
    return product

total_product = list(map(add_total,product_list))
print(product_list)


# capitilize کردن تمامی اسامی
def capitalize_names(name):
    name["name"] = name["name"].capitalize()
    return name

final_name = list(map(capitalize_names,product_list))
print(final_name)


# لیست اسم کالاهای با مجموع کمتر از 5000
def under_5000(product):
    return product["quantity"] * product["price"] < 5000

def get_name(product):
    return product["name"].capitalize()

filter_products = list(filter(under_5000,product_list))
product_names = list(map(get_name,filter_products))
print(product_names)

# لیست اسم کالاهای با مجموع بیشتر از 5000
def upper_5000(product):
    return product["quantity"] * product["price"] > 5000

filter_products = list(filter(upper_5000,product_list))
product_name = list(map(get_name,filter_products))
print(product_name)

# جمع کل فاکتور

