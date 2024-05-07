class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        pass


class BubbleSort(SortingAlgorithm):
    def sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]


class SelectionSort(SortingAlgorithm):
    def sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]


class InsertionSort(SortingAlgorithm):
    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

# Bubble Sort
bubble_sort = BubbleSort(arr.copy())
bubble_sort.sort()
print("Sorted array using Bubble Sort:", bubble_sort.arr)

# Selection Sort
selection_sort = SelectionSort(arr.copy())
selection_sort.sort()
print("Sorted array using Selection Sort:", selection_sort.arr)

# Insertion Sort
insertion_sort = InsertionSort(arr.copy())
insertion_sort.sort()
print("Sorted array using Insertion Sort:", insertion_sort.arr)
