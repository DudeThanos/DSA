def F(n):
    if n <= 1:
        print(n)
        return n
    else:
        k = F(n - 1) + F(n - 2)
        print(k)
        return k


print("Fibonacci Series")
print(F(6))
