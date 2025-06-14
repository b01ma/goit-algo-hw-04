import random
import timeit

def generate_data(size ):
    return random.sample(range(size * 2), size)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
     
        
def timsort_runner(arr):
    sorted(arr)
    
def merge_sort_runner(arr):
    merge_sort(arr)
    
def insertion_sort_runner(arr):
    insertion_sort(arr)


def measure_time(sort_fn, data):
    def wrapper():
        arr = data.copy()
        sort_fn(arr)
    return timeit.timeit(wrapper, number=3) / 3  # середнє з 3 запусків


    
sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    
for size in sizes:
    data = generate_data(size)
    
    print(f"Soring time for the 1_000 elements")
    if size < 10_000: # if more -> takes too long to process
        print("Insertion Sort:", measure_time(insertion_sort, data)) 
    print("Merge Sort:", measure_time(merge_sort_runner, data))
    print("Timsort (Python built-in):", measure_time(timsort_runner, data))
    print('')

'''
Results: 
    Soring time for the 1_000 elements
    Insertion Sort: 0.012144263668839509
    Merge Sort: 0.0010514306680609782
    Timsort (Python built-in): 6.295832766530414e-05

    Soring time for the 10_000 elements
    Insertion Sort: 1.265389735994783
    Merge Sort: 0.01361091666816113
    Timsort (Python built-in): 0.0007977916684467345

    Soring time for the 100_000 elements
    Merge Sort: 0.16466740300529636
    Timsort (Python built-in): 0.010423471995939812

    Soring time for the 1_000_000 elements
    Merge Sort: 2.02980591666225
    Timsort (Python built-in): 0.19177066666694978

    Soring time for the 10_000_000 elements
    Merge Sort: 25.23001718066128
    Timsort (Python built-in): 2.393694972338077
'''

'''
Summery:
    
    Insertion Sort
        Працює дуже швидко тільки на малих масивах (до ~1 000 елементів).
        При 10 000 елементів — вже дуже повільний (1.26 сек) і далі просто не придатний до використання.
        Теоретична складність: O(n²), і це підтверджено на практиці — експоненційне зростання часу.
        Підходить лише для маленьких або майже відсортованих масивів
    
    Merge Sort
        Стабільно швидкий для будь-яких масивів, включно з великими.
        Навіть при 10 млн елементів показав хорошу продуктивність: ~25 сек.
        Теоретична складність: O(n log n), що підтверджено експериментально — час росте логарифмічно.
        Чудовий загальний алгоритм, особливо для великих наборів даних. Недолік — трохи більше споживання пам’яті через копії підмасивів.
        
    Timsort (вбудований в Python sorted)
        Найшвидший у всіх випадках.
        При 10 млн елементів — майже в 10 разів швидший, ніж реалізація Merge Sort.
        На маленьких масивах — взагалі миттєво працює.
        Найкращий варіант для загального використання. Саме тому всі вбудовані методи сортування в Python (sorted(), .sort()) використовують Timsort.
'''