def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # hash table
    hash = {}
    result = []
    # loop through outer
    for i in range(len(arrays)):
        # loop  through inner arrays index to get their values
        for j in arrays[i]:
            # if number exists in the hash, count 1
            if j not in hash:
                hash[j] = 1
            # if not add it to the hash table
            else:
                hash[j] += 1
    # loop through our hash table to find the numbers that repeated over all the arrays
    for num in hash:
        if hash[num] == len(arrays):
            result.append(num)
            # print(hash)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection([
        [1, 2, 3],
        [1, 4, 5],
        [1, 6, 7]
    ]))
