# Bubble sort function
def BubbleSort(input_array):
    x = len(input_array)

    for i in range(x):


        # Output the steps one by one
        print("")
        print(str(i+1) + ". " + str(input_array))

    
        # Bubble sorting algorithm
        for j in range(0, x-i-1):
            if input_array[j] > input_array[j+1]:
                print("The number " + str(input_array[j]) + " is greater than " + str(input_array[j+1]))
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

# Selection sort function               
def SelectionSort(input_array):

    x = len(input_array)
    temp_array = []


    print("1. " + str(input_array))


    # Selection sorting algorithm
    for i in range(x-1):
        iminimum = i


        for j in range(i+1, x):

            if input_array[j] < input_array[iminimum]:
                print(str(input_array[j]) + " is less than " + str(input_array[iminimum]))
                iminimum = j
    

        temp_array = input_array[i]
        input_array[i] = input_array[iminimum]
        input_array[iminimum] = temp_array

        print("")
        print(str(i+2) + ". " + str(input_array))


# Insertion sort function
def InsertionSort(input_array):
    x = len(input_array)

    for i in range(1, x):

        print(str(i) + ". " + str(input_array))


        for j in range(i-1, -1, -1):
        

            if input_array[j] > input_array[j+1]:
                print(str(input_array[j]) + " is greater than " + str(input_array[j+1]))
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
            else:
                break
            

            print("")
            print(str(x) + ". " + str(input_array))


# Merge Sort function
def MergeSort(input_array):

    count = 0

    if len(input_array)>1:
        mid = len(input_array)//2
        lefthalf = input_array[:mid]
        righthalf = input_array[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0
        count = count + 1
     

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                input_array[k]=lefthalf[i]
                i=i+1
            else:
                input_array[k]=righthalf[j]
                j=j+1
            k=k+1
            
           

        while i < len(lefthalf):
            input_array[k]=lefthalf[i]
            i=i+1
            k=k+1
            

        while j < len(righthalf):
            input_array[k]=righthalf[j]
            j=j+1
            k=k+1
        
    print(str(count+1) + ". " + str(input_array))
    


# Quick Sort algorithm    
def QuickSort(input_array):
    quick_sort(input_array,0, len(input_array)-1)

def quick_sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort(A, low, p)
        quick_sort(A, p+1, high)

def partition(A, low, high):
    pivot = A[low]
    i, j = low - 1, high + 1


    while True:
        i += 1
        j -= 1
        

        while(A[i] < pivot): i += 1
        while(A[j] > pivot): j -= 1


        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]
        
        print(str(input_array))



#SHELL SORT
def ShellSort(sample):
    print("1. " + str(sample))
    length = len(sample)
    a = 1
    gap = int(length/2)
    while(gap >= 1):
        i = gap
        a+=1
        while(i < length):
            value = sample[i]
            j = i
            while(j-gap >= 0 and value < sample[j - gap]):
                sample[j] = sample[j - gap]
                j -= gap
            sample[j] = value
            i+=1
        gap = int(gap/2)
        print(str(a) + ". " + str(sample))

#Radix Sort
def counting(input_array, place):
    x = len(input_array)
    output = [0] * x
    count = [0] * 10
    for i in range (0, x):
        index = input_array[i] // place
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = x - 1
    
    while i >= 0:
        index = input_array[i] // place
        output[count[index % 10] - 1] = input_array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0,x):
        input_array[i] = output[i]

def RadixSort(input_array):
    counter = 1
    maximum = max(input_array)
    place = 1

    print("1. " + str(input_array))

    while maximum // place > 0:
        counter += 1
        counting(input_array, place)
        place *= 10
        print(str(counter) + ". " + str(input_array))
            

