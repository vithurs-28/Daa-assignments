#7. Sorting Algorithms Empirical Analysis
import time
import random

class SortingAnalysis:
    def __init__(self):
        self.operations = 0
    
    def bubble_sort(self, arr):
        self.operations = 0
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.operations += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.operations += 1
        return arr
    
    def selection_sort(self, arr):
        self.operations = 0
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.operations += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.operations += 1
        return arr
    
    def analyze_sorting(self, data_size=1000):
        data = [random.randint(1, 10000) for _ in range(data_size)]
        
        print(f"\nSorting Analysis for {data_size} elements:")
        print("-" * 50)
        
        algorithms = [
            ('Bubble Sort', self.bubble_sort),
            ('Selection Sort', self.selection_sort),
        ]
        
        for name, algorithm in algorithms:
            start_time = time.time()
            sorted_data = algorithm(data)
            end_time = time.time()
            
            time_taken = (end_time - start_time) * 1000  
            print(f"{name:<15}: {time_taken:8.2f} ms, {self.operations:8d} operations")


analyzer = SortingAnalysis()
analyzer.analyze_sorting(500)