def get_indices_of_item_weights(weights, length, limit):
    hash = {}
    length = len(weights)

    # loop through the array
    for num in range(length):
        # keep track of num minus the limit
        result = hash.get(limit - weights[num])
        if result is not None:
            return(num, result)
        else:
            hash[weights[num]] = num

    return None
