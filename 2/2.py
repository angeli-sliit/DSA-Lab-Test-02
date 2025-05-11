#recursion
def Multiply(M,n):
    if n == 1:
        return M
    else:
        return M + Multiply(M, n-1)



#main body
while True:
    M = int(input("Enter number M:"))
    if M == -1:
        print(" Exit the loop if M is -1")
        break;
    else:
      n = int(input("Enter number n:"))  
      print("Output: " , Multiply(M,n))      
