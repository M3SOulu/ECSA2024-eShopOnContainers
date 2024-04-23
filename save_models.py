from tenetan.networks import SnapshotGraph
from tenetan.community import community_parafac_nn_als

import pickle

file_net = SnapshotGraph("data_file_network_concat_network.csv", directed=False)
service_net = SnapshotGraph("data_service_network_concat_network.csv", directed=False)

file_comm = community_parafac_nn_als(file_net, 4,
                                     "in_communities", "out_communities", "raw_temporal_activity",
                                     "in_temporal_activity", "out_temporal_activity", "core_consistency", init='svd')
service_comm = community_parafac_nn_als(service_net, 4,
                                        "in_communities", "out_communities", "raw_temporal_activity",
                                        "in_temporal_activity", "out_temporal_activity", "core_consistency", init='svd')

with open("file_communities.pkl", 'wb') as f:
    pickle.dump(file_comm, f)
with open("service_communities.pkl", 'wb') as f:
    pickle.dump(service_comm, f)
