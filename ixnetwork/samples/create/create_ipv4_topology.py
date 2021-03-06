import sys
import os
path = os.path.realpath(__file__)
sys.path.insert(0, path[0: path.rfind('ixnetwork')])

from ixnetwork.samples.Config import Config
from ixnetwork.IxnHttp import IxnHttp
from ixnetwork.IxnConfigManagement import IxnConfigManagement


# get an IxnHttp instance using the samples Config object
ixnhttp = Config.get_IxnHttp_instance()

# management objects
config_mgmt = IxnConfigManagement(ixnhttp)

# clear the current configuration
config_mgmt.new_config()

# create two virtual ports
vports = ixnhttp.root.create_child('vport', count=2)

# setup topology west
w_topology = ixnhttp.root.create_child('topology')
w_topology.attributes.vports.value = [vports[0].href]
w_topology.attributes.name.value = 'West'
w_topology.update()
w_ipv4 = w_topology.create_child('deviceGroup').create_child('ethernet').create_child('ipv4')

# change the address and gw multivalue
w_ipv4.attributes.address.value.single_value = '1.1.1.1'
w_ipv4.attributes.gatewayIp.value.single_value = '1.1.1.2'

# setup topology east
e_topology = ixnhttp.root.create_child('topology')
e_topology.attributes.vports.value = [vports[1].href]
e_topology.attributes.name.value = 'East'
e_topology.update()
e_ipv4 = e_topology.create_child('deviceGroup').create_child('ethernet').create_child('ipv4')

# change the address and gw multivalue
e_ipv4.attributes.address.value.single_value = '1.1.1.2'
e_ipv4.attributes.gatewayIp.value.single_value = '1.1.1.1'
