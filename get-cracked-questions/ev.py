# Calculate the expected value of a die with n sides

def die_expected_value(n):
    expected_val = 0
    for i in range(n + 1):
        expected_val += (i * (1 / n)) 
    
    return round(expected_val, 1)

