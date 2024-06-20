from tenetan.networks import SnapshotGraph
from tenetan.community import community_parafac_nn_als

import pickle

file_net = SnapshotGraph()
file_net.load_csv_directory('data_file_network_clean', source_col='developer_a', target_col='developer_b', weight_col='weight',
                            directed=False, sort_vertices=True)
service_net = SnapshotGraph()
service_net.load_csv_directory('data_service_network_clean', source_col='developer_a', target_col='developer_b', weight_col='weight',
                               directed=False, sort_vertices=True)

file_comm = community_parafac_nn_als(file_net, 2,
                                     "in_communities", "out_communities", "raw_temporal_activity",
                                     "in_temporal_activity", "out_temporal_activity", "core_consistency", init='svd')
service_comm = community_parafac_nn_als(service_net, 5,
                                        "in_communities", "out_communities", "raw_temporal_activity",
                                        "in_temporal_activity", "out_temporal_activity", "core_consistency", init='svd')

with open("file_communities.pkl", 'wb') as f:
    pickle.dump(file_comm, f)
with open("service_communities.pkl", 'wb') as f:
    pickle.dump(service_comm, f)
