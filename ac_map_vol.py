# importing modules
import requests
import urllib3
import purestorage
from purestorage import FlashArray

# deal with self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



# Establish REST sesstion to both ActiveCluster arrays
array1_name = str(input("Please enter FQDN/IP address of first array: "))
array2_name = str(input("Please enter FQDN/IP address of second array: "))

array1_api_token = str(input("Enter API token for array1: "))
array2_api_token = str(input("Enter API token for array2: "))

array1 = purestorage.FlashArray(array1_name, api_token=array1_api_token)
array2 = purestorage.FlashArray(array2_name, api_token=array2_api_token)



for arrays in [array1, array2]:
    array_info = arrays.get()
    print("FlashArray \x1b[1;31m{}\x1b[0m (Purity {}) REST session established!".format(
        array_info['array_name'], array_info['version']))


# specify POD
pod = str(input("Specify POD name in which the Volume should be created:"))

# create Volume in POD
vol_name = str(input("Specify Volume name: "))
vol_size = str(input("Specify Volume size in GB/TB e.g. 200G/4T: "))
pod_vol_name = pod + "::" + vol_name

array1.create_volume(pod_vol_name, vol_size)  # POD not array when available in newer python toolkit
created_vol = array1.get_volume(pod_vol_name)
print("Volume {} in pod {} successfully created".format(vol_name, pod))

''' code for connection to single host
# connect volume to host or hostgroup
single_host = str(input("Please enter host name to connect volume {} : ".format
                        (created_vol['name'])))

for arrays in [array1, array2]:
    arrays.connect_host(single_host, pod_vol_name)
    array_info2 = arrays.get()
    print("Volume {} connected to host {} on array {}".format
          (pod_vol_name, single_host, array_info2['array_name']))
'''

''' code for connection to a host group
# connect volume to hostgroup
hostgroup = str(input("Please enter hostgroup name to connect volume {} :".format(created_vol['name'])))

for arrays in [array1, array2]:
    arrays.connect_hgroup(hostgroup, pod_vol_name, lun="37")
    array_info2 = arrays.get()
    print("Volume {} connected to hostgroup {} on array {} ".format(
        pod_vol_name, hostgroup, array_info2['array_name']))
'''


