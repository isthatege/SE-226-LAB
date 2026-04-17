def calculate_mean(num_list):
    if not num_list:
        raise ValueError("Cannot compute mean of empty list.")
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    if not num_list:
        raise ValueError("Cannot find maximum of empty list.")
    return max(num_list)

def find_minimum(num_list):
    if not num_list:
        raise ValueError("Cannot find minimum of empty list.")
    return min(num_list)
