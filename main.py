
def fibonacci_iterative(n):
    n_1 = 0
    n_2 = 1
    print(n_1)
    print(n_2)

    for fibo in range(n - 2):
        n_3 = n_1 + n_2
        print(n_3)

        n_1 = n_2
        n_2 = n_3

def fibonacci_recursive(num, n_1=0, n_2=1):
    if num == 0:
        return n_1
    else:
        n_3 = n_1 + n_2
        print(n_1)
        return fibonacci_recursive(num - 1, n_2, n_3)

choice = int(input("// Choose an option:" +
      "\n[1]: iterative fibonacci" +
      "\n[2]: recursive fibonacci\n"))

if choice == 1:
    n = int(input("Enter a number: "))
    fibonacci_iterative(n)

if choice == 2:
    n = int(input("Enter a number: "))
    fibonacci_recursive(n)