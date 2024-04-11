import matplotlib.pyplot as plt
import pickle

with open('file_communities.pkl', 'rb') as f:
    file_comms = pickle.load(f)
with open('service_communities.pkl', 'rb') as f:
    service_comms = pickle.load(f)

xticks = ['2.0.0', '2.0.5', '2.0.8', '2.2.0', '3.0.0']
fig, axs = plt.subplots(2, 2)

plt.subplot(221)
plt.plot(file_comms['raw_temporal_activity'])
plt.title('File collaboration')
plt.ylabel('Raw activity')
plt.xticks([0, 1, 2, 3, 4], xticks)

plt.subplot(222)
plt.plot(service_comms['raw_temporal_activity'])
plt.title('Service collaboration')
plt.xticks([0, 1, 2, 3, 4], xticks)

plt.subplot(223)
plt.plot(file_comms['in_temporal_activity'])
plt.ylabel('Scaled activity')
plt.xticks([0, 1, 2, 3, 4], xticks)

plt.subplot(224)
plt.plot(service_comms['in_temporal_activity'])
plt.xticks([0, 1, 2, 3, 4], xticks)

fig.supxlabel('Release')
fig.suptitle("Temporal activity of discovered communities")

plt.savefig('temporal_activity.png')
plt.show()
