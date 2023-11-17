def get_products(**datos):
	print(f" Se vende el producto {datos['name']} en {datos['price']}")


get_products(id="id",
             name="iPhone 12 Pro Max",
             price=1000.00,
             stock=10,
             active=True)
