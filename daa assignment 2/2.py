def get_combinations(items, k):
    "Return all possible groups of size k from the given list."
    result = []                 
    n = len(items)

    def helper(start, current):
        # Base case
        if len(current) == k:
            result.append(current.copy())
            return


        for i in range(start, n):
            current.append(items[i]) 
            helper(i + 1, current)    
            current.pop()              

    helper(0, [])
    return result


# Example
letters = ['a', 'b', 'c', 'd']
print(f"All combinations of {letters} taken 2 at a time:")
for combo in get_combinations(letters, 2):
    print(combo)