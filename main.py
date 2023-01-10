import random
from src.bubble_sort import BubbleSort
from src.heap_sort import HeapSort
from src.merge_sort import MergeSort
from src.quick_sort import QuickSort

if __name__ == "__main__":
    random_array = [random.randint(0, 100) for i in range(10)]
    while True:
        print("Random Array: ", random_array)
        print("1. Bubble Sort")
        print("2. Heap Sort")
        print("3. Merge Sort")
        print("4. Quick Sort")
        print("5. Exit")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                new_array = BubbleSort.sort(random_array)
            elif option == 2:
                new_array = HeapSort.sort(random_array)
            elif option == 3:
                new_array = MergeSort.sort(random_array)
            elif option == 4:
                new_array = QuickSort.sort(random_array)
            elif option == 5:
                break
            else:
                raise ValueError
            print("Sorted Array: ", new_array, "\n")
        except ValueError:
            print("Invalid input! Please, try again...")
