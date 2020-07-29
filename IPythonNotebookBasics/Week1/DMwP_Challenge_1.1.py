'''
Programming Challenges

#1: Even-Odd Vending Machine
Try writing an “even-odd vending machine,” which will take a number as
input and do two things:
1. Print whether the number is even or odd.
2. Display the number followed by the next 9 even or odd numbers.
If the input is 2, the program should print even and then print 2, 4, 6,
8, 10, 12, 14, 16, 18, 20. Similarly, if the input is 1, the program should
print odd and then print 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.
www.it-ebooks.info
Working with Numbers 23
Your program should use the is_integer() method to display an error
message i
'''

def even_odd_vending_machine(a):

    if (a%2==0):
        print('even')
    else:
        print('odd')
#note that the loop is ending and 9th iteration
    for i in range(1,10):
        print(i*a,',',end = "")
#10th iteration converted to string in order to eliminate space in final output
    print(str(a*10)+'.')
            
if __name__ == '__main__':
    a=int(input('Enter an integer: '))
    even_odd_vending_machine(a)
