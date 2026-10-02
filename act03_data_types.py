var_int = 10
var_float = 3.14
var_str = "hi"
var_bool = True
var_none = None

values = [var_int, var_float, var_str, var_bool, var_none]

print("TABLA DE TIPOS:")
for v in values:
    print(f"{str(v):<8} -> {type(v)}")

print("\nPRUEBA DECIMAL:")
print(f"¿0.1 + 0.2 == 0.3? -> {0.1 + 0.2 == 0.3}")
print(f"Valor real de 0.1 + 0.2 -> {0.1 + 0.2}")

# print("3" + 3)