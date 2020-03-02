from enum import Enum
class ListTypes(Enum):
    BothMatrices = 1
    BothVectors = 2
    VectorAndMatrix = 3
    ConstantAndList = 4

def identify_constant(a,b):
    if isinstance(a,int) or isinstance(a,float):
        return a
    else:
        return b

def identify_matrix(a,b):
        if is_matrix(a) and not is_matrix(b):
            return a
        elif is_matrix(b) and not is_matrix(a):
            return b
        else:
            return None
def identify_vector(a,b):
        if is_vector(a) and not is_vector(b):
            return a
        elif is_vector(b) and not is_vector(a):
            return b
        else:
            return None
def is_constant(a):
    return isinstance(a,float) or isinstance(a,int)

def is_matrix(a):
    return  len(a) > 1 and len(a[0]) >= 1  #isinstance(a,list) and isinstance(a[0],list)

def is_vector(a):
    return len(a) == 1 and len(a[0]) >= 1   #isinstance(a,list) and not isinstance(a[0],list)

def check_type(a,b):
    if is_matrix(a) and is_matrix(b):
            return ListTypes.BothMatrices

    elif is_vector(a) and is_vector(b):
            return ListTypes.BothVectors

    elif is_constant(a) or is_constant(b):
        return ListTypes.ConstantAndList
    else:
        return ListTypes.VectorAndMatrix
