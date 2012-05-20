import pylab
import numpy

def plot_spikes(max_time, timestep, nb_neurons):

	t = numpy.arange(0,max_time+timestep,timestep)

	# Input pop
	data = numpy.genfromtxt("Results/input_spikes.dat")

	for j in data:
		pylab.plot([j,j],[-1,0],c="g",linewidth=2)

	for i in range(nb_neurons):

		# Exc_pop
		data = numpy.genfromtxt("Results/spikes" + str(i) + ".dat")

		spike_times = []
		for j in data:
			spike_times.append(j[0])

		for j in spike_times:
			pylab.plot([j,j],[i*2,i*2+1],c="r",linewidth=2)

		# Inh_pop
		data = numpy.genfromtxt("Results/spikes_inh" + str(i) + ".dat")

		spike_times = []
		for j in data:
			spike_times.append(j[0])

		for j in spike_times:
			pylab.plot([j,j],[i*2+1,i*2+2],c="b",linewidth=2)

	pylab.xlim(0,max_time)
	pylab.xlabel("Time [ms]")
	pylab.ylabel("Neuron ID")
	pylab.show()

plot_spikes(1000,1e-3,4)