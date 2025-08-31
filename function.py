def calculate_area (a, b, shape):
    if shape == "rectangle":
        area = a*b
    else:
        area = (1/2)*a*b
    return area
def print_pattern(n):
    
    for i in range(n):
        s = '' 
        for j in range(i + 1):
            s = s + '*'
        print(s)

print(print_pattern(3))