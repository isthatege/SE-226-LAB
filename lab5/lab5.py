def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

exp_x_abs = lambda x, i: (x ** (2 * i)) / factorial(2 * i)

def exp_x_(x, n):
    total = 0
    for i in range(n):
        total += ((-1) ** i) * exp_x_abs(x, i)
    return total 

Gn_sum = 0
def Gn(n, r):
    global Gn_sum
    """This calculates G_n = 1 + r + r^2 + ... + r^{n-1} recursively.
    Takes n and r It's using Gn_sum to keep track of total. 
    Base case is n==0, does nothing then returns. 
    Otherwise it calls itself with n-1 and after returning adds r^(n-1) to Gn_sum."""
    if n == 0:
        return
    Gn(n - 1, r)
    Gn_sum += r ** (n - 1)

if __name__ == "__main__":
    x_val = float(input("Enter x: "))
    n_val = int(input("Enter n (number of terms for S): "))
    print(f"S = {exp_x_(x_val, n_val)}\n")

    r_val = float(input("Enter common ratio (r): "))
    n_gn = int(input("Enter highest power (n for Gn): "))

    Gn_sum = 0
    Gn(n_gn, r_val)
    print(f"Gn_sum = {Gn_sum}")