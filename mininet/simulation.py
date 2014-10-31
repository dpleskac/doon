"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

num_nodes = 2
num_vxlans_per_node = 1
num_hosts_per_vxlan = 2

def overlayNet():

    "Create an empty network and add nodes to it."
    net = Mininet()

    switches = []

    for node in range(1, num_nodes + 1):
        info( '**  Creating node %d\n' % node) 

        'Create switch for the node '
        s = net.addSwitch( 's%d' % node , ip='10.0.0.%d' % (node + 100))

        'Create hosts '
        for vxlan in range(1, num_vxlans_per_node + 1):
            for host in range(1, num_hosts_per_vxlan + 1):
                host_str = 'h' + str(node) + chr(ord('a') + vxlan - 1) + str(host) 
                h = net.addHost(host_str, \
                                ip='%d.0.0.%d' % (vxlan, (host + ((node - 1) * num_hosts_per_vxlan))), \
                                mac='00:00:00:00:00:%d' % (host + ((node - 1) * num_hosts_per_vxlan)))
                'Connect to node switch'
                net.addLink( h, s )

        'Create links between switches'
#        for sw in switches:
#            net.addLink( sw, s )

        switches.append( s )


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    overlayNet()
