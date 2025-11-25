# Python Algorithms Toolkit

A comprehensive Python project implementing all algorithms and concepts from the Computer Problem Solving course syllabus.

## 📚 Course Coverage

This project covers **all 6 units** from your syllabus:

### Unit 1: Introduction to Computer Problem Solving (8 hours)
- Algorithm efficiency analysis
- Time and space complexity evaluation
- Problem-solving methodology

### Unit 2: Python Data, Expressions and Statements (8 hours)
- Python interpreter and interactive mode
- Variables, expressions, and statements
- Tuple assignment and operator precedence
- Data types and type conversion

### Unit 3: Fundamental Algorithms & Control Flow (11 hours)
- **Algorithms**: Exchange values, counting, summation, factorial, Fibonacci, reverse, base conversion
- **Control Flow**: Conditionals (if-elif-else), iteration (while, for, break, continue, pass)
- **Functions**: Function definition, parameters, and arguments

### Unit 4: Factoring Methods (9 hours)
- Finding square root (Newton's method)
- Smallest divisor computation
- GCD (Greatest Common Divisor) - Euclidean algorithm
- Prime number generation (Sieve of Eratosthenes)
- Prime factorization
- Pseudo-random number generation
- Efficient power computation (exponentiation by squaring)
- nth Fibonacci number calculation

### Unit 5: Array Techniques & Python Lists (9 hours)
- Array order reversal
- Array counting operations
- Finding maximum and minimum
- Removing duplicates from ordered/unordered arrays
- Array partitioning
- Finding Kth smallest/largest element
- **Python Data Structures**:
  - Lists: operations and time complexity
  - Tuples: immutable sequences
  - Sets: operations (union, intersection, difference)
  - Dictionaries: key-value pairs with O(1) lookup

### Unit 6: Tools Required
- Python 3.x (main implementation language)
- Compatible with Scratch/Raptor concepts

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only standard library)

### Installation

1. Clone or download this project
2. Navigate to the project directory
3. Run the main program:

```bash
python python_algorithms_toolkit.py
```

## 📖 Usage Examples

### Running All Demonstrations

```bash
python python_algorithms_toolkit.py
```

This will execute demonstrations of all algorithms with sample inputs and outputs.

### Using Individual Functions

```python
from python_algorithms_toolkit import *

# Factorial calculation
result = factorial_iterative(5)
print(f"5! = {result}")  # Output: 5! = 120

# Fibonacci sequence
fib = fibonacci_sequence(10)
print(f"First 10 Fibonacci numbers: {fib}")

# GCD calculation
gcd_result = gcd_euclidean(48, 18)
print(f"GCD(48, 18) = {gcd_result}")  # Output: GCD(48, 18) = 6

# Prime generation
primes = generate_primes(50)
print(f"Primes up to 50: {primes}")

# Array operations
arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_val = find_maximum(arr)
kth = kth_smallest(arr, 3)
print(f"Maximum: {max_val}, 3rd smallest: {kth}")

# Data structure operations
list_demo = list_operations_demo()
set_demo = set_operations_demo()
dict_demo = dictionary_operations_demo()
```

## 🧮 Algorithm Implementations

### Unit 1: Problem Solving
- `analyze_algorithm_efficiency(arr)` - Analyzes sorting check with complexity

### Unit 2: Python Basics
- `demonstrate_python_basics()` - Shows variables, types, expressions, data structures

### Unit 3: Fundamental Algorithms
- `exchange_values(a, b)` - Swap two values
- `counting_sum(n)` - Sum 1 to n (iterative)
- `summation_formula(n)` - Sum 1 to n (formula)
- `factorial_iterative(n)` - Factorial (iterative)
- `factorial_recursive(n)` - Factorial (recursive)
- `fibonacci_sequence(n)` - Generate Fibonacci sequence
- `reverse_string(s)` - Reverse a string
- `reverse_array(arr)` - Reverse an array
- `base_conversion(num, from_base, to_base)` - Convert between number bases
- `character_to_number(char)` - ASCII conversion
- `number_to_character(num)` - ASCII to character

### Unit 3: Control Flow
- `conditional_example(x)` - If-elif-else demonstration
- `iteration_while(n)` - While loop example
- `iteration_for(n)` - For loop example

