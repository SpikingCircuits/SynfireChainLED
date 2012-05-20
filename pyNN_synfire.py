from pyNN.utility import get_script_args
from pyNN.errors import RecordingError
from pyNN.nest import *
import numpy as np
from plot_spikes import *
import time

# Setup
start_time = time.time()
setup(timestep=0.1,min_delay=0.1,max_delay=20.0)

# Parameters
exc_neurons_nb = 4
stim_time = 40
stim_freq = 10
chain_delay = 20
chain_delay_inh = 4
chain_weight = 0.1
chain_weight_inh = 0.05

# Create neurons
exc_neurons = []
inh_neurons = []

for i in range(exc_neurons_nb):
	ifcell = create(IF_cond_exp, {  'i_offset' : 0.0,    'tau_refrac' : 2.0,
                                'v_thresh' : -50.0,  'tau_syn_E'  : 5.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})
	exc_neurons.append(ifcell)

for i in range(exc_neurons_nb):
	ifcell = create(IF_cond_exp, {  'i_offset' : 0.0,    'tau_refrac' : 2.0,
                                'v_thresh' : -50.0,  'tau_syn_E'  : 5.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})
	inh_neurons.append(ifcell)

# Create stimulus
input_spikes = [float(i) for i in range(0,stim_time,stim_freq)]
spike_sourceE = create(SpikeSourceArray, {'spike_times': input_spikes})

# Input connections
connE = connect(spike_sourceE, exc_neurons[0], weight=0.5, synapse_type='excitatory',delay=2.0)
connI = connect(spike_sourceE, inh_neurons[0], weight=0.5, synapse_type='excitatory',delay=2.0)

# Connections between stages
for i in range(exc_neurons_nb-1):
	exc_fwd_connection = connect(exc_neurons[i], exc_neurons[i+1], weight=chain_weight, synapse_type='excitatory',delay=chain_delay)
	inh_fwd_connection = connect(exc_neurons[i], inh_neurons[i+1], weight=chain_weight, synapse_type='excitatory',delay=chain_delay)
	inh_connection = connect(inh_neurons[i], exc_neurons[i], weight=chain_weight_inh, synapse_type='inhibitory',delay=chain_delay_inh)

# Loop connection (last neurons)
loop_connection = connect(exc_neurons[exc_neurons_nb-1], exc_neurons[0], weight=chain_weight, synapse_type='excitatory',delay=chain_delay)
loop_connection_inh = connect(exc_neurons[exc_neurons_nb-1], inh_neurons[0], weight=chain_weight, synapse_type='excitatory',delay=chain_delay)
loop_connection_self = connect(inh_neurons[exc_neurons_nb-1], exc_neurons[exc_neurons_nb-1], weight=chain_weight_inh, synapse_type='inhibitory',delay=chain_delay_inh)

# Save results
for i in range(exc_neurons_nb):
	#record_v(exc_neurons[i], "Results/synfire_v_" + str(i) + ".v")
	record(exc_neurons[i], "Results/spikes" + str(i) + ".dat")
	record(inh_neurons[i], "Results/spikes_inh" + str(i) + ".dat")

np.savetxt("Results/input_spikes.dat",input_spikes)

run(1000.0)

end()
print "Simulation done in", time.time() - start_time, "s"

# Plot
plot_spikes(1000,0.1,exc_neurons_nb)