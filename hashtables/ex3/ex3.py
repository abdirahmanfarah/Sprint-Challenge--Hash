def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # hash table
    hash = {}
    result = []

    # loop through outer
    for i in range(len(arrays)):
        # loop  through inner arrays to get all the values
        for j in range(len(arrays[i])):
            # if number exists in the hash, put that in the result array
            if i is not
            # if not add it to the hash table
            else:
                hash[arrays[i]] = i

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
