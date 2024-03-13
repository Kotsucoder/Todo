def calculate_time(g=9.80665, h):
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)