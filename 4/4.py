# Fibonacci recursive function

def Fibonacci(n):
    if n<=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)





# main boady
while True:
    num = int(input("Enter number: "))
    if num == -1:
        print("Exit")
        break                # exit from loop
    else:
       print(f"Fibonacci {num}: ", Fibonacci(num)) 
