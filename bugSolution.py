def function_with_uncommon_error_solution(a, b):
    if a == 0 and b != 0:
        return float('inf')
    elif a == 0 and b == 0:
        return float('nan')
    elif b == 0:
        return float('inf')
    else:
        return a / b