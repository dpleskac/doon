do.o.n
======

Docker overlay network 


Create a VXLAN tunnel between 2 hosts:
======================================

HOST ABC @192.169.1.101:

sudo ./doon add-node
sudo ./doon add-tunnel 192.169.1.102

H1=$(sudo docker run -d -ti ubuntu bash)
sudo ./pipework doon $H1 1.0.0.10/24


HOST XYZ @192.169.1.102:

sudo ./doon add-node
sudo ./doon add-tunnel 192.169.1.101

H1=$(sudo docker run -d -ti ubuntu bash)
sudo ./pipework doon $H1 1.0.0.20/24

H2=$(sudo docker run -d -ti ubuntu bash)
sudo ./pipework doon $H2 1.0.0.30/24


sudo ovs-ofctl show doon
sudo ovs-ofctl dump-flows doon

sudo ./doon del-tunnel 192.169.1.104
sudo ./doon del-node

