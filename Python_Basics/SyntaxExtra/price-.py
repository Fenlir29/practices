price = float(input("ingrese precio del producto:"))
if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10
final_price =price - discount
print(f"El descuento para este producto es de: {final_price}")

