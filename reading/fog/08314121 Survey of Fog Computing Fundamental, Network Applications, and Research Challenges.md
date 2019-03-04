### Technologies that use Edge Computing

1. Cloudlets - Put the resource rich computers near the end-user. These are virtualization capable and the user data is accumulated to thiese computers. Then these communicate with the cloud. Faces issues when end user devices are mobile. Heavily depends on VMs. In case of a mobile device, the VM needs to be live migrated to the nearest cloudlet. It works as an independent cloud, does not need the cloud.

2. MEC - A standardization for enabling mobile edge computing platforms to be integrated and used.

3. Fog Computing - Fog computing has more nodes and focusses on using less powerful nodes. It usually needs the cloud to operate

## Architechtures

1. 3-Tier : TN (Terminal Nodes), Fog, Cloud

    This architecture also mentions interfaces between TN and Fog, Fog and Fog and Fog Cloud which are in my opinion the most important interfaces which need standardization for effective use.

2. Layerd Architechture : Consists of multiple logical layers of independent tasks that need to be done.

    1. Physical And Virtualization Layer - TN, sensor nodes
    2. Monitoring layer - Handles service requests from TN and energy related issues.
    3. Preprocessing Layer - Filters the data obtained
    4. Temporary Storate Layer - Stores this filtered data
    5. Security Layer - Makes the temporary data transport secure
    6. Transport Layer - Transport to cloud

    Here the points 2 to 6 comprise of the fog network and relates to the other survey taxonomy as specified. Although this gives a very small picture of how computation is saved locally (except for the data filtering and trimming layer). Fog also does some local computation, possibly at the monitoring layer or between the security and the temporary storage layer. This part is crucial for the real-time cyber-physical systems.

3. Combined Fog-Cloud : The main idea behind this is that the QoS as reqested by the service might vary and their needs might be minimal. Small service requests that do not compute and network intensive tasks (for the fog, not the cloud) like data aggregation can be satisfied with one-hop computing infrastrucre.

    1. TN - Terminal Nodes
    2. Fog 1 - Low access delay (usually one-hop)
    3. Fog 2 - Medium access delay (a bit more close to the cloud than the previosly defined fog)
    4. Cloud

### Virtualized Fog Data Centers

Datacenters provide cloud services on the backbone of virtualization of storage compute and network technologies. This does not address security, but creates flexibility for deployment of user (DSS, Data service subsriber) requested infrastructure. Virtualization also provides monitoring of hardware metrics efficiently and accurately per DSS. Idea of a Virtualized Fog Data Center is to offload this virtualization to DC operators which reside between the DSS and the Cloud. Hence the requests can be handled there. ?? Not sure what these Operators are. Are they any different from setting up local infra? ??
Datacenters provide cloud services on the backbone of virtualization of storage compute and network technologies. This does not address security, but creates flexibility for deployment of user (DSS, Data service subsriber) requested infrastructure. Virtualization also provides monitoring of hardware metrics efficiently and accurately per DSS. Idea of a Virtualized Fog Data Center is to offload this virtualization to DC operators which reside between the DSS and the Cloud. Hence the requests can be handled there. ?? Not sure what these Operators are. Are they any different from setting up local infra? ??

### Fog Radio Access Networks `Not convincing`

### Fog Computing Architecture using Software Defined Networking `Not convincing`

Controlled use of Fog and Edge layer networking when the nodes in both these tiers are high. In conventional networking where networking devices are intelligent and distributed, causes issues when edge nodes are mobile. SDN solves this issue and hence is compatible with fog.

What is not clear as in how SDN is extended to use fog for its own operations and how this integrates with the underlying fog that it is looking to control.

## Mathematical model

### Devices

- Terminal Node : $T = <EU_{id}, Status, \tau_i, L, H, I(q)>$. 
  
  <ID, Status (Idle 0, Active 1), Event Type (Fixed finite set), geographic location, Hardware and software, ID of the application instances>

Set of terminal nodes form a virutal cluster.

- Virtual Cluster : $V = <V_{ID}, T(u) , R , F_{id}>$.
  
  <ID, Set of EU nodes, Region, Physical Fog instance to which the cluster is mapped>

The fog computing instances are like orchestration servers for fog computing devices.

- Fog Computing Instances : $F=<F_{ID}, C_{AP}, D(v)>$.

  <ID, Accespoint through which the fog instance is connected to the cloud, Device ids for all fog devices>

