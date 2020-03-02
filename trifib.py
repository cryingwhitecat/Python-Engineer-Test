from dot import dot

def m_power(matrix,n):
    temp = matrix
    for i in range(n):
        temp = dot(temp,matrix)
    return temp

def trifib(n):
    S = [[1,1,1],[1,0,0],[0,1,0]]
    V = [1,0,0]
    temp = []
    result = []

    if n <= 3:
        return V[n-1]

    temp = m_power(S,n-4)
    result = dot(temp,V)
    return (result[0],temp)

if __name__ == "__main__":
    result,matrix = trifib(10000)
    print("10000th trifib is "+str(result))
    print("Transition Matrix is ")
    print(matrix)

