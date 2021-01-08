from airports.inputs import starting_airport, airports, routes

# construct graph
class Airport:
    def __init__(self, name):
        self.name = name
        self.outbound = []
        self.inbound = []
        self.visited = False  # for Kosaraju's algorithm

class Connection:
    def __init__(self, a1, a2):
        self.inbound = a1
        self.outbound = a2

    def __eq__(self, connection):
        if self.inbound == connection.inbound:
            return True
        return False

class SSC:
    id = 1
    def __init__(self, id):
        self.id = SSC.id
        SSC.id += 1
        self.inbound = set()
        self.outbound = set()

airports = [Airport(airport) for airport in airports]
airport_names = list(map(lambda x: x.name, airports))


def get_airport_index(airport):
    return airport_names.index(airport.name)


def get_airport_by_name(airport_name):
    return airports[airport_names.index(airport_name)]

connections = []
for route in routes:
    airport_in = get_airport_by_name(route[0])
    airport_out = get_airport_by_name(route[1])
    connection = Connection(airport_in, airport_out)
    airport_in.outbound.append(connection)
    airport_out.inbound.append(connection)
    connections.append(connection)
print()

# find strongly-connected components

# Kosaraju's algorithm

visited_airports = []
def visit(airport):
    if not airport.visited:
        airport.visited = True
        for connection in airport.outbound:
            visit(connection.outbound)

        if visited_airports:
            visited_airports.insert(0, airport)
        else:
            visited_airports.append(airport)
        return
    return



for airport in airports:
    visit(airport)

print()
