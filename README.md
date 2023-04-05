| Parameter               | Parameter Value                               |
|-------------------------|-----------------------------------------------|
| Simulation Program      | NS-3.35                                       |
| Operating System        | Ubuntu 22.04 LTS                              |
| Number of Node          | 10,20,30,40,50,70                             |
| Number of Area(m)       | 200x200, 300x300, 500x500, 1000x1000          |
| Simulation Speed (m/s)  | 1m/s, 2m/s, 5m/s, 10m/s, 20m/s                |
| Radio Propagation Model | Friis Propagation Loss                        |
| Packet Size             | OnOff Application                             |
| Protocol MAC            | 802.11                                        |
| RTS/CTS                 | None                                          |
| Mobility Model          | Random Way Point                              |
| Simulation Time         | 200 seconds                                   |


## Scenario 1
### [Experiment 1](https://github.com/NickLebel/Comp4203/tree/master/nodes)
- Area       = 200x200
- Node speed = 5m/s
- Nodes      = 20 / 30 / 50 / 70 / (100 not included)
- Receivers  = 10
- Limitations: Run time of 100 node
- Matched paper :x:
### [Experiment 2](https://github.com/NickLebel/Comp4203/tree/master/nodesvsreceivers)
- Area       = 200x200
- Node speed = 5m/s
- Nodes      = 10 / 20 / 30 / 40 / 50
- Receivers  = 5 / 10 / 15 / 20 / 25
- Limitations: None
- Matched paper :heavy_check_mark:


## [Scenario 2](https://github.com/NickLebel/Comp4203/tree/master/area)
- Area       = (100x100 not included), 300x300, 500x500, 1000x1000
- Node speed = 5m/s
- Nodes      = 70
- Receivers  = 10
- Limitations: Run time of 100x100
- Matched paper :x:


## [Scenario 3](https://github.com/NickLebel/Comp4203/tree/master/speed)
- Area       = 200x200
- Node speed = 1m/s, 2m/s, 5m/s, 10m/s, 20m/s
- Nodes      = 50 (instead of 70)
- Receivers  = 10
- Limitations: Run time of 70 node
- Matched paper :x:

## Data and Metrics
### CSV Files
- Throughput in Kbps in 2nd column (ReceiveRate)
- First ~100 empty lines are simulation preparation after program build.

### XML Files
- Delay
- PDR
- Lost packets

### To Run Analysis:
- `pip install -r requirements.txt`
