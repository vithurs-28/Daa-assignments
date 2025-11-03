#6. KMP Algorithm Implementation
def compute_lps(pattern):
    """Compute Longest Prefix Suffix table for KMP algorithm"""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """KMP string search algorithm with comparison counting"""
    if not pattern:
        return [], 0
    
    lps = compute_lps(pattern)
    i = j = 0
    indices = []
    comparisons = 0
    
    while i < len(text):
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            indices.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return indices, comparisons


text = "CATSABCBCABCDOGSABCBCABC"
pattern = "ABCBCABC"
indices, comparisons = kmp_search(text, pattern)
print(f"KMP Search: Pattern found at indices {indices}")
print(f"Comparisons made: {comparisons}")