# Pascal's triangle
def pascal_triangle(n):
    for i in range(1,n+1):
        for j in range (n-i,0,-1):
            print(end=" ")
        C = 1
        for k in range (1,i+1):
            print(C,end=" ")
            C = int(C*(i-k)/k)
        print(" ")

pascal_triangle(6)


    