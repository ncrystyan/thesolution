from data_structures.datacenter import Datacenter

def test_rem_one():
    clusters = {'LOND-007':{"security_level": 1, "networks": {}}, 'LON-007':{"security_level": 1, "networks": {}} }
    dc_in = Datacenter('London', clusters)
    dc_out = Datacenter('London', clusters)
    dc_out.remove_invalid_clusters()
    assert len(dc_in.clusters) == len(dc_out.clusters) + 1, "Should remove one cluster"


def test_rem_one_1():
    clusters = {'LOND-007':{"security_level": 1, "networks": {}}, 'LON-007':{"security_level": 1, "networks": {}} }
    dc_in = Datacenter('London', clusters)
    dc_out = Datacenter('London', clusters)
    dc_out.remove_invalid_clusters()
    assert dc_out.clusters[0].name == 'LON-007', "Should be LON-007"

def test_dc_short_name():
    clusters = {'BA-007':{"security_level": 1, "networks": {}}, 'LON-007':{"security_level": 1, "networks": {}} }
    dc_out = Datacenter('Ba', clusters)
    dc_out.remove_invalid_clusters()
    name_len = len(dc_out.clusters[0].name.split('-')[0])
    assert name_len == 3, "Should be 3"