from data_structures.network_collection import NetworkCollection

class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = int(security_level)
        self.networks = []
        for key,value in network_dict.items():
            self.networks.append(NetworkCollection(key, value))


