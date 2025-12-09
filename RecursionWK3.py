## Develop both a recursive and an iterative algorithm to calculate the N-th Fibonacci number, F(N).
## Compare their time complexities. The Fibonacci sequence is defined as F(N+2) = F(N) + (FN+1), with F(1) = F(2) = 1.
## Note that F(1) and F(2) are defined as 0 and 1 respectively in certain literature.

from random import sample

class Recursion:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1,3 * self.max_size), self.max_size)

    def print_all(self):
        print("The size of the random array is: ", str(len(self.data)))
        print("Before sorting, the array is " + str(self.data))

    def fib_iterative(self, n):
        if n < 1:
            raise ValueError("n should be a positive integer.")
        f1 = f2 = 1
        out = -1
        if n == 1 or n == 2:
            return f1
        for i in range(3, n + 1):
            out = f1 + f2
            f1 = f2
            f2 = out
            print("The " + str(i) + "-th Fibonacci number is: " + str(out))
        return out
    
    def fib_recursive(self, n):
        if n <1:
            raise ValueError("n should be a positive integer.")
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)
    
    # Compute the greatest common divisor (GCD) of two positive integers n and m using recursion
        
    def gcd(self, n, m):
        if n == m:
            return n
        elif n < m:
            return self.gcd(m-n,n)
        else:
            return self.gcd(n-m,m)
        
    # Merge sort implementation

    def merge_sort(self):
        #arr has to be sorted array
        self._merge_sort(self.data, 0, len(self.data)-1)
        print("After the merge sort the array is " + str(self.data))


    def _merge_sort(self, arr, start, end):
        if start >= end:
            return
        mid = (end - start) // 2 + start
        self._merge_sort(arr,start,mid)
        self._merge_sort(arr,mid+1,end)
        # merge the two sorted sub-arrays
        self._merge(arr,start,mid,end)

    def _merge(self, arr, start, mid, end):
        temp = []
        p1 = start
        p2 = mid + 1
        # Compare the first elements in two sub-arrays (referenced by p1 and p2 respectively), the smaller one is first inserted to the new array
        while p1 <= mid and p2 <= end:
            if arr[p1] <= arr[p2]:
                temp.append(arr[p1])
                p1 += 1
            else:
                temp.append(arr[p2])
                p2 += 1
        #When one sub-array is exhausted, the remaining elements of theother sub-array will be copied to the new array - only 1 of the following2while loops will be executed
        while p1 <= mid:
            temp.append(arr[p1])
            p1 += 1
        while p2 <= end:
            temp.append(arr[p2])
            p2 += 1
        #Update the original array
        for i in range(len(temp)):
            arr[start + i] = temp[i]

    def quick_sort(self):
        self._quick_sort(self.data, 0, len(self.data)-1)
        print("After the quick sort the array is " + str(self.data))
    
    def _quick_sort(self, arr, start, end):
        if start < end:
            #after the partition, pivot is in its final correct position
            pivot = self._partition(arr, start, end)
            self._quick_sort(arr, start, pivot - 1)
            self._quick_sort(arr, pivot + 1, end)

    def _partition(self, arr, start, end):
        # we  choose the last element as the pivot
        pivot = arr[end]
        i = start
        for j in range(start,end):
            if arr[j] < pivot:
                # swap the element smaller than the pivot anmd the element larger than the pivot - the swapped one with a smalelr value has a larger index
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
                # now swap the pivot to its final correct position - smaller than right half, larger than left half
        arr[end], arr[i] = arr[i], arr[end]
        return i
    
    # checks if a input is a palindrome (same forwards as backwards, racecar)

    def palindrome(self, s):
        if len(s) == 0 or len(s) ==1:
            return True
        elif s[0] != s[len(s)-1]:
            print("The first is " +s[0])
            print("The last is " +s[len(s)-1])
            # not a palindrome
            return False
        else:
            #noting the substring returns the interval with an open interval [start,end]
            return self.palindrome(s[1:len(s)-1])



arr = Recursion()
arr.fib_iterative(10)
print(arr.fib_recursive(10))

print("The greatest common divisor is " + str(arr.gcd(27,18)))
print("The greatest common divisor is " + str(arr.gcd(28,19)))

arr.initialise()
arr.print_all()
arr.merge_sort()

arr.initialise()
arr.print_all()
arr.quick_sort()

str1 = "!_asddsa_!"
print("The string " + str1 + " is palindrome? --- " +str(arr.palindrome(str1)))
str2 = "aaa"
print("The string " + str2 + " is palindrome? --- " +str(arr.palindrome(str2)))
str3 = "abcdba"
print("The string " + str3 + " is palindrome? --- " +str(arr.palindrome(str3)))

# manually add numbers

arr1 = Recursion()
arr1.data = [1,4,2,5,3]
arr1.print_all()
arr1.merge_sort()

