# Process

[Process of Partitioning on Topic Creation](topic.md)


## Partitioning Tradeoffs
* The more partitions, the greater the zookeeper overhead
  * large partition numbers ensure proper zookeeper capacity
* Message ordering can become complex
  * Use a single partition for global ordering (if you dont want consumer having to deal with ordering)
* The more partitions the longer the leader fail-over time