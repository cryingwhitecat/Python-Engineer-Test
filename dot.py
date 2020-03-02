from itertools import chain
from identify import *


# class LengthMismatchException(Exception):
#     def __init__(self,*args):
#         self.message = args
#     def __str__(self):
#         if self.message:
#             return self.message
#         else:
#             return "Length Mismatch Exception occured"

def dot(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a * b
    try:
        flag = check_type(a,b)
        if flag == ListTypes.BothMatrices:
            return multiply_matrices(a,b)
        elif flag == ListTypes.BothVectors:
            return multiply_vector(a[0],b[0])
        elif flag == ListTypes.VectorAndMatrix:
            return mv_multiplication(a,b)
        elif flag == ListTypes.ConstantAndList:
            return multiply_by_constant(a,b)
    except Exception :
         print("An Exception Occured")
         return


def multiply_by_constant(a,b):
    cs = identify_constant(a,b)
    list_var = identify_matrix(a,b)
    if list_var == None:
        list_var = identify_vector(a,b)
    if not isinstance(list_var[0],list):
        result = [i*cs for i in list_var]
        return result
    else:
        result = [[0 for i in range(len(list_var[0]))] for j in range(len(list_var))]
        for i in range(len(list_var)):
            for j in range(len(list_var[0])):
                result[i][j]= list_var[i][j] * cs
    return result
    


#matrix-vector multiplication    
def mv_multiplication(a,b):
    matrix = identify_matrix(a,b)
    vector = identify_vector(a,b)[0]
    w = len(matrix)
    h = 1
    result = init_result(w,h)
    for i in range(len(matrix)):
        total = 0
        for j in range(len(vector)):
            total += vector[j]*matrix[i][j]
        result[i] = total
    return result

def init_result(w,h):
    if h == 1 and w != 1:
        result = [0 for x in range(w)]
        return result
    elif w == 1 and h != 1:
        result = [0 for y in range(h)]
        return result
    result =  [[0 for x in range(w)] for y in range(h)]
    return result

def multiply_vector(a,b):

    if isinstance(a,int):
        result = [a*b[i] for i in range(len(b))]
        return result

    elif isinstance(b,int):
        result = [b*a[i] for i in range(len(a))]
        return result


    elif len(a) == len(b):
        result = init_result(len(a),len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                result[i][j] = a[i]*b[j]
        return result
    else:
        return mv_multiplication(a,b)

def multiply_matrices(a,b):
    w = len(b[0])
    h = len(a)
    result = init_result(w,h)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

if __name__ == "__main__":
    X = [[1,2,3]]
    Y = [[5,8,1],[5,2,2]]
    result = dot(X,Y)
    if result is not None:
        print(result)


