# Questions

Nodes for greco-p2p analysis

1. Data popularity affects the simulation values. In default, 100 Jobs might use only 20 datasets as we consider jobs in a fixed, small time internval. The datasets added randomly are taken from the datasets.json file which contains all the datasets that have been in CEPH since the beginning. So chances that the same dataset is requested again by another job is drastically reduced. Chances that a dataset requested by two jobs in the same week are drastically higher. We do not have this data when the dataset was first requested in the system.
2. 15s in 24 hours. See heatmap, very less transfers per day. For overlapping to be significant, we need to multiple by a very high value. If there is no overlapping and assuming that p2p bandwidths are less, p2p analysis doesnt make sense.
3. Overlapping is not linear. It reflects like a chain reaction which again is not linear. (2^2^x). Overlaps of overlaps.
4. The issue with CEPH we describe here is due to the overlapping, if we cannot control the generation of overlaps, it is no point doing this.
5. On the x axis it should be max(cardinality)