cart=[
{"item":"keyboard","price":50.00,"quantity":1},
{"item":"mouse","price":25.00,"quantity":2},
{"item":"monitor","price":200.00,"quantity":1},
{"item":"headphones","price":75.00,"quantity":1}] 



total=0

for product in cart:
    print(f"Item: {product['item']}, Price: {product['price']}, Quantity: {product['quantity']}")
    total += product['price'] * product['quantity']

print(f"Total: ${total:.2f}")