- Fog Computing Devices : $D=<D_{ID}, Type, Spec>$

  <ID, Type (router, gateway, processing, storage), Specifications>

> Mapping from $V \Rightarrow F$ is injective. Every virtual cluster needs a unique instance to communicate to.

> Mapping from  $T \Rightarrow F$ is many to one. A EU can be a part of multiple Virtual Clusters

### Networking

- Edge gateway : $E$. Connects $V$ to $F$. The relation is the cartesian product where each element is a badnwidth limited gateway. $X_{v_i, e, f}^{fog}$ represents routing variable for the link $v_i \rightarrow e \rightarrow f$.

- Fog gateway : $G$. Connects $F$ to Cloud $C$. The set $C$ is not well defined. $X_{f, g, c}^{cloud}$ represents routing variable for the link $f \rightarrow g \rightarrow c$.

> Variable $X$ represents the amount of data transferred in that link.

### Latency, Transmission, Enery Consumption model `Skipped`

## Service allocation and Resource Management

Which service should be processed at which layer? This problem is modelled as an integer linear programming problem which tries to minimize the total service latency given the following restrictions.

1. Requirement of every service (computation wise) is satisfied.
2. Avoid allocation of more slots than available.
3. Prevent use of one slot for more than one service at the same time.
4. Define the delay using a bitmask.

### Latency

Which node of fog to select for what task?

Model the source nodes (where each node can be a set of end user nodes) and the fog nodes as a complete bipartitie graph. Assumption is this is a closed queueing network where the request arrivals from the source nodes are possion. Various policies can be implemented for selecting the fog node for computation.

`Blocking Proabability` : Ratio of rejected workloads and total number of workloads.

### Energy Consumption

Fog power consumption is high due to large amount of nodes that are not computationally powerfull, but do take significant power. Hence optimal energy consumption comes with a tradeoff of latency. Usage of distributed Clouds can help fog. Applications are either static, have dynamic user content or applications where the source data is not created by a user but is obtained from other sources. nDC are useful when most of the data is generated at the edge level.

### Resource Sharing

Resource in a fog network is composed of random distributed resources. These are more flexible and movable due to the large number of nodes and the small size of each of these nodes. Resource sharing terms the sharing of compute, network and storage to other nodes in the network.

`Computational Offloading` : Giving resources to other nodes in the network. This is a very specific idea. It refers to when each node has its own way to manage its resources and hence decides to sell or either offload to other nodes.

A perfect copy of the data need not be stored at every point in the whole network. This will be hard to maintain as data validation and updateion across nodes will be cumbersome. Hence it is important that for a fog network that stores data, the synchronization is well balanced and fast.

### Caching

`Proactive Computing` : The caching of partially computed results during off-peaks.

Resource caching in fog servers is necessary for fast access by terminal nodes. The terminal nodes themselves might not store any resources themselves, so their reliability on the fog increases. Thus the fog cluster needs to have a way to store or cache this resource with minimum cost.

Consider that the fog network is a graph where the nodes are the fog nodes and the edges are the connection with weights as the cost of that specific connection. To find the minimum value of cost associated for distributing the data between every node, we need to find a Steiner tree. Unlike a minimum spanning tree, the fog network is configurable to be added with more nodes (possibly only for routing) and thus the optimal value of the least cost can be decreased more than the solution of the MST.

### VM

Virtualization technology can be used at the fog tier to reduce computation dependence on the cloud. Virtualization is hard to maintain on slow, mobile devices and hence poses a challenge. Fog tier virtualization needs to handle live migration to be able to handle mobile edge devices. Making the decision when and where to migrate the VM depends completely upon the application's requirement, QoS, SLA etc. The total downtime as faced by migration.

### Unvertainity of Position and Availability of Fog Nodes

Difficult load balancing as nodes are active, inactive, joining, leaving a networks. This increases communication overhead and makes dynamic resource allocation difficult. Latency is also an important factor in fog nodes (it is why it was introduced first). Maintaining low lantency in such cases is necessary.

### Realtime Fog network formation

Due to uncertianity in the presence of terminal devices, it might be better if the fog network is reconstructed as per the movement of the nodes. In such a case, it needs to be decided when and which nodes should be a part of the new fog network. Handling partially synchronized resources, partially computed results add to the issues faced by this idea.