# Temporal Network Community Detection for Collaboration Networks

This is a fork of eShopOnContainers repository for the paper ???.

This branch contains the data replication instructions for the developer coupling network construction and analysis.
All the other branches are original branches and are used for commit mining

## Install necessary packages

For developer coupling network mining, install the `mison` python package

For the temporal community discovery, install `tenetan` library with optional dependencies for preprocessing:

```python
python -m pip install tenetan[prepr]
```


## Temporal community detection

### Choosing the amount of communities R to detect based on Core Consistency

The script `choice_of_R.py` repeats the PARAFAC decomposition of the network tensors for different choices of R 
 and creates the 'elbow' figure to allow selection of the optimal parameter value (4 in our paper).
It also saves the calculated core consistencies in json files.
