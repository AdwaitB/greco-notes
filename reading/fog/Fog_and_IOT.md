## IOT + cloud
- high latency between cloud and iot devices.
- data size increases vastly as iot nodes increase
- not suitable for realtime/periodic iot systems
- these metrics change for iot devices that are ubiquitios and moving.

Fog to the rescue
	Acts as an interface for data and control between iot and cloud

Research works
- Comm between different devices in the fog
- security and privacy of transferred data
- reducing the size of transmitted data
- where to process/store

Fog network highly depends on what iot application is considered. But this should not be the case. New application are large scale, latency sensitive and share resources with each other.

Edge computing is more towards the user. Fog is more towards the infra.

OpenFog nomnclature: 1. Cloud layer, Multi-tier Fog layer, edge layer.
This fog layer has multiple tiers. More the tier is close to the cloud, more powerful it is, but it suffers more latency can face more bandwidth issues

## Challenges faced by fog

1. Scalability : Fog network should be able to handle geo-distributed and high volume of iot devices. The presence of ubiquious nodes imply the importance of elasticity too.

2. Interoperability : Like edge nodes, fog nodes will come in a variety of physical configurations, providers and software. These devices should be able to communicate with each other efficiently and  hide differences.

3. Realtime resposiveness : Fog nodes should be able to provide low latency computation and communication. They should also be able to communicate with the cloud regarding multiple data streams from iot devices for storage and long term processing.

4. Data Quality : Important due to sensor actuation dependency. Fog nodes that take in data from multiple, possibly heterogeneous sources need to ensure the quality of data. Data aggregation, filtering, normalization and analytics are necessary operations. Faulty data is problematic.

5. Security : Due to the large quanitity of nodes present in a fog network, security protocols which operate over the whole network and not just between two specific nodes are required for better safety and avoid unecessary computation. More than this, fog security values with tiers, hence the transport of critical data is to be monitored across a large number of nodes.

6. Location awareness : Fog networks need to be location aware for iot devices to be able to support ubiquious devices and provide more security. If the network is aware of the geo-location, performance can be hugely improvised across tiers. Not only inside of fog networks, but also between and beyond. 

7. Mobility : Data in case of mobile edge devices needs to be rerouted in real time where the destination is mobile. Getting data to the mobile node without the added latency is a non-trivial challenge. Large quantities of data are generated on the move which needs to be managed.

8. Reliability - The fog nodes should be independently reliable, available and serviceable. This is same as cloud to maintain the quality of the nodes and provide QoS management. Reliability encompasses hardware reliability of computation and connectivity.

## Architecture

A grid of horizontal and vertical components/perspectives. The grid is the cartesian product.

### Vertical
Edge, Fog, Cloud

### Horizontal

- Communication : Interoperable infrastructure for fast exchanges of data. Mobile devices should be easily transferable.
- Security : This encompasses security and privacy of data and also the safety given the system has actuators.
- Data Quality : Noise reduction, normalization, filtering, aggregation, compression (relating to cloud tier).
- Sensing and Actuation Management - Both sensor and actuation nodes can be a part of the fog network. Unlike compute nodes, these are critical and are the direct interface to the application. 
- Cloudification : Set up a small distributed cloud in a fog network. These nodes will need to have virtualization technologies to support the same functionality as cloud. Networking capabilites are by default included. Vastly improves latency and enables location aware realtime computing.
- Analytics and Decision Making - The characteristic to handle, analysize data at different levels. Process realtime data and make crucial actuator decisions. Process long time data far away from the edge.

## Taxonomy

- Communication
	- Standardization
		- Application Protocol : Custom protocols
		- Infra Protocol : Protocols for network layer and lower devices
	- Network Semantics
		- Retransmission : Error correction for data validity
		- Handshake : Negotiatiate transmission parameter
		- Publish/Subscribe : Multicast for FOG?
	- Low-Lantency
	- Mobility
		- Routing - Construct and maintain optimal routes
		- Resource Discovery - Locate devices that travel between multiple subnets/networks.

- Security
	- Safety ?? Depends on business logic ??
		- Activity Coordination
		- Activity Monitoring
		- Action Planning
	- Security
		- Confidentiality - Data should be routed to the right place
		- Data Loss - Data loss should be well monitored and controlled
		- Data Integrity - Prevent unauthorized modifications
		- Intrusion detection - Detect and prevent unauthorized access for read/write
	- Privacy
		- Access Control - Control unauth users. IP spoofing is possible given the massive network of devices, significant of which are local
		- Partial Computation - A technique where each party computes and gets only a minimal result.

- Data Quality
	- Data Normalization - Vast range of sensors. Can give data which is of different resolutions.
		- Specification Language - Common format that is accepted in the whole network.
		- Data Homogenization - Make the data look same. Fix resolution and sampling.
		- Data Serialization - Data needs to be serialized for communication. This is protocol dependent, has to be standardized.
	- Data Filtering - Remove noise, erroreous and faulty data. Ideally implemented near the edge to prevent the unnecessary crowding.
	- Data Aggregation - Shorten the data even further. ?? Not sure if this is lossless ??

- Sensing and Actuation Management - Can be physical or virtual.
	- Sensors
	- Actuators

- Cloudification - Encapsulate IOT applications and deploy them as VM's or docker images
	- Virtualization - Manage migration and manage iot system
	- Storage - A distributed storage can be developed locally on a fog network. It can be a distributed storage. This storage can also be a part of a larger content delivery network where local caches are generated for location based data or as requested. CDN is equivalent to a dumb version of a fog storage.

- Analytics and Decision Making
	- Data Analytics - Process the data
		- Big Data Analytics - Restricted to cloud
		- Small Data Analytics - Used for realtime systems
		- Hierarchial Data Analytics - Used to manage network related data
	- Decision Making - Make decision based on the processed data. Defines the business.
		- Predictive - Predict a metric of the system. A long term initiative. Based on big data analytics
		- Reactive - Short term predictions. Based on small data analytics.