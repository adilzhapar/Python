class Matrix():
    def __init__(self, myMatrix):
        self.myMatrix = myMatrix
    
    def __str__(self):
        for i in self.myMatrix:
            for j in i:
                print(j, end=' ')
            print()
        return ""
    
    def __add__(self, other):
        if len(self.myMatrix) != len(other.myMatrix):
            return 0
        for i in range(len(self.myMatrix)):
            for j in range(len(self.myMatrix)):
                self.myMatrix[i][j] += other.myMatrix[i][j]
        return Matrix(self.myMatrix)
        


matrices = []
for i in range(3):
    arr = []
    for _ in range(3):
        l = list(map(int, input().split()))
        arr.append(l)
    matrices.append(Matrix(arr))

m1 = matrices[0]
res = True
for i in range(1, len(matrices)):
    m1 += matrices[i]
    if m1 == 0:
        print(0)
        res = False
        break

if res:
    print(m1)

