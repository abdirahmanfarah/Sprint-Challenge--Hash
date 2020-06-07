#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    hash = {}

    for i in range(len(tickets)):
        hash[tickets[i].source] = tickets[i].destination
        # print(hash)

    for k, v in hash.items():
        if k == "NONE":
            route.append(v)

    all_routes = False

    while not all_routes:
        # find out the next route which is LAX
        last_route = route[-1]

        route.append(hash[last_route])
        if last_route == "NONE":
            all_routes = True

    return route[:length]