# Heap Sort
def swap(i, j):                    
    input_array[i], input_array[j] = input_array[j], input_array[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and input_array[i] < input_array[l]:   
        max = l   
    if r < end and input_array[max] < input_array[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def HeapSort(input_array):     
    count = 0
    end = len(input_array)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):
        count = count + 1
        swap(i, 0)   
        heapify(i, 0)   
        print(str(count) + ". " + str(input_array))
    
                
        

#######QUIZ ALGORITHMS#########
# Bubble sort function
def BubbleSort_quiz(input_array):
    x = len(input_array)
    inputAnswers = []

    for i in range(x):

        print("")

        inputAnswers.clear()

        for z in range(x):
            inputAnswers.append(int(input("Using bubble sort, enter the correct number for position " + str(z) + " in this array: ")))
        
        # Determining whether or not the user is correct
        if inputAnswers == input_array:
            print("")
            print("Nice! You got the step " + str(i+1) + " correct")

        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get the next step correct!")


        # Output the steps one by one
        print("")
        print(str(i+1) + ". " + str(input_array))

    
        # Bubble sorting algorithm
        for j in range(0, x-i-1):
            if input_array[j] > input_array[j+1]:
                print("The number " + str(input_array[j]) + " is greater than " + str(input_array[j+1]))
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
                
                      

# Selection sort quiz            
def SelectionSort_quiz(input_array):

    x = len(input_array)
    temp_array = []
    inputAnswers = []

    # Only for the first step of selection sort
    for z in range(0, x):
        inputAnswers.append(int(input("Using selection sort, enter the correct number for index " + str(z) + " in this array ")))

    print("")
    if inputAnswers == input_array:
        print("Nice! You got step 1 correct")
        print("")
    
    elif inputAnswers != input_array:
        print("Sorry, that is the wrong answer. Try to get the next step correct!")
        print("")

    print("1. " + str(input_array))


    # Selection sorting algorithm
    for i in range(x-1):
        iminimum = i

        inputAnswers.clear()

        for j in range(i+1, x):

            if input_array[j] < input_array[iminimum]:
                print(str(input_array[j]) + " is less than " + str(input_array[iminimum]))
                iminimum = j

        print("")
        for b in range(x):
            inputAnswers.append(int(input("Using selection sort, enter the correct number for index " + str(b) + " in this array ")))
        

        temp_array = input_array[i]
        input_array[i] = input_array[iminimum]
        input_array[iminimum] = temp_array

        if inputAnswers == input_array:
            print("")
            print("Nice! You got step " + str(i+2) + " correct")
    
        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get the next step correct!")

        

        print("")
        print(str(i+2) + ". " + str(input_array))


# Insertion sort function
def InsertionSort_quiz(input_array):
    x = len(input_array)
    inputAnswers = []

    for i in range(1, x):

        print("")

        inputAnswers.clear()

        for z in range(x):
             inputAnswers.append(int(input("Using insertion sort, enter the correct number for position " + str(z+1)+ " in the array ")))

        if inputAnswers == input_array:
            print("")
            print("Nice! You got step " + str(i) + " correct")

        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get it correct next time!")

        print("")
        print(str(i) + ". " + str(input_array))


        for j in range(i-1, -1, -1):
        

            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
            else:
                break
            
        if i == x-1:
            print("")

            inputAnswers.clear()

            for z in range(x):
                inputAnswers.append(int(input("Using insertion sort, enter the correct number for position " + str(z+1)+ " in the array ")))

            if inputAnswers == input_array:
                print("")
                print("Nice! You got step " + str(i+1) + " correct")

            elif inputAnswers != input_array:
                print("")
                print("Sorry, that is the wrong answer. Try to get it correct next time!")


            print("")
            print(str(x) + ". " + str(input_array))



# Shell Sort Quiz 
def ShellSort_quiz(input_array):
    inputAnswers = []

    length = len(input_array)

    for i in range(0, length):
        inputAnswers.append(int(input("Using shell sort, enter the correct number for index " + str(i) + " in this array: ")))
    
    if inputAnswers == input_array:
        print("")
        print("Nice! You got step 1 correct")

    elif inputAnswers != input_array:
        print("")
        print("Sorry, that is the wrong answer. Try to get it correct next time!")

    inputAnswers.clear()

    print("")
    print("1. " + str(input_array))

    
    a = 1
    gap = int(length/2)
    while(gap >= 1):
        i = gap
        a+=1
        while(i < length):
            value = input_array[i]
            j = i
            while(j-gap >= 0 and value < input_array[j - gap]):
                input_array[j] = input_array[j - gap]
                j -= gap
            input_array[j] = value
            i+=1
        gap = int(gap/2)

        print("")
        for b in range(0, length):
            inputAnswers.append(int(input("Using shell sort, enter the correct number for index " + str(b) + " in this array: ")))

        if inputAnswers == input_array:
            print("")
            print("Nice! You got step " + str(a) + " correct")
        
        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get it correct next time!")
        
        inputAnswers.clear()

        print("")
        print(str(a) + ". " + str(input_array))


# Radix Sort Quiz
def counting_quiz(input_array, place):
    x = len(input_array)
    output = [0] * x
    count = [0] * 10
    for i in range (0, x):
        index = input_array[i] // place
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = x - 1
    
    while i >= 0:
        index = input_array[i] // place
        output[count[index % 10] - 1] = input_array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0,x):
        input_array[i] = output[i]

