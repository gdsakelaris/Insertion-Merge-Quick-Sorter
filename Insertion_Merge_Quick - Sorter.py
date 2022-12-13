print("\nINSTRUCTIONS:")
print("-----------------------------------------------------------------------------------------------\n")
print("Run all tests through this file/shell (A3.py) with the sorter() function.\n\n"
      "A3.py must be in the same directory as the file(s) you wish to sort.\n")
print("-----------------------------------------------------------------------------------------------\n")
print("    Call = sorter('filename', 's')\n")
print("filename = string of the file name (including its extension)\n")
print("       s = string representing the first initial of the sorting\n"
      "           algorithm you want to call (NOT case-sensitive)\n\n")
print("Examples:\n"
      "     >>> sorter('10_Random.txt', 'i')   --> Calls Insertion Sort on 10_Random.txt\n"
      "     >>> sorter('100_Reverse.txt', 'M') --> Calls Merge Sort on 100_Reverse.txt\n"
      "     >>> sorter('1000_Sorted.txt', 'q') --> Calls Quick Sort on 1000_Sorted.txt\n\n")
print("The output of sorter() will include:\n\n"
      "1. A list of the data in its original order (used to check if the sorted output was valid)\n"
      "2. The sorted data, printed one element per line\n"
      "3. A few basic messages indicating what is being done\n\n")
print("Note: All possible test calls are commented out at the bottom of A3.py.\n"
      "      They can be uncommented to run multiple tests at once.\n")
print("-----------------------------------------------------------------------------------------------")

def InsertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key
    print("Insertion Sort Output:\n")
    for i in range(len(lst)):
        print(f"{lst[i]}")
    print("\nInsertion Sort Completed")
    print("-----------------------------------------------------------------------------")

    
def MergeSort(lst):
    leng = len(lst)
    if leng == 1:
        return lst
    
    mid = leng // 2
    left_part = MergeSort(lst[:mid])
    right_part = MergeSort(lst[mid:])
    return Merge(left_part, right_part)

def Merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    output.extend(left[i:])
    output.extend(right[j:])
    return output

def runMergeSort(lst):
    sortedLst = MergeSort(lst)
    print("Merge Sort Output:\n")
    for i in range(len(sortedLst)):
        print(f"{sortedLst[i]}")
    print("\nMerge Sort Completed")
    print("-----------------------------------------------------------------------------")


def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1
        (lst[i], lst[j]) = (lst[j], lst[i])
              
    (lst[i + 1], lst[high]) = (lst[high], lst[i + 1])
    return i + 1
        
def QuickSort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)

        QuickSort(lst, low, pi - 1)
        QuickSort(lst, pi + 1, high)


def sorter(filename, s):
    file = open(filename)
    fileout = []
    for iii in file:
        ii = iii.strip()
        i = int(ii)
        fileout.append(i)
    print(f"List of data from '{filename}' in its ORIGINAL ORDER:\n\n{fileout}\n")

    typeOfsort = s.upper()
    if typeOfsort == 'I':
        InsertionSort(fileout)
    elif typeOfsort == 'M':
        runMergeSort(fileout)
    elif typeOfsort == 'Q':        
        inp = fileout
        size = len(inp)
        QuickSort(inp, 0, size - 1)
        print("Quick Sort Output:\n")
        for i in range(len(inp)):
            print(f"{inp[i]}")
        print("\nQuick Sort Completed")
        print("-----------------------------------------------------------------------------")



## All Possible Tests:
     
#sorter('10_Random.txt', 'I')  
##sorter('10_Reverse.txt', 'I')
##sorter('10_Sorted.txt', 'I')
##sorter('10_Random.txt', 'M')       
##sorter('10_Reverse.txt', 'M')
##sorter('10_Sorted.txt', 'M')
##sorter('10_Random.txt', 'Q')      
##sorter('10_Reverse.txt', 'Q')
##sorter('10_Sorted.txt', 'Q')

##sorter('100_Random.txt', 'i')
##sorter('100_Reverse.txt', 'i')
##sorter('100_Sorted.txt', 'i')
##sorter('100_Random.txt', 'm')
##sorter('100_Reverse.txt', 'm')
##sorter('100_Sorted.txt', 'm')
##sorter('100_Random.txt', 'q')
##sorter('100_Reverse.txt', 'q')
##sorter('100_Sorted.txt', 'q')

##sorter('1000_Random.txt', 'I')
##sorter('1000_Reverse.txt', 'i')
##sorter('1000_Sorted.txt', 'I')
##sorter('1000_Random.txt', 'm')
##sorter('1000_Reverse.txt', 'M')
##sorter('1000_Sorted.txt', 'm')
##sorter('1000_Random.txt', 'Q')
##sorter('1000_Reverse.txt', 'q')
##sorter('1000_Sorted.txt', 'Q')
