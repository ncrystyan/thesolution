import re
from data_structures.cluster import Cluster
class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = []
        for key, value in cluster_dict.items():
            self.clusters.append(Cluster(key, value['networks'], value['security_level']))


    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        begin = self.name[0:3].upper()
        regex = rf"{begin}-([0-9]){{1,3}}"
        copy = self.clusters.copy()
        for cluster in copy:
            try:
                reg = re.search(regex, cluster.name).group(0)
                if cluster.name != reg:
                    self.clusters.remove(cluster)

            except:
                self.clusters.remove(cluster)
