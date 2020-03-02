import matplotlib.pyplot as plt
from dot import dot
import math

def scalar_product(a,b):
    return a[0]*b[0] + a[1]*b[1]

def calculate_length(vector):
    return math.sqrt(vector[0]**2+vector[1]**2) 

def calculate_angle(a,b):
    a_legth = calculate_length(a)
    b_length = calculate_length(b)

    cosine = scalar_product(a,b) / (a_legth * b_length)

    return math.acos(cosine)

def print_angles(vectors):
    print("angle between vectors a and b is: " + 
        str(math.degrees(calculate_angle(vectors[0],vectors[1]))))
    print("angle between vectors b and c is: " +
        str(math.degrees(calculate_angle(vectors[1],vectors[2]))))
    print("angle between vectors a and c is: " + 
        str(math.degrees(calculate_angle(vectors[0],vectors[2]))))

if __name__ == "__main__":
    vectors = [[1, 1], [-2, 2], [1.8, -0.5]]

    origin = [0], [0]
    # plt.quiver(*origin, [v[0] for v in vectors], [v[1] for v in vectors],\
    #     color=['r','b','g'], scale=10)
    # plt.show()
    operators = [
        [[1,0],[0,1]],
        [[0,1],[1,0]],
        [[0,1],[-1,0]],
        [[math.sqrt(3)/2, 0.5],[-0.5,math.sqrt(3)/2]],
        [[1,0],[0,0]],
        [[2,0],[0,1]],
        [[0.7,0.7],[-0.7,0.7]]
    ]
    for operator in operators:
        n_vectors = dot(vectors, operator)
        print_angles(n_vectors)
        plt.quiver(*origin, [v[0] for v in n_vectors], [v[1] for v in n_vectors],
        color=['r','b','g'], scale=10)
        plt.show()
