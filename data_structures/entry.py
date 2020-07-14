from datetime import datetime
from data_structures.new_sorted import my_sorted
  
class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = datetime.strptime(last_used, "%d/%m/%y %H:%M:%S")


def sorted(list_entries):
    sorted_entries = my_sorted(list_entries)
    return sorted_entries