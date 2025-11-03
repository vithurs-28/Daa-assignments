#8. KMP vs Naive String Search Comparison
import time

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
        if j < len(pattern) and text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == len(pattern):
            indices.append(i - j)
            j = lps[j-1]
    
    return indices, comparisons

def naive_search(text, pattern):
    """Naive string search algorithm with comparison counting"""
    indices = []
    comparisons = 0
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            indices.append(i)
    
    return indices, comparisons

def compare_search_algorithms():
    text = "CATSABCBCABCDOGSABCBCABC"
    pattern = "ABCBCABC"
    
    print("\nString Search Algorithm Comparison:")
    print("=" * 50)
    
    start_time = time.time()
    kmp_indices, kmp_comparisons = kmp_search(text, pattern)
    kmp_time = (time.time() - start_time) * 1000
    
  
    start_time = time.time()
    naive_indices, naive_comparisons = naive_search(text, pattern)
    naive_time = (time.time() - start_time) * 1000
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Matches found: {len(kmp_indices)} at indices {kmp_indices}")
    
   
    if kmp_indices == naive_indices:
        print("✓ Both algorithms found the same matches")
    else:
        print("✗ Algorithms found different matches!")
        print(f"  KMP found: {kmp_indices}")
        print(f"  Naive found: {naive_indices}")
    
    print("\nComparison Results:")
    print(f"{'Algorithm':<12} {'Time (ms)':<12} {'Comparisons':<12} {'Efficiency':<12}")
    print(f"{'-' * 50}")
    print(f"{'KMP':<12} {kmp_time:<12.4f} {kmp_comparisons:<12} {'Better':<12}")
    print(f"{'Naive':<12} {naive_time:<12.4f} {naive_comparisons:<12} {'Worse':<12}")
    
    efficiency_ratio = naive_comparisons / kmp_comparisons if kmp_comparisons > 0 else 0
    time_ratio = naive_time / kmp_time if kmp_time > 0 else 0
    
    print(f"\nPerformance Summary:")
    print(f"KMP is {efficiency_ratio:.2f}x more efficient in comparisons")
    print(f"KMP is {time_ratio:.2f}x faster in execution time")
    
    return kmp_indices, naive_indices, kmp_comparisons, naive_comparisons


def test_multiple_patterns():
    """Test both algorithms with multiple patterns"""
    test_cases = [
        ("CATSABCBCABCDOGSABCBCABC", "ABCBCABC"),
        ("AABAACAADAABAABA", "AABA"),
        ("THIS IS A TEST TEXT", "TEST"),
        ("ABABDABACDABABCABAB", "ABABCABAB"),
    ]
    
    print("\n" + "="*60)
    print("COMPREHENSIVE ALGORITHM COMPARISON")
    print("="*60)
    
    for text, pattern in test_cases:
        print(f"\nTest Case: Text='{text[:20]}...', Pattern='{pattern}'")
        
        
        kmp_indices, kmp_comparisons = kmp_search(text, pattern)
        
       
        naive_indices, naive_comparisons = naive_search(text, pattern)
        
        print(f"Matches: {kmp_indices}")
        print(f"KMP Comparisons: {kmp_comparisons}")
        print(f"Naive Comparisons: {naive_comparisons}")
        
        if naive_comparisons > 0:
            ratio = naive_comparisons / kmp_comparisons
            print(f"Efficiency Ratio: {ratio:.2f}x")
        
        print("-" * 40)


if __name__ == "__main__":
  
    kmp_indices, naive_indices, kmp_comp, naive_comp = compare_search_algorithms()
    
  
    test_multiple_patterns()
    
   
    print("\n" + "="*60)
    print("PERFORMANCE ON LARGER TEXT")
    print("="*60)
    

    large_text = "A" * 1000 + "CATSABCBCABCDOGSABCBCABC" + "B" * 1000
    pattern = "ABCBCABC"
    
    start_time = time.time()
    kmp_indices, kmp_comparisons = kmp_search(large_text, pattern)
    kmp_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    naive_indices, naive_comparisons = naive_search(large_text, pattern)
    naive_time = (time.time() - start_time) * 1000
    
    print(f"Large text size: {len(large_text)} characters")
    print(f"KMP: {kmp_time:.4f} ms, {kmp_comparisons} comparisons")
    print(f"Naive: {naive_time:.4f} ms, {naive_comparisons} comparisons")
    print(f"KMP is {naive_comparisons/kmp_comparisons:.2f}x more efficient")