### Unit 4: Factoring Methods
- `find_square_root(n, precision)` - Newton's method for square root
- `smallest_divisor(n)` - Find smallest divisor > 1
- `gcd_euclidean(a, b)` - GCD using Euclidean algorithm
- `gcd_recursive(a, b)` - GCD recursive version
- `is_prime(n)` - Check if number is prime
- `generate_primes(n)` - Sieve of Eratosthenes
- `prime_factors(n)` - Prime factorization
- `pseudo_random(seed)` - Linear congruential generator
- `power_efficient(base, exp)` - Exponentiation by squaring
- `fibonacci_nth(n)` - Efficient nth Fibonacci

### Unit 5: Array Techniques
- `array_order_reversal(arr)` - Reverse array order
- `array_counting(arr, target)` - Count occurrences
- `find_maximum(arr)` - Find maximum element
- `find_minimum(arr)` - Find minimum element
- `remove_duplicates_ordered(arr)` - Remove duplicates (ordered)
- `remove_duplicates_unordered(arr)` - Remove duplicates (unordered)
- `partition_array(arr, pivot)` - Partition around pivot
- `kth_smallest(arr, k)` - Find Kth smallest
- `kth_largest(arr, k)` - Find Kth largest

### Unit 5: Python Data Structures
- `list_operations_demo()` - List operations with time complexities
- `tuple_operations_demo()` - Tuple operations (immutable)
- `set_operations_demo()` - Set operations (union, intersection, etc.)
- `dictionary_operations_demo()` - Dictionary with O(1) lookup

## 📊 Time Complexity Reference

| Operation | List | Tuple | Set | Dictionary |
|-----------|------|-------|-----|------------|
| Access by index | O(1) | O(1) | N/A | N/A |
| Access by key | N/A | N/A | N/A | O(1) |
| Append | O(1) | N/A | O(1) | O(1) |
| Insert | O(n) | N/A | O(1) | O(1) |
| Delete | O(n) | N/A | O(1) | O(1) |
| Search | O(n) | O(n) | O(1) | O(1) |
| Membership test | O(n) | O(n) | O(1) | O(1) |

## 🎯 Project Features

✅ **Complete syllabus coverage** - All units (1-6) implemented  
✅ **Clean, documented code** - Every function has docstrings  
✅ **Educational focus** - Clear algorithm explanations  
✅ **Production-ready** - Error handling and edge cases covered  
✅ **Performance optimized** - Efficient implementations (e.g., O(log n) power, Sieve for primes)  
✅ **Comprehensive testing** - Main function demonstrates all algorithms  
✅ **Type hints** - Modern Python typing for clarity  

## 📝 Code Quality

- **PEP 8 compliant** - Follows Python style guidelines
- **Modular design** - Each unit organized in separate sections
- **Comprehensive docstrings** - All functions documented
- **Type annotations** - Clear parameter and return types
- **Error handling** - Validates inputs and handles edge cases

## 🧪 Testing

Run the main program to see all algorithms in action:

```bash
python python_algorithms_toolkit.py
```

Expected output includes:
- Algorithm efficiency analysis
- Python basics demonstration
- Fundamental algorithm results
- Factoring method computations
- Array technique examples
- Data structure operation results

## 🎓 Learning Outcomes

After using this toolkit, you will understand:

1. **Algorithm design and analysis** - Problem-solving approaches
2. **Python fundamentals** - Data types, expressions, control flow
3. **Classic algorithms** - Factorial, Fibonacci, GCD, prime generation
4. **Optimization techniques** - Efficient power, square root, nth Fibonacci
5. **Data structures** - Lists, tuples, sets, dictionaries with time tradeoffs
6. **Array processing** - Searching, sorting, partitioning, kth element

## 📄 License

This is an educational project for coursework completion.

## 👨‍💻 Author

Student Project - VIT Bhopal  
Computer Problem Solving Course  
November 2025

## 🤝 Contributing

This is a course project. Feel free to:
- Study the implementations
- Modify for your own learning
- Add additional test cases
- Optimize algorithms further

## 📚 References

- Course syllabus: Units 1-6
- Python official documentation
- Classic algorithms and data structures textbooks
- Time complexity analysis resources

---

**Note**: This project demonstrates all required concepts from the 45-hour course syllabus (8+8+11+9+9 hours = 45 hours of content).
