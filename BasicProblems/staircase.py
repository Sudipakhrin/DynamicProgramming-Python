"""Its base and height are both equal to n . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n."""

def staircase(n):
    for i in range(n):
        print( ' ' * (n-i-1) + '#' * (i+1))
    
staircase(6)