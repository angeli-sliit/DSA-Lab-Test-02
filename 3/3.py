#recursive function
def recursive(s):
    if s == 1:
        return 2
    else:
        return recursive(s-1)/2



# main body
while True:
    num = int(input("Enter number: "))
    if num == -1:
        print("Output: Finished")
        break                          # exit loop
    else:
        print ("Output: ", recursive(num))    #print output
