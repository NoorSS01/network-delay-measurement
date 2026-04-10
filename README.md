
#Problem Statement

We need to measure and analyze delay between hosts in a network using Mininet. We also want to compare delay across paths and see how it varies.

#Objectives

-Measure Round Trip Time (RTT) using ping

-Record delay values

-Compare delay across network setups

-Analyze delay variations

-Implement Software Defined Networking (SDN) using POX controller

-Observe flow rule behavior

#Tools Used

-Mininet (a tool to create networks)

-Ubuntu Machine

-POX Controller (a SDN controller)

-Open vSwitch (a virtual switch)

-Ping Command (to test network connectivity)

#Methodology

1. Network Setup

We use Mininet to create networks with hosts and switches.

2. Delay Configuration

We add delay using the command:



sudo mn --link tc delay=10ms



3. Controller Integration

We use POX controller with the command:

./pox.py forwarding.l2_learning

We connect Mininet to the controller using:

sudo mn --controller=remote ip=127.0.0.1,port=6633



4. Delay Measurement

We use ping command to measure delay:

h1 ping h2



5. Flow Rule Observation

We observe flow rules using:

dpctl dump-flows



#Experiment Scenarios

##Scenario 1: Single Switch Topology

We create a network with a switch and 3 hosts using:



sudo mn --topo single,3 --link tc,delay=10ms



Observation:

-Delay is lower

-RTT is around 50 ms

##Scenario 2: Linear Topology (Multiple Switches)

We create a network with switches in a linear setup using:



sudo mn --topo linear,2 --controller=remote ip=127.0.0.1,port=6633 --link tc,delay=10ms



Observation:

-Delay is higher

-RTT is around 100-300 ms

#Results

| Network Setup | Path    | RTT |

| ------------- | ------- | ----------- |

Single Switch | h1 → h2 | ~50 ms      |

| Single Switch | h1 → h3 | ~55 ms      |

| Linear        | h1 → h2 | ~100–300 ms |

#Analysis

-Delay increases with number of switches in the path

-Linear topology has delay due to multiple switches

-RTT values vary due to processing delay queueing delay and network conditions

#SDN Implementation (POX)

-POX controller acts as the brain of the network

-Switch acts as the data forwarding device

-We use the forwarding.l2_learning module

-Controller handles packet events and installs flow rules dynamically

#Flow Table Observation

Using:



dpctl dump-flows



We observe:

-Match fields like input port and MAC address

-Actions like output, to a port

-Dynamic flow installation

#Validation

##Scenario 1:

-Network has low delay

-RTT is

##Scenario 2:

-Network has high delay

-RTT varies

#Proof of Execution

We include screenshots of:

-Mininet network topology

-Ping results

-Flow table output

-POX controller logs


Delay increases with path length and number of switches.

Network delay. Depends on topology and traffic conditions.

SDN using POX shows how a controller can manage the network.