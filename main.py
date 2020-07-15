import time
import json
from urllib.request import Request, urlopen
from urllib.error import URLError
from data_structures.datacenter import Datacenter


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    r = Request(url)
    retry = 0
    while retry < max_retries:
        try:
            data = urlopen(r).read()
            if data:
                js_data = json.loads(data)
                break
        except URLError:
            retry += 1
            print('Retry no {}'.format(retry))
            time.sleep(delay_between_retries)
    try:
        return js_data
    except UnboundLocalError:
        return None


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [Datacenter(key, value) for key, value in data.items()]


    for i in datacenters:
        i.remove_invalid_clusters()
        print(i.name)
        for j in i.clusters:
            print('\t'+j.name)
            # print (str(j.networks) + ' {}'.format(type(j.networks)))
            for k in j.networks:
                
                k.remove_invalid_records()
                print('\tNetwork {}'.format(k.ipv4_network))
                for e in k.entries:
                    print('\t\t'+e.address)

                k.sort_records()
                print('\tSorted record entries:')

                for e in k.entries:
                    print('\t\t'+e.address)



    with open('mocky_response.json', 'w') as f:
        json.dump(data, f, indent=3)




if __name__ == '__main__':
    main()
