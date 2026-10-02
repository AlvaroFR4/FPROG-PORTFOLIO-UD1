from config import IVA, DISCOUNT, CURRENCY

base_price = 100

total = base_price * (1 + IVA)
final = total - (total * DISCOUNT)

print("=== INVOICE / FACTURA ===")
print(f"Precio base: {base_price:>6.2f} {CURRENCY}")
print(f"Total (+IVA):{total:>6.2f} {CURRENCY}")
print(f"Total final: {final:>6.2f} {CURRENCY}")
print("=========================")