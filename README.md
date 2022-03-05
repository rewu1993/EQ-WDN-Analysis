# Water Distribution Network Earthquake Hazard Analysis 

Earthquake hazard analysis code for EBMUD water distribution network using [HydrauSim](https://github.com/cb-cities/pipe-network).


## Data

All the analysis is performed on the EBMUD dataset. 


## Running

The code is composed of two parts: data processing and earthquake impact analysis.

### Data Processing
There are five notebooks to process the raw data from EBMUD.
- EBMUD_parser: parse pipe and node information from the EBMUD raw data 
- data_augmentation: add demand and elevation information to the network 
- select_study_region: select the region of interest from the whole network based on pressure zone code
- data_explorer: tools to visualize the network properties of the selected data
- generate_inp: create the .inp file for hydraulic simulation 

<p align="center">
<img src="https://github.com/rewu1993/EQ-WDN-analysis/blob/master/figures/EBMUD_data_preprocessing.png" alt="high_level" class="design-primary" width="600px">
</p>


### Earthquake Impact Analysis 
There are two notebooks to analyze the impact of an earthquake to the EBMUD WDN. Note: earthquake ground motion data (spatial correlated) is assumed to be given in this case. 
- map_pipe_failure_rates: map ground motion to WDN pipes and use ALA pipe fragility curve to calculate failure probability 
- damaged_network_analysis: use Monte Carlo simulation to estimate demand shortage due to the earthquake event. The hydraulic analysis is performed by [HydrauSim](https://github.com/cb-cities/pipe-network).


<p align="center">
<img src="https://github.com/rewu1993/EQ-WDN-analysis/blob/master/figures/pipe_hazard_analysis.png" alt="high_level" class="design-primary" width="1000px">
</p>

Figure below illustrate the overall concept of the EQ impact analysis
<p align="center">
<img src="https://github.com/rewu1993/EQ-WDN-analysis/blob/master/figures/case_simulation_workflow.png" alt="high_level" class="design-primary" width="400px">
</p>



