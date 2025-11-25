"""
Python Algorithms Toolkit
A comprehensive collection of algorithms covering all syllabus units:
- Unit 1: Introduction to Computer Problem Solving
- Unit 2: Python Data, Expressions and Statements
- Unit 3: Fundamental Algorithms & Control Flow
- Unit 4: Factoring Methods
- Unit 5: Array Techniques & Python Lists

Author: Student Project
Date: November 2025
"""

import math
from typing import List, Tuple, Any


# ============================================================================
# UNIT 1: INTRODUCTION TO COMPUTER PROBLEM SOLVING
# ============================================================================

def analyze_algorithm_efficiency(arr: List[int]) -> dict:
    """
    Analyzes the efficiency of checking if an array is sorted.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    n = len(arr)
    comparisons = 0
    is_sorted = True

    for i in range(n - 1):
        comparisons += 1
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break

    return {
        'is_sorted': is_sorted,
        'comparisons': comparisons,
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)'
    }


# ============================================================================
# UNIT 2: PYTHON DATA, EXPRESSIONS AND STATEMENTS
# ============================================================================

def demonstrate_python_basics():
    """
    Demonstrates Python interpreter, values, types, variables, expressions,
    statements, tuple assignment, precedence of operators, and comments.
    """
    # Variables and types
    integer_var = 42
    float_var = 3.14
    string_var = "Hello, Python!"
    boolean_var = True

    # Tuple assignment
    x, y, z = 10, 20, 30

    # Expressions and operator precedence
    result = 2 + 3 * 4 ** 2  # Power first, then multiplication, then addition

    # List, tuple, set, dictionary
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3, 3, 2}  # Duplicates removed
    my_dict = {'name': 'Python', 'version': 3.9}

    return {
        'variables': (integer_var, float_var, string_var, boolean_var),
        'tuple_assignment': (x, y, z),
        'precedence_result': result,
        'data_structures': {
            'list': my_list,
            'tuple': my_tuple,
            'set': my_set,
            'dict': my_dict
        }
    }


# ============================================================================
# UNIT 3: FUNDAMENTAL ALGORITHMS & CONTROL FLOW
# ============================================================================

def exchange_values(a: Any, b: Any) -> Tuple[Any, Any]:
    """Exchange two values using tuple assignment."""
    a, b = b, a
    return a, b


def counting_sum(n: int) -> int:
    """Calculate sum from 1 to n using iteration."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def summation_formula(n: int) -> int:
    """Calculate sum from 1 to n using mathematical formula."""
    return n * (n + 1) // 2


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of n iteratively.
    n! = n × (n-1) × (n-2) × ... × 1
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Calculate factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate Fibonacci sequence up to n terms.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def reverse_array(arr: List) -> List:
    """Reverse an array/list."""
    return arr[::-1]


def base_conversion(number: str, from_base: int, to_base: int) -> str:
    """
    Convert a number from one base to another.
    First converts to decimal, then to target base.
    """
    # Convert from source base to decimal
    decimal = int(number, from_base)

    # Convert from decimal to target base
    if to_base == 10:
        return str(decimal)

    if decimal == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base

    return result


def character_to_number(char: str) -> int:
    """Convert a character to its ASCII number."""
    return ord(char)


def number_to_character(num: int) -> str:
    """Convert an ASCII number to its character."""
    return chr(num)


# ============================================================================
# UNIT 3: PYTHON CONTROL FLOW & FUNCTIONS
# ============================================================================

def conditional_example(x: int) -> str:
    """Demonstrate if-elif-else conditionals."""
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"


def iteration_while(n: int) -> List[int]:
    """Demonstrate while loop - generate numbers from 1 to n."""
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i += 1
    return result


def iteration_for(n: int) -> List[int]:
    """Demonstrate for loop - generate numbers from 1 to n."""
    return [i for i in range(1, n + 1)]


# ============================================================================
# UNIT 4: FACTORING METHODS
# ============================================================================

def find_square_root(n: float, precision: float = 0.0001) -> float:
    """
    Find square root using Newton's method (Babylonian method).
    x_new = (x_old + n/x_old) / 2
    """
    if n < 0:
        raise ValueError("Cannot find square root of negative number")
    if n == 0:
        return 0

    x = n
    while True:
        root = (x + n / x) / 2
        if abs(root - x) < precision:
            return root
        x = root


def smallest_divisor(n: int) -> int:
    """
    Find the smallest divisor of n (greater than 1).
    """
    if n < 2:
        return n

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


