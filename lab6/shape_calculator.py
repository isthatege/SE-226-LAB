import geometry_utils as geo

operations = {
    "circle_area": geo.circle_area,
    "circle_perimeter": geo.circle_perimeter,
    "rectangle_area": geo.rectangle_area,
    "rectangle_perimeter": geo.rectangle_perimeter,
    "triangle_area": geo.triangle_area
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")
op = input("Enter the operation you want to perform: ").strip()

if op not in operations:
    print("Invalid operation.")
    exit(1)

try:
    if op.startswith("circle"):
        radius = float(input("Enter radius: "))
        result = operations[op](radius)
    elif op.startswith("rectangle"):
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        result = operations[op](width, height)
    elif op.startswith("triangle"):
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = operations[op](base, height)
    print(f"Result: {result:.2f}")
except ValueError as e:
    if "could not convert" in str(e).lower():
        print("Input Error: Please enter numeric values.")
    else:
        print(f"Input Error: {e}")
