from tenetan.networks import SnapshotGraph
from tenetan.community import community_parafac_nn_als

import matplotlib.pyplot as plt

import json

N_COMM_MAX = 6  # Maximum number of communities in the experiments


def repeat_detection(net: SnapshotGraph, n_comm_max: int = 20):
    results = {}
    for n_comm in range(2, n_comm_max+1):
        print(f"Running experiment for {n_comm=} (max {n_comm_max})")
        experiment = community_parafac_nn_als(net, n_comm, "core_consistency", init='svd')
        results[n_comm] = experiment["core_consistency"]
    return results


file_net = SnapshotGraph("data_file_network_concat_network.csv")
service_net = SnapshotGraph("data_service_network_concat_network.csv")

cc_file_net = repeat_detection(file_net, n_comm_max=N_COMM_MAX)
cc_service_net = repeat_detection(service_net, n_comm_max=N_COMM_MAX)

with open(f"core_consistency_file_network_ncomm_max_{N_COMM_MAX}.json", 'w') as f:
    json.dump(cc_file_net, f)
with open(f"core_consistency_service_network_ncomm_max_{N_COMM_MAX}.json", 'w') as f:
    json.dump(cc_service_net, f)

plt.figure()
plt.subplot(121)
plt.plot(cc_file_net.keys(), cc_file_net.values(), 'b-')
plt.plot(cc_file_net.keys(), cc_file_net.values(), 'ro')
plt.title('File collaboration')
plt.subplot(122)
plt.plot(cc_service_net.keys(), cc_service_net.values(), 'b-')
plt.plot(cc_service_net.keys(), cc_service_net.values(), 'ro')
plt.title('Service collaboration')
plt.suptitle("Core consistency elbow")
plt.savefig('cc_elbow.png')
plt.show()
