import serial
import time
import numpy as np
import sys

ser = serial.Serial('/dev/tty.usbmodemfa131', 38400)
time.sleep(1)

# Send a list of spikes and blink at each spike 
def send_spikes(spikes_list,max_time,dec_factor,mapping):

	# Time array creation
	dt = 0.01*dec_factor
	time_array = np.arange(0,max_time*dec_factor+dt,dt)

	# Deccelerate spike times
	for k in spikes_list:
		k[0] = k[0]*dec_factor

	for t in time_array:

		if (spikes_list != []):
	 
			while (t == spikes_list[0][0]):
				spiking_neuron = spikes_list[0][1]
				print "Spike for neuron " + str(mapping_matrix[spiking_neuron]) + " at time " + str(t)
				spikes_list = spikes_list[1:]

				ser.write(str(mapping_matrix[spiking_neuron]))

				if (spikes_list == []):
					break

		# Wait
		time.sleep(dt*1e-3)

# Test the stuff

# Import results from pyNN
spikes_list = []

# Input spikes
data = np.genfromtxt("Results/input_spikes.dat")

for j in data:
	spikes_list.append([j,0])

# Exc spikes
for i in range(4):
	data = np.genfromtxt("Results/spikes" + str(i) + ".dat")

	for j in data:
		spikes_list.append([j[0],i+1])

# Inh spikes
for i in range(4):
	data = np.genfromtxt("Results/spikes_inh" + str(i) + ".dat")

	for j in data:
		spikes_list.append([j[0],i+5])

mapping_matrix = [2,3,5,7,9,4,6,8,"a"]

spikes_list.sort(key=lambda x: x[0])

send_spikes(spikes_list,1000,20,mapping_matrix)