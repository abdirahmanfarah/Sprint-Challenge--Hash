def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positive = {}
    result = []

    for i in a:
        for j in a:
            if positive is not None:
                if (positive[i] + positive[j]) == 0:
                    print(i)

        else:
            positive[i] = i

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# We have a list
# loop through list to find integers that when added together return zero
# two hashtables
