import bubble
bubble.bubblesort(obj1)

# from bubble import bubblesort
# bubblesort()

#This is the program where we are using sorting method with the help of OOPs
class Sorting():
    def __init__(self, my_list=[]):
        self.array = my_list

    def bubbleSort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j +1] = self.array[j + 1], self.array[j]

    def selectionSort(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            j = i-1
            nxt_element = self.array[i]
            while (self.array[j] > nxt_element) and (j >= 0):
                self.array[j+1] = self.array[j]
                j = j-1
            self.array[j+1] = nxt_element

    def shellSort(self):
        gap = len(self.array) // 2
        while gap > 0:
            for i in range(gap, len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j = j-gap
                self.array[j] = temp
                gap = gap//2

#if __name__ == "__main__":

while True:
    print("\n\nwe have four type of sorting please select the choice according to their given number")
    print("1.Bubble Sort")
    print("2.Selection Sort")
    print("3.Insertion Sort")
    print("4.Shell Sort")
    print("5.exit")

#here we ask to user to selct the sorting according to their given number
    choice=input("enter the choice(1/2/3/4/5):")
    if choice == '5':
        print("\n\nThank you for using sorting!\n\n")

        break
    obj1 = Sorting()
    print("\nenter the value that you want to sort -")
    obj1.array = list(map(int, input().strip().split(" ")))


#Here we start B5ubble sort
    if choice=='1':
        bubble.bubblesort(obj1)
        print("bubble sorting :-")
        print(obj1.array)
        with open('C:/Users/91884/AppData/Local/Programs/Python/Python38-32/buble.py','r') as f:
            print(f.read())
#Here we start we start selction sort
    elif choice=='2':  
        obj1.selectionSort()
        print("\nselection sorting :-")
        print(obj1.array)
#here we start insertion sort
    elif choice=='3':    
        obj1.insertion_sort()
        print("\nInsertion sort :-")
        print(obj1.array)


#here we start shell sort
    

    elif choice == '4':
        obj1.shellSort()
        print("\nShell sorting :-")
        print(obj1.array)

    else:
        print("you have entered the wrong choice")    




