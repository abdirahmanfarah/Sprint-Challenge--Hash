def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positive = {}
    result = []

    # loop through array
    for i in a:
        # check if number is in the dictionary
        if positive.get(abs(i)):
            # if it is, add the current number to the array[i] and if they equal zero
            if (positive.get(abs(i)) + i) == 0:
                # append that number to our results arrray
                result.append(abs(i))
        else:
            positive[abs(i)] = i
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# We have a list
# loop through list to find integers that when added together return zero
# two hashtables