def gcd_euclidean(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    GCD(a, b) = GCD(b, a mod b)
    """
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a: int, b: int) -> int:
    """Calculate GCD recursively."""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(n: int) -> List[int]:
    """
    Generate all prime numbers up to n using Sieve of Eratosthenes.
    """
    if n < 2:
        return []

    # Create a boolean array and initialize all entries as true
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    p = 2
    while p * p <= n:
        if is_prime_arr[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, n + 1, p):
                is_prime_arr[i] = False
        p += 1

    return [i for i in range(n + 1) if is_prime_arr[i]]


def prime_factors(n: int) -> List[int]:
    """
    Compute prime factors of n.
    """
    if n < 2:
        return []

    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


def pseudo_random(seed: int) -> float:
    """
    Generate pseudo-random number using Linear Congruential Generator.
    Formula: (a * seed + c) mod m
    """
    a = 9301
    c = 49297
    m = 233280
    return ((a * seed + c) % m) / m


def power_efficient(base: float, exp: int) -> float:
    """
    Raise a number to a large power efficiently using exponentiation by squaring.
    Time Complexity: O(log n)
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power_efficient(base, -exp)

    if exp % 2 == 0:
        half = power_efficient(base, exp // 2)
        return half * half
    else:
        return base * power_efficient(base, exp - 1)


def fibonacci_nth(n: int) -> int:
    """
    Compute nth Fibonacci number efficiently using iteration.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ============================================================================
# UNIT 5: ARRAY TECHNIQUES
# ============================================================================

def array_order_reversal(arr: List) -> List:
    """Reverse the order of an array."""
    return arr[::-1]


def array_counting(arr: List, target: Any) -> int:
    """Count occurrences of target in array."""
    return arr.count(target)


def find_maximum(arr: List[int]) -> int:
    """Find the maximum number in an array."""
    if not arr:
        raise ValueError("Array is empty")
    return max(arr)


def find_minimum(arr: List[int]) -> int:
    """Find the minimum number in an array."""
    if not arr:
        raise ValueError("Array is empty")
    return min(arr)


def remove_duplicates_ordered(arr: List) -> List:
    """
    Remove duplicates from an ordered array while maintaining order.
    """
    if not arr:
        return []

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result


def remove_duplicates_unordered(arr: List) -> List:
    """
    Remove duplicates from an array (order may not be preserved).
    """
    return list(set(arr))


def partition_array(arr: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    """
    Partition array into three parts: less than pivot, equal to pivot, greater than pivot.
    """
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return less, equal, greater


def kth_smallest(arr: List[int], k: int) -> int:
    """
    Find the Kth smallest element in array (1-indexed).
    """
    if k < 1 or k > len(arr):
        raise ValueError("K is out of range")

    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]


def kth_largest(arr: List[int], k: int) -> int:
    """
    Find the Kth largest element in array (1-indexed).
    """
    if k < 1 or k > len(arr):
        raise ValueError("K is out of range")

    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[k - 1]


# ============================================================================
# UNIT 5: PYTHON LISTS - DATA STRUCTURES & TIME TRADEOFFS
# ============================================================================

def list_operations_demo() -> dict:
    """
    Demonstrate Python list operations and their time complexities.
    """
    my_list = [1, 2, 3, 4, 5]

    # Append: O(1) average
    my_list.append(6)

    # Insert at beginning: O(n)
    my_list.insert(0, 0)

    # Remove: O(n)
    my_list.remove(3)

    # Pop: O(1)
    last = my_list.pop()

    # Access by index: O(1)
    element = my_list[2]

    # Search: O(n)
    exists = 4 in my_list

    return {
        'final_list': my_list,
        'popped_element': last,
        'accessed_element': element,
        'search_result': exists,
        'time_complexities': {
            'append': 'O(1)',
            'insert_beginning': 'O(n)',
            'remove': 'O(n)',
            'pop': 'O(1)',
            'access': 'O(1)',
            'search': 'O(n)'
        }
    }


def tuple_operations_demo() -> dict:
    """
    Demonstrate Python tuple operations.
    Tuples are immutable - cannot be changed after creation.
    """
    my_tuple = (1, 2, 3, 4, 5)

    # Access: O(1)
    element = my_tuple[2]

    # Search: O(n)
    exists = 3 in my_tuple

    # Count: O(n)
    count = my_tuple.count(3)

    # Slicing: O(k) where k is slice size
    slice_tuple = my_tuple[1:4]

    return {
        'tuple': my_tuple,
        'accessed_element': element,
        'search_result': exists,
        'count': count,
        'slice': slice_tuple,
        'properties': 'Immutable, faster than lists for read operations'
    }


def set_operations_demo() -> dict:
    """
    Demonstrate Python set operations and their time complexities.
    Sets are unordered collections with no duplicates.
    """
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Add: O(1) average
    set1.add(6)

    # Remove: O(1) average
    set1.discard(2)

    # Union: O(len(set1) + len(set2))
    union = set1 | set2

    # Intersection: O(min(len(set1), len(set2)))
    intersection = set1 & set2

    # Difference: O(len(set1))
    difference = set1 - set2

    # Membership test: O(1) average
    exists = 3 in set1

    return {
        'set1': set1,
        'set2': set2,
        'union': union,
        'intersection': intersection,
        'difference': difference,
        'membership': exists,
        'time_complexities': {
            'add': 'O(1)',
            'remove': 'O(1)',
            'membership': 'O(1)',
            'union': 'O(m+n)',
            'intersection': 'O(min(m,n))'
        }
    }


def dictionary_operations_demo() -> dict:
    """
    Demonstrate Python dictionary operations and their time complexities.
    Dictionaries are key-value pairs with fast lookup.
    """
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Insert/Update: O(1) average
    my_dict['d'] = 4
    my_dict['b'] = 20

    # Access: O(1) average
    value = my_dict.get('c', 0)

    # Delete: O(1) average
    deleted = my_dict.pop('a', None)

    # Membership test: O(1) average
    exists = 'b' in my_dict

    # Get all keys/values: O(n)
    keys = list(my_dict.keys())
    values = list(my_dict.values())

    return {
        'dictionary': my_dict,
        'accessed_value': value,
        'deleted_value': deleted,
        'membership': exists,
        'keys': keys,
        'values': values,
        'time_complexities': {
            'insert': 'O(1)',
            'access': 'O(1)',
            'delete': 'O(1)',
            'membership': 'O(1)',
            'iteration': 'O(n)'
        }
    }


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def main():
    """Main function demonstrating all algorithms."""
    print("=" * 80)
    print("PYTHON ALGORITHMS TOOLKIT - COMPREHENSIVE SYLLABUS COVERAGE")
    print("=" * 80)

    # Unit 1: Algorithm Analysis
    print("\n[UNIT 1: ALGORITHM EFFICIENCY ANALYSIS]")
    arr = [1, 2, 3, 4, 5]
    analysis = analyze_algorithm_efficiency(arr)
    print(f"Array: {arr}")
    print(f"Analysis: {analysis}")

    # Unit 2: Python Basics
    print("\n[UNIT 2: PYTHON DATA & EXPRESSIONS]")
    basics = demonstrate_python_basics()
    print(f"Tuple assignment: {basics['tuple_assignment']}")
    print(f"Operator precedence result: {basics['precedence_result']}")

    # Unit 3: Fundamental Algorithms
    print("\n[UNIT 3: FUNDAMENTAL ALGORITHMS]")
    print(f"Factorial(5): {factorial_iterative(5)}")
    print(f"Fibonacci(10): {fibonacci_sequence(10)}")
    print(f"Reverse 'Python': {reverse_string('Python')}")
    print(f"Binary 1010 to Decimal: {base_conversion('1010', 2, 10)}")
    print(f"Sum 1 to 100: {summation_formula(100)}")

    # Unit 4: Factoring Methods
    print("\n[UNIT 4: FACTORING METHODS]")
    print(f"Square root of 16: {find_square_root(16)}")
    print(f"Smallest divisor of 15: {smallest_divisor(15)}")
    print(f"GCD(48, 18): {gcd_euclidean(48, 18)}")
    print(f"Primes up to 30: {generate_primes(30)}")
    print(f"Prime factors of 60: {prime_factors(60)}")
    print(f"Power 2^10: {power_efficient(2, 10)}")

    # Unit 5: Array Techniques
    print("\n[UNIT 5: ARRAY TECHNIQUES]")
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"Original array: {test_arr}")
    print(f"Maximum: {find_maximum(test_arr)}")
    print(f"Minimum: {find_minimum(test_arr)}")
    print(f"3rd smallest: {kth_smallest(test_arr, 3)}")
    print(f"Remove duplicates: {remove_duplicates_unordered(test_arr)}")
    print(f"Reversed: {array_order_reversal(test_arr)}")

    # Unit 5: Python Lists & Data Structures
    print("\n[UNIT 5: PYTHON DATA STRUCTURES & TIME TRADEOFFS]")
    list_ops = list_operations_demo()
    print(f"List operations: {list_ops['final_list']}")

    tuple_ops = tuple_operations_demo()
    print(f"Tuple: {tuple_ops['tuple']} (Immutable)")

    set_ops = set_operations_demo()
    print(f"Set union: {set_ops['union']}")
    print(f"Set intersection: {set_ops['intersection']}")

    dict_ops = dictionary_operations_demo()
    print(f"Dictionary: {dict_ops['dictionary']}")

    print("\n" + "=" * 80)
    print("All algorithms executed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
