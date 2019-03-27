# Questions

Place to add questions (and answer them :P).

## Architechture of Qarnot

1. Why is the task model mapped like this?
   3. Parent node?
   4. What about data that is transient?
   5. What about data that is locked?
   6. How to estimate wall time?
2. Where is the location of the InfluxDB in the architecture?
3. How is the IOT workflow processed?

## InfluxDB

1. Why is the sum of `transfer_history.cached_data_size` + `transfer_history.actually_transferred_size` not equal to  `transfer_history.transfer_size`. The absolute value of the difference is concentrated at one point (do not know this exactly).
2. The up values are very small in quantity. (476 up and 11730 down).
3. Unique way to identify datasets? Datasets in json are <jobname:type:size>, which is not a good way to do it.

1. What are the units for time and data_size? (bits and time in seconds, is kind of best case)
2. How do retention policies work? They have different fields. The extractor code has a way to join them, how does that work? Also is there anyway to get a raw CSV with all fields? 
