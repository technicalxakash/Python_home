"""

print("==================================================")

print("hello")

for i in range(0,5):
    print(i)



for i in range(0,5):
    for j in range(0,5):
        print("* ",end=" ")
    print(" ")



for i in range(0,7):
    for j in range(i):
        print("* ",end=" ")
    print(" ")



for i in range(0,5):
    for j in range(0,5):
        print(i,end=" ")
    print(" ")

for i in range(0,7):
    for j in range(i):
        print(i,end=" ")
    print(" ")



for i in range(0,7):
    for j in range(i):
        print(j,end=" ")
    print(" ")



k=1;
for i in range(0,6):
   
    for j in range(0,i+1):
        print(k,end=" ")
        k=k+1;
    print(" ")


==================================================
hello
0
1
2
3
4
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
 
*   
*  *   
*  *  *   
*  *  *  *   
*  *  *  *  *   
*  *  *  *  *  *   
0 0 0 0 0  
1 1 1 1 1  
2 2 2 2 2  
3 3 3 3 3  
4 4 4 4 4  
 
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  
6 6 6 6 6 6  
 
0  
0 1  
0 1 2  
0 1 2 3  
0 1 2 3 4  
0 1 2 3 4 5  
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15  
16 17 18 19 20 21  
==================================================

print("==================================================")
"""