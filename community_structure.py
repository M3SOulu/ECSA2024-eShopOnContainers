import matplotlib.pyplot as plt
import numpy as np
import pickle

with open('file_communities.pkl', 'rb') as f:
    file_data = pickle.load(f)
with open('service_communities.pkl', 'rb') as f:
    service_data = pickle.load(f)

file_comms = file_data['in_communities']
file_comms = file_comms / np.max(file_comms, axis=None)
service_comms = service_data['in_communities']
service_comms = service_comms / np.max(service_comms, axis=None)

fig, axes = plt.subplots(2,1, figsize=(8,4))
plt.subplot(211)
markerline, stemlines, baseline = plt.stem(file_comms[:, 0], linefmt='-', markerfmt='o')
plt.setp(markerline, 'color', '#1f77b4')
plt.setp(stemlines, 'color', '#1f77b4')
plt.setp(baseline, 'color', 'none')
markerline, stemlines, baseline = plt.stem(file_comms[:, 1], linefmt='--', markerfmt='x')
plt.setp(markerline, 'color', '#ff7f0e')
plt.setp(stemlines, 'color', '#ff7f0e')
plt.setp(baseline, 'color', 'none')
plt.title('File collaboration')
plt.ylim([0.0, 1.05])
plt.xticks([],[])
plt.xlabel('Developers')
plt.ylabel('Membership strength')

plt.subplot(212)
markerline, stemlines, baseline = plt.stem(service_comms[:, 4], linefmt='-', markerfmt='v')
plt.setp(markerline, 'color', '#9467bd')
plt.setp(stemlines, 'color', '#9467bd')
plt.setp(baseline, 'color', 'none')
markerline, stemlines, baseline = plt.stem(service_comms[:, 0], linefmt='-', markerfmt='o')
plt.setp(markerline, 'color', '#1f77b4')
plt.setp(stemlines, 'color', '#1f77b4')
plt.setp(baseline, 'color', 'none')
markerline, stemlines, baseline = plt.stem(service_comms[:, 1], linefmt='--', markerfmt='x')
plt.setp(markerline, 'color', '#ff7f0e')
plt.setp(stemlines, 'color', '#ff7f0e')
plt.setp(baseline, 'color', 'none')
markerline, stemlines, baseline = plt.stem(service_comms[:, 3], linefmt=':', markerfmt='d')
plt.setp(markerline, 'color', '#d62728')
plt.setp(stemlines, 'color', '#d62728')
plt.setp(baseline, 'color', 'none')
markerline, stemlines, baseline = plt.stem(service_comms[:, 2], linefmt='-.', markerfmt='+')
plt.setp(markerline, 'color', '#2ca02c')
plt.setp(stemlines, 'color', '#2ca02c')
plt.setp(baseline, 'color', 'none')
plt.title('Service collaboration')
plt.xticks([],[])
plt.xlabel('Developers')
plt.ylabel('Membership strength')

fig.suptitle('Community membership')

plt.tight_layout()
plt.savefig('communities.png')
