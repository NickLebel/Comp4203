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

### Results
```
PDR vs Number of nodes
         AODV       DSDV       OLSR
20  79.841894  88.207168  89.263461
30  85.697213  97.735463  95.496337
50  85.815089  96.749790  98.512639
70  81.937022  97.855698  98.517588

PDR vs Area Simulation
           AODV       DSDV       OLSR
300   94.634932  38.374255  57.901702
500   85.243252  77.455496  80.310323
1000  75.575734  84.244038  94.444533

PDR vs Speed Simulation
         AODV        DSDV        OLSR
1   80.124177   82.416609   82.920579
2   79.549370   94.534683   96.976680
5   81.937022   97.855698   98.517588
10  83.069806   99.924433  100.000000
20  68.849397  100.000000  100.000000

Packet Loss vs Number of nodes
         AODV       DSDV       OLSR
20  20.158106  11.792832  10.736539
30  14.302787   2.264537   4.503663
50  14.184911   3.250210   1.487361
70  18.062978   2.144302   1.482412

Packet Loss vs Area Simulation
           AODV       DSDV       OLSR
300    5.365068  61.625745  42.098298
500   14.756748  22.544504  19.689677
1000  24.424266  15.755962   5.555467

Packet Loss vs Speed Simulation
         AODV       DSDV       OLSR
1   19.875823  17.583391  17.079421
2   20.450630   5.465317   3.023320
5   18.062978   2.144302   1.482412
10  16.930194   0.075567   0.000000
20  31.150603   0.000000   0.000000

Delay vs Number of nodes
          AODV       DSDV      OLSR
20  847.661636  1751.6679  353.2375
30  547.392893   308.4772  567.7882
50  652.935125   454.6374  164.5963
70  698.310482   932.2955  240.4641

Delay vs Area Simulation
            AODV       DSDV       OLSR
300   542.453832  5526.7456  2417.1219
500   891.788292  5557.1813  3864.3971
1000  887.284349  4885.2374  2159.2766

Delay vs Speed Simulation
          AODV       DSDV        OLSR
1   937.187205  719.28439   394.91237
2   783.938701  774.55060  1141.16520
5   698.310482  932.29550   240.46410
10  965.611522  665.58690   145.22450
20  644.815416  317.87770   161.25030

Throughput vs Number of nodes
         AODV       DSDV       OLSR
20  18.902626  19.890424  20.045576
30  19.771475  19.905939  19.445657
50  19.709414  19.693899  20.030061
70  17.077010  17.956202  18.173414

Throughput (50% scenario) vs Number of nodes
         AODV       DSDV       OLSR
10  35.064242  39.630869  10.090020
20  43.871677  19.905939  48.050424
30  19.771475  28.263434  30.259717
40  29.752889  47.202263  19.445657
50  10.053818  10.110707  40.179071

Throughput vs Area Simulation
           AODV       DSDV       OLSR
300   14.532525   7.835152   9.795232
500   12.551758  17.123556  19.243960
1000  13.782626  15.732364  16.342626

Throughput vs Speed Simulation
         AODV       DSDV       OLSR
1   18.902626  19.890424  20.045576
2   16.130586  20.330020  20.330020
5   20.055919  20.314505  20.330020
10  19.187071  19.207758  19.709414
20  18.494061  16.761535  16.864970
```

### To Run Analysis:
- `pip install -r requirements.txt`
- `python3 analysis.py`
