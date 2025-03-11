<p align="center">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="public/kafka.png">
  <source media="(prefers-color-scheme: dark)" srcset="public/kafka.png">
  <img src="public/kafka.png" alt="Kafka Logo" width="20%"> 
</picture>
</p>

# Apache Kafka

This is a repository  for adding files and commands while learning Apache Kafka

### Downloading Kafka
Kafka can be downloaded from the official website
https://kafka.apache.org/downloads

Locate the folder for Kafka

```
$ cd kafka_2.13-3.9.0
```
To Start the **Zookeeper** Service,  
Open your terminal in the Kafka directory  
Run the following command on your terminal  
```
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
To Start the **Kafka broker** Service  
Open a new terminal in the Kafka directory  
Run the following command on your terminal
```
$ bin/kafka-server-start.sh config/server.properties
```
