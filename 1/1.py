#recursive function
def recursive(n):
    if n == 1:
        return 1
    return n+recursive(n-1)



#main boady
while True:
    number = int(input("Enter number: "))
    if number == -1:
        print("Output:Finished")
        break
    else:
        print("Output: ", recursive(number))
