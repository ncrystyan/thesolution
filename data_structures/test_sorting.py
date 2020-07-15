from data_structures.network_collection import NetworkCollection


def test_sorting_length():
    entries = [{"address": "1.1.1.254", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "10.0.8.1", "available": False, "last_used": "30/01/20 16:00:00"}, {"address": "1.1.1.4", "available": True, "last_used": "30/01/20 17:00:00"},{"address": "5.5.8.1", "available": False, "last_used": "30/01/20 16:00:00"}]
    nc_in = NetworkCollection('1.1.1.0/24', entries)
    nc_sorted = NetworkCollection('1.1.1.0/24', entries)
    nc_sorted.sort_records()
    assert len(nc_in.entries) == len(nc_sorted.entries), "Should be equal to original"

def test_sorting_position():
    entries = [{"address": "1.1.1.254", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "10.0.8.1", "available": False, "last_used": "30/01/20 16:00:00"}, {"address": "1.1.1.4", "available": True, "last_used": "30/01/20 17:00:00"},{"address": "5.5.8.1", "available": False, "last_used": "30/01/20 16:00:00"}]
    
    nc_in = NetworkCollection('1.1.1.0/24', entries)
    nc_sorted = NetworkCollection('1.1.1.0/24', entries)
    nc_sorted.sort_records()
    for i in nc_sorted.entries:
        print(i.address)
    assert nc_sorted.entries[0].address == "1.1.1.4" and nc_sorted.entries[2].address == "5.5.8.1", "Should be 1.1.1.4 first and 5.5.8.1 third in list"
