### Latencies in flog infrastructure

Edge to Fog : 10 ms to 100 ms
Interfog : 50 to 100 ms
Fog to Cloud : Not predictable

## IPFS

For fog networks, we need a storage protocol that works P2P and is also efficient in the communication. IPFS builds on top of BitTorrent protocol for file transfer and Kademlia which is a distributed hash table (DHT). The idea is to keep the DHT for tracking files and the BitTorrent for efficient file transfers. IPFS then brings the two together to make a storage system that works on distributed nodes. Both the BitTorrent protocol and Kademlia DHT are scalable.

### A brief IPFS working protocol

There are multiple IPFS nodes in a fog network that store the data. DHT are also stored and are their locations are known by every IPFS node. A client can request the local IPFS node for the data. In such a scenario, there are three cases. In all the cases, the location of the data is always updated in the DHT.

1. Data is created in the client : The data is directly put in the local IPFS and DHT is updated.
2. Data is present in the same fog : The other IPFS in the local system is now consulted. It then asks the DHT. Then this data is cached in the local and returned. The DHT is updated.
3. Data not present in the fog : Local IPFS consults DHT, retrieves data, sends to user. Then it caches the data and updates DHT with its location. 

The end update in DHT seems asynchronous. Hence when the DHT is updated has no bound.

### Drawbacks

It does not take advantage of the topology of the fog network. For example if the fog node has multiple IPFS and since the DHT update is asynchronous, the existence of the file in the local IPFS due to BitTorrent transfer is not taken into consideration. Hence multiple requests for the same file from the same fog network can cause high data transfers in the network.

## IPFS with scaled out NFS

We use a DFS Server (which is a scaled out NFS) at every fog site. Rather than the IPFS node in the fog asking the DHT if the file is not present, it asks the local DFS server. Whenever the file is received by BitTorrent, it then caches the file in the DFS server. So now if any other IPFS node from the same fog is requests for the same file, the DFS is consulted which now has the file. DHT updates do not change.