def RadixSort_quiz(input_array):
    x = len(input_array)
    inputAnswers = []
    counter = 1
    maximum = max(input_array)
    place = 1

    for i in range (0,x):
        inputAnswers.append(int(input("Using radix sort, enter the correct number for index " + str(i) + " in this array: ")))

    if inputAnswers == input_array:
        print("")
        print("Nice! You got step 1 correct")
    
    elif inputAnswers != input_array:
        print("")
        print("Sorry, that is the wrong answer. Try to get it correct next time!")

    print("")
    print("1. " + str(input_array))

    inputAnswers.clear()

    while maximum // place > 0:
        counter += 1
        counting(input_array, place)
        place *= 10

        print("")
        for i in range (0,x):
            inputAnswers.append(int(input("Using radix sort, enter the correct number for index " + str(i) + " in this array: ")))

        if inputAnswers == input_array:
            print("")
            print("Nice! You got step " + str(counter) + " correct")
    
        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get it correct next time!")

        print("")
        print(str(counter) + ". " + str(input_array))

        inputAnswers.clear()


# Heap Sort Quiz
def swap_quiz(i, j):                    
    input_array[i], input_array[j] = input_array[j], input_array[i] 

def heapify_quiz(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and input_array[i] < input_array[l]:   
        max = l   
    if r < end and input_array[max] < input_array[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def HeapSort_quiz(input_array):     
    count = 0
    inputAnswers = []
    end = len(input_array)   
    start = end // 2 - 1 

    for b in range (0, end):
        inputAnswers.append(int(input("Using heap sort, enter the correct number for index " + str(b) + " in this array: ")))

    if inputAnswers == input_array:
        print("")
        print("Nice! You got step 1 correct")
    
    elif inputAnswers != input_array:
        print("")
        print("Sorry, that is the wrong answer. Try to get it correct next time!")
    
    print("")
    print("1. " + str(input_array))

    inputAnswers.clear()


    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):
        count = count + 1
        swap(i, 0)   
        heapify(i, 0)

        print("")
        for a in range (0, end):
            inputAnswers.append(int(input("Using heap sort, enter the correct number for index " + str(a) + " in this array: ")))

        if inputAnswers == input_array:
            print("")
            print("Nice! You got step " + str(count + 1) + " correct")
    
        elif inputAnswers != input_array:
            print("")
            print("Sorry, that is the wrong answer. Try to get it correct next time!")

        inputAnswers.clear()

        print("")
        print(str(count + 1) + ". " + str(input_array))

    
# Initializing/declaring arrays
input_array = []
temp_array = []


############QUIZ##############
print("Hello! Welcome to Sorting Algorithms tutorial")
quiz_input = str(input("Do you want to quiz yourself? (Enter yes to get a quiz and enter no to get a tutorial) "))

if quiz_input in ['Yes', 'yes']:
    print("|---------------------------------------------------------------------------------|")
    print("|Bubble Sort, Selection Sort, Insertion Sort, Shell Sort, Radix Sort, or Heap Sort|")
    print("|---------------------------------------------------------------------------------|")
    print("")
    algorithms = str(input("Which sorting algorithm do you want to quiz yourself? "))
    numbers_amount = int(input("How many numbers do you want to be sorted? "))

    for a in range(numbers_amount):
        input_array.append(int(input("Enter a number: ")))
        temp_array = input_array.copy()
    
    print("-----------------------------------")
    
    if algorithms in ['Bubble Sort' , 'bubble sort', 'Bubble sort', 'bubble Sort', 'bubble', 'Bubble']:
        BubbleSort_quiz(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Selection Sort', 'Selection sort', 'selection sort', 'selection Sort', 'Selection', 'selection']: 
        SelectionSort_quiz(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Insertion Sort', 'Insertion sort', 'insertion sort', 'insertion Sort', 'Insertion', 'insertion']:
        InsertionSort_quiz(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array)) 
    
    elif algorithms in ['Shell Sort', 'Shell sort', 'shell sort', 'shell Sort', 'shell', 'Shell']:
        ShellSort_quiz(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Radix Sort', 'Radix sort', 'radix sort', 'radix Sort', 'radix', 'Radix']:
        RadixSort_quiz(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Heap Sort', 'Heap sort', 'heap sort', 'heap Sort', 'heap', 'Heap']:
        HeapSort_quiz(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))
       


###############TUTORIAL################
elif quiz_input in ['No', 'no']:
    print("|---------------------------------------------------------------------------------------------------------|")
    print("|Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Shell Sort, Radix Sort, or Heap Sort|")
    print("|---------------------------------------------------------------------------------------------------------|")
    print("")
    algorithms = str(input("Which sorting algorithm do you want to use? "))

    numbers_amount = int(input("How many numbers do you want to be sorted? "))

    # Initializing/declaring arrays
    input_array = []
    temp_array = []

    for a in range(numbers_amount):
        input_array.append(int(input("Enter a number: ")))
        temp_array = input_array.copy()
    

    print("---------------------------------------")


    #if Statements
    if algorithms in ['Bubble Sort' , 'bubble sort', 'Bubble sort', 'bubble Sort', 'bubble', 'Bubble']:
        BubbleSort(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    
    elif algorithms in ['Selection Sort', 'Selection sort', 'selection sort', 'selection Sort', 'Selection', 'selection']: 
        SelectionSort(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))


    elif algorithms in ['Insertion Sort', 'Insertion sort', 'insertion sort', 'insertion Sort', 'Insertion', 'insertion']:
        InsertionSort(input_array)
        print("---------------------------------------")
        print("The original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Merge Sort', 'Merge sort', 'merge sort', 'merge Sort', 'merge', 'Merge']:
        MergeSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Quick Sort', 'Quick sort', 'quick sort', 'quick Sort', 'quick', 'Quick']:
        QuickSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Shell Sort', 'Shell sort', 'shell sort', 'shell Sort', 'shell', 'Shell']:
        ShellSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Radix Sort', 'Radix sort', 'radix sort', 'radix Sort', 'radix', 'Radix']:
        RadixSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Radix Sort', 'Radix sort', 'radix sort', 'radix Sort', 'radix', 'Radix']:
        RadixSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))

    elif algorithms in ['Heap Sort', 'Heap sort', 'heap sort', 'heap Sort', 'heap', 'Heap']:
        HeapSort(input_array)
        print("---------------------------------------")
        print("THe original array was " + str(temp_array))
        print("The sorted array is " + str(input_array))
