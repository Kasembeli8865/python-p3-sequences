def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    
    print(fibonacci_sequence)

print_fibonacci(10)  # Prints the first 10 Fibonacci numbers
