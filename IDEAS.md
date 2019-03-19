
# IDEAS

Place to add ideas.

## Fog Computing

1. `Graph of Graphs`
   1. Model the whole network (cloud + fog + edge) as a graph of graphs. The whole network will be sparse where some edge and fog network will have high connectivity. Hence model the whole network as a graph (possibly of fog networks) and then the nodes are another graph. This will make processing simple.
2. `Estimating data transfer costs, using edge caches`
   1. Considering two main factors, the bandwidth and the latency. The bandwidth can be mapped with network flow and the latency with dijkstra. Latency will be small compared to delay caused due to bandwidth.
   2. Extend this to consider multi source, multi destination and merging both of these factors. This algorithm should scale well and needs to be fast. The final value should be scaled by a constant factor that can be learnt by ML or even regression (which is possible in realtime).
   3. Gomory-Hu trees as an intermediate data structure for linear time queries for max flow. Although in such a case, exact flow cannot be found out.
3. `Speculation`
   1. Given that cache data is used for local transport, we can find clusters while initializing the data such that the worst case cost for travel (if requested anywhere from the network) is minimized. k-means clustering to find clusters.
   2. Help the scheduler by identifying nodes where data is seldom localized. This gives an idea for unused local instances where background tasks dominate. Data can be localized here while initializing or during data transfer request.
   3. Also identify points where data is clogging the bandwidth. Move data away from these points.
4. `Synchronization`
   1. The knowledge base needs to be up-to-date for being effective. Since the data operations are executed through the storage controller, the map can be updated before the action is executed. A periodic heartbeat message will make sure that local changes and monitors keep the knowledge updated.
5. `Fog Storage`
   1. Similar to IPFS with DFS, we can have storage devices that cache data on each of the above mentioned tiers. The scheduling nodes are synchronized with the storage controller nodes. How faster this is than one single DFS for the whole Fog network to be studied.
6. `Checkpointing` 
   1. Checkpointing for long duration tasks. Although, it is not necessary now, in case of highly distributed systems, and very high number of tasks, node availability is not guranteed. Tasks can be specifically programmed with an interface which supports
      - Taking a checkpoint
      - Loading from a checkpoint
      - Evaluating percentage of task completion
7. `Unified Scheduling`
   1.  In traditional single node computers, scheduling was done on the single fact to minimize turnaround time and maximize throughput. This was crucial for better use. There was a single source of data. Hence the scheduler was different than the storage controller.
   2.  Even in case of multiple PCI peripherals, compute, storage scheduling wasn't much of a problem due to very fast busses interconnecting each device independently.
   3.  Now, the storage are jobs are equally important given the geo-distributed nature. One cannot simply consider these are two different entities. The scheduling of jobs to achieve user SLA and the efficient storage are equally important for fault tollerant and reducing network impact.
   4.  So instead of thinking of the storage controller as a different unit, I define a map set which is a set of maps that has a data mapped to multiple jobs (and its reverse). Hence this map set is fundamental unit of this geo-distributed system.
   5.  Each map has to be handled without seperating data and compute.
8. `Multi layer scheduling`
    1.  All models described are centralized.
    2.  Nodes in the whole system cannot be stable. As system increases the frequency at which nodes enter/exit the system will be fast that communication about all this with the central scheduler will be very slow and hence the scheduler wont be able to communicate efficiently.
    3.  Split the map of jobs -> data into multiple large sets and let the local schedulers handle this.
    4.  This is scalable as multi-tier scheduling is possible. Only the bottom layer does the exact node scheduling.
    5.  Easier message passing. The network wont be overloaded with data transfers.