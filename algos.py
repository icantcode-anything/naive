def greedyalgo():
    # for input lng to
    arrayofnum=[]
    rangeofunm=int(input('Please enter number of data: '))
    target=int(input('Please enter target number: '))
    
    for i in range(rangeofunm):
        number=int(input('Enter a data: '))
        arrayofnum.append(number)
   
    # mismong algo
    # in this case, nag add lng para makuha ung target, atleast alam na ung mismong logic
    result=[]
    arrayofnum.sort(reverse=True)
    for num in arrayofnum:
        while sum(result)+num <= target: #core function
            result.append(num)
    return result    

print(greedyalgo())

def bruteforcealgo():
    possiblepass=[1,2,3,4,5,6,7,8,9,0]
    passcode=[3,4,6,5]
    numoftries=0
    
    # in this case lng to, since fixed sa 4 lng un try
    for d1 in possiblepass:
        for d2 in possiblepass:
            for d3 in possiblepass:
                for d4 in possiblepass:
                    guess=[d1,d2,d3,d4]
                    numoftries+=1
                    if guess==passcode:
                        return numoftries

print("PASSWORD CRACKED\nTries:",bruteforcealgo())


def backtrackingalgo(start, files):
    # path = stack ,, stack lng ung path
    path=[start] 
    while path:
        current=path[-1]
        children=files.get(current,[])
        print(f'You are currently in File: {current}')
        print(f'File{current} Childs:{children}')

        if not children:
            print(f"File {current} does not have any files!")
            choice = input("Type BACK or EXIT: ").lower()
        else:
            choice = input("Choose child OR type BACK/EXIT: ").lower()

        if choice=='back':
                if len(path) == 1:
                    print("Already at root; can't go back further.") #kapag nagback kung nasa file 10 ka na
                else:
                    path.pop() #pagdelete kapag back
        elif choice=='exit':
            break
        else:
            try:
                child = int(choice)
                if child in children:
                    path.append(child)
                else:
                    print("Invalid choice, not a child of this file.")
            except ValueError:
                print("Invalid input, please type a number, BACK, or EXIT.")
files = {
10: [2, 5, 6, 7],
6: [3, 5, 1],
2: [],
5: [],
7: [],
3: [],
1: []
}
backtrackingalgo(10,files)