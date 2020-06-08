nterm = int(input("Enter the range of fibonacci series: "))
n1 = 0
n2 = 1
count = 0
if nterm <= 0:
    print ("Enter positive number")
elif nterm == 1:
    print ("The fibonacci series of",nterm,"is: ")
    print(n1)
else:
    print ("The fibonacci series for range",nterm,"is: ")
    while count<nterm:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
