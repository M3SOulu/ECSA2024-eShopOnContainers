# Temporal Network Community Detection for Collaboration Networks

This is a fork of eShopOnContainers repository for the paper ???.

This branch contains the data replication instructions for the developer coupling network construction and analysis.
All the other branches are original branches and are used for commit mining

All commands should be run in the root of this repository

## Obtaining the developer collaboration networks

For developer collaboration network mining, install the `mison` python package

```shell
python -m pip install mison==1.0.1
```

### Mining the commits

Mine the commits corresponding to the studied releases with the `mison` commands

```shell
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --to 2017-10-27 --commit_table data_commits/eshop_commits_2.0.0.csv
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --to 2018-04-05 --since 2017-10-27 --commit_table data_commits/eshop_commits_2.0.5.csv
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --since 2018-04-05 --to 2018-11-12 --commit_table data_commits/eshop_commits_2.0.8.csv
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --since 2018-11-12 --to 2019-03-21 --commit_table data_commits/eshop_commits_2.2.0.csv
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --to 2019-11-26 --since 2019-03-21 --commit_table data_commits/eshop_commits_3.0.0.csv
python -m mison commit --backend pydriller --import_mapping_file mison.mappings.eshoponcontainers --repo . --since 2019-11-26 --to 2021-10-27 --commit_table data_commits/eshop_commits_5.0.0.csv
```

### Constructing the networks

Process the commits information into file and service developer collaboration networks for each release:

NOTE: order of lines will not be preserved relative to example files that are already in this repository, but the content is the same.

```shell
# File networks
python -m mison network --commit_table data_commits/eshop_commits_2.0.0.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_2.0.0.csv
python -m mison network --commit_table data_commits/eshop_commits_2.0.5.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_2.0.5.csv
python -m mison network --commit_table data_commits/eshop_commits_2.0.8.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_2.0.8.csv
python -m mison network --commit_table data_commits/eshop_commits_2.2.0.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_2.2.0.csv
python -m mison network --commit_table data_commits/eshop_commits_3.0.0.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_3.0.0.csv
python -m mison network --commit_table data_commits/eshop_commits_5.0.0.csv --field file --skip_zero --network_output data_file_network_raw/eshop_network_files_5.0.0.csv

# Service networks
python -m mison network --commit_table data_commits/eshop_commits_2.0.0.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_2.0.0.csv
python -m mison network --commit_table data_commits/eshop_commits_2.0.5.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_2.0.5.csv
python -m mison network --commit_table data_commits/eshop_commits_2.0.8.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_2.0.8.csv
python -m mison network --commit_table data_commits/eshop_commits_2.2.0.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_2.2.0.csv
python -m mison network --commit_table data_commits/eshop_commits_3.0.0.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_3.0.0.csv
python -m mison network --commit_table data_commits/eshop_commits_5.0.0.csv --field service --skip_zero --network_output data_service_network_raw/eshop_network_services_5.0.0.csv
```

## Temporal community detection

### Choosing the amount of communities R to detect based on Core Consistency

The script `choice_of_R.py` repeats the PARAFAC decomposition of the network tensors for different choices of R 
 and creates the 'elbow' figure to allow selection of the optimal parameter value (4 in our paper).
It also saves the calculated core consistencies in json files.
