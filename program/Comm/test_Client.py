from reseau import Reseau

if __name__ == "__main__":
    client = Reseau()
    client.client("10.33.1.159", 5454)
    while True:
        client.receiveData()