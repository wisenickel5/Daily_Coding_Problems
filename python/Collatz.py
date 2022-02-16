'''
Collatz Conjecture Probelm
'''

def collatz(n: int, count = 0):
    if (count >= 100):
        print(f"Collatz procedure exceeded {count}..")
        return False, 0

    if (n == 1): # Base Case
        count += 1
        return True, count

    elif (n % 2 == 0): # Number is even
        new_int = n / 2
        count += 1
        result, idx = collatz(new_int, count)
    elif(n % 2 != 0): # Number is odd
        new_int = (3 * n) + 1
        count += 1
        result, idx = collatz(new_int, count)

if __name__ == "__main__":
    result, count = collatz(10)
    print(f"{str(result)} {str(count)}")