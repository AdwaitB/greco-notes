### Issues with Big Data

1. Handling the big data : Data arrives from multiple streams at a very high rate.
2. Analysis : Data might be possibly incomplete. The data is also heterogeneous in content, type m structure and formats.
3. Privacy : Given this huge infrastructure required to store this data, leaks are hard to manage.
4. Storage : Such a large data cannot be stored and acted upon on a single storage unit.
5. Visualization : Making sense of this incomplete, unstructured data
6. Job Scheduling : Efficient distribution of jobs in a distributed environment.
7. Fault Tolerence : The distributed system underlying the storage of bid data should be able to handle faults.

`Job Scheduling` : This term points to the logic behing how jobs (computations) are executed on a given hardware. Scheduling varies with how the system is. For realtime systems, a FIFO queue destroyes the whole idea of real-time systems as a large jobs will hog the whole system even if all the other jobs in the system are very small. Hence sheduling algorithms are very domain specific and need to be developed keeping the use case in mind. In the contect of Big Data, jobs are usually modificaions/reading on this Big Data.

## Hadoop

Hadoop is an ecosystem of tools used for managing and interacting with Big Data. Hadoop has two core components. HDFS (Hadoop distributed file system) and MapReduce.

- HDFS is distributed file system for storing huge files across distributed nodes. Maintains 3 copies of blocks on different machines. The metadata related to all these nodes is stored in one dedicated server called NameNode, and the application data is kept in each node is stored in the DataNode of that node.
- MapReduce is a programming paradign which is used for computation of data on these distributed nodes.

### Map Reduce

Map Reduce first takes the input data from HDFS. This data is divided by the HDFS into fixed size blocks (as key-value pairs). Then the Map task takes these key-value pairs and then produces the partial result. This result is computed by the underlying distributed system. Each map task is preferably scheduled on the machine where the copy is present. Then the reduce job is collects these partial results and then merges them into one output value.

There is a `MasterNode` which acts as a master for all the nodes on the distributed system. The `MasterNode` consists of two software components. `NameNode` manages the data on each slave node. It has a file system tree and the metadata for all the slave nodes. `JobTracker` manages the jobs on each slave node. Each node on the distributed system is called a `SlaveNode`. They also have corresponding `DataNode` and `TaskTracker` that act on the data and the jobs scheduled on that specific node.

> User Job -> Map taks + Reduce Tasks -> Execute Map tasks (on TaskTracker) -> Reduce (on TaskTracker) -> Output. The number of map and reduce tasks is fixed on a node.

Issues in Map Reduce
- Locality : Distance between input data node and task node. Same node, Rack Node, Other.
- Synchronization : How are the reduce tasks synchonized with the map tasks.
- Fairness : How fair is the scheduling algorithm in dividing the resources. 

## Schedulers in Hadoop

Objectives : Minimize completion time, maximize throughput, Minimize overhead.

1. FIFO : Standard FIFO scheduler. Oldest job first.
2. Fair : Jobs are clustered into pools (like groups of users). Each pool has a minimum share of map and reduce task slots. If a pool reserved share is not being used, it is given to other jobs. The other jobs that used these unused reserve can be preempted. 
3. Capacity : Similar to Fair, unused nodes cannot be shared. No preemptions.
4. Delay : Imporves locality. Jobs are sorted according to the increasing order of running tasks. If a node is free, it selects the first job in the sorted order that satisfies data locality. For tasks that are skipped, the delay time is increased till a threshold. This resolved two issues.
   
    1. Head-of-line scheduling : When a small job with small input file reaches the head of multiple such ordered queues, one task blocks the data, hence the other tasks have to wait.
    2. Sticky slot : When the task of a job are likely to finish execution earlier than other, the job sticks to the slot.

5. Matchmaking : Let the slave nodes grab all the local tasks before any non-local is assigned.
6. Longest Approx Time to End : Detect tasks that are running slow. Launch other tasks as a backup.
7. Deadline Contraint : Users specify deadline constraints. The system estimates the time required for exeution and schedules only the ones for which the deadlines can be met. 
8. Resource Aware : Considers CPI, IO, Disk, Network utilization while scheduling.