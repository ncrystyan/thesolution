import ipaddress
from data_structures.entry import Entry
from data_structures.entry import sorted


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipaddress.ip_network(ipv4_network)
        self.entries = []
        for i in raw_entry_list:
            self.entries.append(Entry(i['address'],i['available'], i['last_used']))
        


    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        hosts = list(ipaddress.ip_network(self.ipv4_network).hosts())
        copy = self.entries.copy()
        for entry in copy:
            
            try:
                if ipaddress.ip_address(entry.address) not in hosts:
                    self.entries.remove(entry)
                
            except:
                self.entries.remove(entry)
        

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
