def knapsack_bruteforce_binary(values, weights, capacity):
    n = len(values)
    best_value = 0
    best_mask = 0

   
    for mask in range(1 << n): 
        total_weight = 0
        total_value = 0

      
        for i in range(n):
            if (mask >> i) & 1: 
                total_weight += weights[i]
                total_value += values[i]

        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_mask = mask

    best_items = [i for i in range(n) if (best_mask >> i) & 1]

    return best_value, best_items


# Example 
values = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
capacity = 15

best_value, best_items = knapsack_bruteforce_binary(values, weights, capacity)
print("Best value:", best_value)
print("Items chosen (indices):", best_items)