class Matrix():
    def __init__(self, myMatrix):
        self.myMatrix = myMatrix
    
    def __str__(self):
        for i in self.myMatrix:
            for j in i:
                print(j, end=' ')
            print()
        return ""
    
    def not_equal(self, other):
        if len(self.myMatrix) != len(other.myMatrix):
            return True
        for i in range(len(self.myMatrix)):
            if len(self.myMatrix[i]) != len(other.myMatrix[i]):
                return True 
    
    def __add__(self, other):
        if self.not_equal(other):
            return 0
        for i in range(len(self.myMatrix)):
            for j in range(len(self.myMatrix)):
                self.myMatrix[i][j] += other.myMatrix[i][j]
        return Matrix(self.myMatrix)

    

matrices = []
n = int(input("Input number of matrices: "))

for i in range(n):
    arr = []
    m = int(input(f"Input number of rows for {i+1} matrix: "))
    for _ in range(m):
        l = list(map(int, input().split()))
        arr.append(l)
    matrices.append(Matrix(arr))

m1 = matrices[0]
res = True
for i in range(1, len(matrices)):
    m1 += matrices[i]
    if m1 == 0:
        print("Error, matrices are not equal")
        res = False
        break

if res:
    print(m1)

