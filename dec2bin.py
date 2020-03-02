def dec2bin_list(num,arr=[]):

    assert isinstance(num,int), "num must be an integer"
    assert num >=0, "num must be greater or equal than zero"

    if num > 1:
        arr = dec2bin_list(num // 2,arr)
    arr.append(num % 2)
    return arr

if __name__ == "__main__":
    print(dec2bin_list(10))