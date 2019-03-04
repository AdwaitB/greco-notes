### Introduction and Taxonomy

Resource scheduling at three main levels. Defined based on the IaaS, PaaS and SaaS software stacks. Scheduling happens on all these layers.

1. Scheduling in the application layer : Schedule the physical or virtual layers for software
   1. User QoS
   2. Provider Efficiency
   3. Negotiation
2. Scheduling in the virtualization layer : Mapping virtual layer to physical with optimal load balance, energy consumption, migration, QoS.
   1. Load Balance
   2. Energy Consumption
   3. Cost Effectiveness
3. Scheduling in the deployment layer : Optimal and strategic infrastructure, outsourcing, service placement, etc.
   1. Service Placement
   2. Partner Federation
   3. Data Routing

### Cloud Resource Scheduling problem

Find an optimal mapping $C$ from the set $T x R \rightarrow \R^{z}$ where $T$ is the set of virtual resources that are required or planned, $R$ is the set of physical resources given $z$ objectives that are collectively optimal and that $T$, $R$ are of finite cardinality.

### Nature inspired algorithms

1. Genetic algorithm : Select populations and create mutations and observe the outcome of the mutations.
2. Ant Colony Optimization : Uses the idea that a trail of pheromone implies positive outcome. Although, permenent pheromone trail results in solution stuck at local optima. Hence locally and globally pheromoes are updated. 
3. Particle Swarm Optimization : At every iteration, a set of particles update their velocity vectors by considering three things. Current velocity (momentum), personal maxima (intuition), and global maxima (communication). The distance travelled is stocastic.

All these algorithms pass through the three stages.

1. Fitness evaluation (the countour of an optimization problem)
2. Candidate selection (how the current solutions deviate)
3. Trial variation (add some variation)

