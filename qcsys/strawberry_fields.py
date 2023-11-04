# generate samples

from strawberryfields.apps import sample
import numpy as np

nr_modes = 5
n_mean = 5
nr_samples = 10

A = np.random.normal(0, 1, (nr_modes, nr_modes))
A += A.T

samples = sample.sample(A, n_mean, nr_samples)

# implementation of max clique

from strawberryfields.apps import clique, data, sample
import networkx as nx

p_hat = data.PHat() # load samples
g = nx.Graph(p_hat.adj) # graph from adjacency matrix
s = sample.postselect(p_hat, 16, 20) # post-select samples
s = sample.to_subgraphs(s, g) # convert to subgraphs
cliques = [clique.shrink(i, g) for i in s] # select clique subgraphs
cliques = [clique.search(c, g, 10) for c in cliques] # search neighbours

# output results

from strawberryfields.apps import plot

clique_sizes = [len(c) for c in cliques]
largest_clique = cliques[np.argmax(clique_sizes)]
plot.graph(g, largest_clique)

import strawberryfields as sf # import module
from strawberryfields.ops import * # contains operations


num_subsystems = 2 # number of qumodes in circuit
prog = sf.Program(num_subsystems) # store our circuit

with prog.context as q: # context manager
    Sgate(1.0) | q[0] # first wire (qumode)
    Sgate(1.0) | q[1] # phase squeezing gate
    BSgate() | (q[0], q[1]) # beam splitter
    MeasureFock() | q # measure state

eng = sf.Engine(backend="gaussian") # backend
results = eng.run(prog, shots=10) # simulations to average
state = results.state # quantum state
measurements = results.samples # measurements
print(state, measurements)