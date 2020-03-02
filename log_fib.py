from dot import dot
def log_fib(n):
    A = [[1,1],[1,0]]
    init_vector = [[0,1]]
    result = dot(A,init_vector)
    for i in range(n-2):
        result = dot(A,result)
    return result[0]
if __name__=="__main__":
    nums = [5,10,35,40,42,500000]
    fibs = []
    for i in nums:
        fibs.append(log_fib(i))
    print(fibs)