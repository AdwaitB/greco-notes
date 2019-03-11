`Resource and Job Managemenet systems` need to evolve for exasclae computers. Hardware is not present to be tested, we need to simulate. Also, hardware variation is too much to have reproducability.

Divides the simulation internally into two parts. The first is the `Batsim` which works on top of SimGrid and tis in charge of the simulation of the resources and the `Decision` which is in charge of taking scheduling or energy related decisions.

It then gives out three files which show the execution schedule, the scheduling metrics and the job metrics.

The components are instantiated as processes (OS System processes) and communicate via a Unix Domain Socket synchronously. The simulation runs is Batsim component and as soon as an event occurs, it is stopped and the Decision component takes further decision.

### SimGrid model

1. Host : A resource that is defined in flops.
2. Links : A link in a network or between  networks. Defined in latency and bandwidth. The network topolgy has to be specified.
3. Processes :  A user defined function that can run on a host (Simulating Algorithms).
4. Messages : Processes communicate with each other using these Messages (Simulating MPI).

The hosts and links are defined by an XML file and the processes and messages that are run are defined in program as a function whose function is registered (in case of simulating algorithms) or as MPI_ communication calls that are handled by SimGrid. The SimGrid runtime takes in a set of hosts on which the computation is run in the cluster. It also takes while simulating how many of them are to be used. 

- [ ] But why do we need this if the cluster is already described?

> In the case of Simulating algorithms, the MPI is simulated, the user defined function is run inside the simulator. Hence the user doesnt have to use `mpi.h` and its defined functions.

> In the case of Simulating MPI, the communication is handled by the simulator while considering the latencies as provided in the configuration file. The user needs to write MPI statements too.

### Batsim model

Batsim consists of a `Master host`

Batsim workloads are divided into two parts. One set of jobs and one set of profiles. A job will have an id, submission time, max wall time (after which it is killed), number of requested resources and the profile. A profile describes how a job is executed.

Workloads are the main Batsim inputs. They consists of job and profiles. Defined in .json.

Types of profiles

1. Delay : The cpu is idle.
2. Parallel : A set of tasks which are tightly bound. Specify tasks array for cpu, and comm matrix between the tasks.
3. Homogeneous Parallel : A task that can run on any machine and comm between each pair takes place. Only two values cpu, comm and specified.
4. Homogeneous Parallel with total amount : Total cpu that should be computed over all nodes.
5. Sequence : A sequence of profiles with repeat value.
6. Homogeneous Parallel with I/O : Specify bytes to read and write. No cpu or comm.
7. Staging between storage tiers : From tier, to tier and size
8. SMPI trace replay : Replay an MPI trace on Batsim.

External Events : External events that occur can be added to the simulation.


### Other Points

- Parallel tasks can be created whose results than can be merged. 
- Simgrid allows each host to have a set of pwer states. Each state defines several properties like the computation speed and enegy consumption. Switching from power states is instantaneous. 
- Batsim defines three power states on top of simgrid (and types of them). Computation, Sleep and Transition. Transition between computation states are instant, sleep states consume energy.