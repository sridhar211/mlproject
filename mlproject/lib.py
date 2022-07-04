from mlproject.distance import haversine

def hello_world():
    return "Hello world from mlproject"

def try_me():
    lat1 = float(input('Enter latitude of location 1:\n'))
    lon1 = float(input('Enter longitude of location 1:\n'))
    lat2 = float(input('Enter latitude of location 2:\n'))
    lon2 = float(input('Enter longitude of location 2:\n'))
    print ('Haversine distance between two locations is:', haversine(lon1,lat1,lon2,lat2))

if __name__ == "__main__":
    try_me()
