
# IDEAS

Place to add ideas.

## Fog Computing

1. `Graph of Graphs`
   1. Model the whole network (cloud + fog + edge) as a graph of graphs. The whole network will be sparse where some edge and fog network will have high connectivity. Hence model the whole network as a graph (possibly of fog networks) and then the nodes are another graph. This will make processing simple.
2. `Estimating data transfer costs, using edge caches`
   1. Considering two main factors, the bandwidth and the latency. The bandwidth can be mapped with network flow and the latency with dijkstra. Latency will be small compared to delay caused due to bandwidth.
   2. Extend this to consider multi source, multi destination and merging both of these factors. This algorithm should scale well and needs to be fast. The final value should be scaled by a constant factor that can be learnt by ML or even regression (which is possible in realtime).
3. `Speculation`
   1. Given that cache data is used for local transport, we can find clusters while initializing the data such that the worst case cost for travel (if requested anywhere from the network) is minimized. k-means clustering to find clusters.
   2. Help the scheduler by identifying nodes where data is seldom localized. This gives an idea for unused local instances where background tasks dominate. Data can be localized here while initializing or during data transfer request.
   3. Also identify points where data is clogging the bandwidth. Move data away from these points.
4. `Synchronization`
   1. The knowledge base needs to be up-to-date for being effective. Since the data operations are executed through the storage controller, the map can be updated before the action is executed. A periodic heartbeat message will make sure that local changes and monitors keep the knowledge updated.
5. `Scheduling` 
   1. Having multi-tier QBoxes. Currently QBoxes are the only link between the edge and the cloud. So in places where there are multiple QBoxes for a large site. We can have a 'parent QBox' that controls these Qboxes. Scheduling occurs at every level and each level is only responsible for the next level. Every level does have metrics based on its subtree.
6. `Fog Storage`
   1. Similar to IPFS with DFS, we can have storage devices that cache data on each of the above mentioned tiers. The scheduling nodes are synchronized with the storage controller nodes. How faster this is than one single DFS for the whole Fog network to be studied.
7. `Checkpointing` 
   1. Checkpointing for long duration tasks. Although, it is not necessary now, in case of highly distributed systems, and very high number of tasks, node availability is not guranteed. Tasks can be specifically programmed with an interface which supports
      - Taking a checkpoint
      - Loading from a checkpoint
      - Evaluating percentage of task completion