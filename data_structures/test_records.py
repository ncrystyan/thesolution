from data_structures.network_collection import NetworkCollection
import pytest

def test_rem_not_in_subnet():
    entries = [{"address": "1.1.1.254", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "10.0.8.1", "available": False, "last_used": "30/01/20 16:00:00"}]
    nc_in = NetworkCollection('1.1.1.0/24', entries)
    nc_out = NetworkCollection('1.1.1.0/24', entries)
    nc_out.remove_invalid_records()
    assert len(nc_in.entries) == len(nc_out.entries) + 1, "Should remove one record"

def test_rem_not_in_subnet_1():
    entries = [{"address": "1.1.1.254", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "10.0.8.1", "available": False, "last_used": "30/01/20 16:00:00"}]
    
    nc_out = NetworkCollection('1.1.1.0/24', entries)
    nc_out.remove_invalid_records()
    assert nc_out.entries[0].address == "1.1.1.254", "Should be 1.1.1.254"

def test_rem_one_invalid_ip():
    entries = [{"address": "1.a.a.254", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "1.1.1.1", "available": False, "last_used": "30/01/20 16:00:00"}]
    
    nc_out = NetworkCollection('1.1.1.0/24', entries)
    nc_out.remove_invalid_records()
    assert nc_out.entries[0].address == "1.1.1.1", "Should be 1.1.1.1"

def test_rem_two_invalid_ip():
    entries = [{"address": "1..2.25", "available": True, "last_used": "30/01/20 17:00:00"}, {"address": "1.1.1.0", "available": False, "last_used": "30/01/20 16:00:00"}]
    
    nc_out = NetworkCollection('1.1.1.0/24', entries)
    nc_out.remove_invalid_records()
    with pytest.raises(IndexError):   nc_out.entries[0].address, "Should be empty list -> IndexError"