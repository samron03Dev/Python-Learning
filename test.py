#https://docs.python.org/3/tutorial/

print("Choice 1: Variables")
print("Choice 2: Conditional Statements and Loops")
print("Choice 3: Functions")
print("Choice 4: Keyword Arguments")
print("Choice 5: Array Manipulation")
print("Choice 6: The Lambda Function")
print("Choice 7: Objects")
runChoice = int(input("Which section would you like to run? "))
print("")
#This is fascinating because when using input in Python, it always returns a string. Therefore, you can use int([YOUR STRING]) to make
#it an int

if runChoice==0:
    print("This is the testing area!")

elif runChoice==1:
    print("Let's do some exercises with variable assignments!")
    test_num = 50 #Normal Variable Syntax

    print(test_num)
    print("Hello!")
    print("This is how to use a \' in this without just making a new string or something!")

    myArr = [1,2,3,4,5] #Array Syntax

    print(myArr)

    myRevArr = myArr[::-1] #I think this is called slicing? It's lit it allows the program to work backwards through an array

    print(myRevArr)

    print(myRevArr[-2]) #This is the second index from the end. It should print 2
    print(myRevArr[3]) #This should also print 2
    print(myArr[1]) #This should also print 2

elif runChoice==2: #Unlike other languages where you use else if by typing that out, you just simply use elif in python
    print("Let's do some exercises using conditional things!")

    test_num = int(input("Put a number here: "))

    if test_num >= 0:
        #Unlike many other languages, you do not put parentheses after the if or elif, like how in JS or C++ you do if(...) {}
        #This means in Python, indentation is VERY important!
        print("Your number is at least 0!")
    else:
        print("You typed a negative number!")
    
    myArr = [1,2,3,4,5]

    for i in myArr:
        print(i) #This automatically does the work for you for tracking the indices of the array used in the loop

    print("")

    for i in range(5):
        print(myArr[i]) #This does the same thing but manually. Something that surprised me is that this does 0-4, not 1-5!

    print("")

    for i in range(0,5):
        print(myArr[i]) #This does the same thing but now with the lower bound set manually. Useless here but still worth learning!

    print("")

    for i in range(0,5,2):
        print(myArr[i]) #This now prints 1, 3, and 5 since it iterates by 2 instead of 1

    print("")

    print(sum(range(1,6))) #Utilizing both sum and range, you can make summations pretty easily. This does 1+2+3+4+5

    test_num = abs(int(input("Type a positive number! ")))

    while test_num >= 0:
        print(test_num)
        test_num -= 1

elif runChoice==3:
    print("Let's do some exercises using functions!")

    def hello_world(name):
        print("Hello world! My name is", name)

    myName = input("Type your name here: ")
    hello_world(myName)

    def fib_seq():
        fib_indices = int(input("Which index do you want to go until on the Fibonacci Sequence? "))
        fib_num = [0, 1]
        print(1, end=" ")
        for i in range(fib_indices - 1):
            temp = fib_num[0] + fib_num[1]
            print(temp, end=" ")
            fib_num[0] = fib_num[1]; fib_num[1] = temp
        print("")

    fib_seq()

    def emp_id(name, id=1, salary=50000):
        #This is cool because it makes it so that you can leave default values in the functions
        #You then only have to fill in what is required. In this case, the name
        print(name); print(id); print("$", salary, sep="")

    emp_id("Samuel")
    emp_id("Tyrone", salary=10000)
    #You can also fill in some of the ones that have defaults. If you want to skip one, you can target the one you're not skipping

elif runChoice==4: #This is for keyword arguments. Study this more
    #https://docs.python.org/3/tutorial/controlflow.html
    #There's tons of stuff at this link starting from 4.9.2 and later
    pass

elif runChoice==5:
    print("Let's do some exercises using array manipulation!")
    myArr = [1,2,3,4,5,6,7,8,9,10]

    print(len(myArr)) #This is a simple way to extract the length of myArr

    print(4 in myArr) #This is a simple way to see if an array includes something

    myArr.append(11) #This adds whatever is inputted as the parameter at the end of the array
    print(myArr)
    myArr[len(myArr):] = [12] #This also does the same thing!
    print(myArr)

    testArr = [-1,-2,-3]
    myArr.extend(testArr) #This adds the values of testArr at the end of myArr
    print(myArr)

    myArr.insert(0, -1) #This adds a value at the specific index. This adds -1 at the first index and then shifts everything else
    print(myArr)

    myArr.remove(-1) #This removes the first instance of this value (-1 in this case)
    #This means the second -1 in this array is left untouched
    print(myArr)

    myArr.pop(11) #This removes the element at that specific index
    print(myArr)

    print(testArr)
    testArr.clear() #This clears the contents of the array
    print(testArr)

    myArr.insert(0, -1)
    print(myArr.index(-1)) #This yields the first occurence of what the parameter
    print(myArr.index(-1, 10, len(myArr)-1)) #This also allows you to put 2 extra parameters showing the start and stop for your search
    #This makes it so that you can only search a specific section of the array
    print(myArr.index(-1, 10)) #You also only have to put the start of your search parameter if you'd like

    print(myArr.count(1)) #This yields the amount of times something appears in the array
    print(myArr.count(0))
    print(myArr.count(-1))

    testArr = [1, 3, 2, 10, 0]
    print(sorted(testArr)) #This prints the sorted array without actually changing the array itself
    testArr.sort() #This sorts the array and actually does affect the contents of the array
    #This is not to be confused with testArr[::-1] as that reverses the order of the current contents of the array, but does not sort it
    print(testArr)
    testArr.sort(reverse=True) #This sorts the array in reverse order
    print(testArr)

    testArr.reverse() #This of course reverses the contents of the array
    #This DOES do the same thing as testArr[::-1], except that testArr[::-1] does not change the array
    #testArr.reverse() is the exact same thing as testArr = testArr[::-1]. testArr.reverse() is more effecient though as a function

    print(myArr.copy()) #This creates a shallow copy of the array. Meaning it does not assign it to anything on its own
    print(myArr[:]) #This does the exact same thing as the copy function
    #Unlike the reverse function and doing [::-1], the copy function and [:] are exactly the same thing both functionally
    #and performance wise

elif runChoice==6:
    print("Let's do some exercises using the lambda function!")

    myArr = [1,2,3,4,5,6,7,8,9,10]

    oddArr = list(filter(lambda x: x%2==1, myArr))
    print(oddArr)

    squaredArr = map(lambda x: x*2, myArr) #This will only save the lazy evaluation
    #This is essentially the saved result that hasn't been used yet
    print(squaredArr)
    print(list(squaredArr))

    lastLetterArr = ["Chad", "Blob", "Lambda", "Almanac"]
    lastLetterArr.sort(key=lambda x: x[-1]) #This is a way to sort this array by the last letters only
    print(lastLetterArr)

elif runChoice==7:
    print("Let's do some exercises using objects!")