from lammps import lammps
from mpi4py import MPI
import time
import random

from bayes_opt import BayesianOptimization
from bayes_opt.util import UtilityFunction, Colours
import numpy as np
import asyncio
import threading

# lmp.command("units si")


# lmp.file("Inputscript.lammps")
# lammps_set_variable('rx', 3)
def black_box_function(x, y):
    varx = float(x)#str(3)
    vary = float(y)
    hgtx = 11
    hgty = 20
    print(type(varx))
    print(type(vary))
    print(type(hgtx))
    print(type(hgty))
    # varx = str(varx)
    # lmp.command('variable        rx equal x')
    # lmp.set_variable(varx,3)
    # lmp.set_variable("vary",vary)
    # lmp.set_variable("hgtx",hgtx)
    # lmp.set_variable("hgty",hgty)

    # lmp.command("region cone_1_1 cone z 5 5 ${rx} ${ry} ${hx} ${hy}")
    # lmp.command("region cone_1_1 cone z 5 5 %d 2 11 20" % rx)
    lmp = lammps()
    lmp.command("variable        rx equal %d" % varx)
    lmp.command('variable        ry equal %d' % vary)
    lmp.command('variable        hx equal %d' % hgtx)
    lmp.command('variable        hy equal %d' % hgty)
    # rx = 3
    # lmp.command('variable        rx equal ${varx}')
    lmp.file("loop.lammps")
    # me = MPI.COMM_WORLD.Get_rank()
    # nprocs = MPI.COMM_WORLD.Get_size()
    # print("Proc %d out of %d procs has" % (me,nprocs),lmp)
    # MPI.Finalize()
    # lmp.command('variable        rx equal 3')
    natoms = lmp.get_natoms()

    output = natoms
    print(output)
    print(varx)
    print(vary)
    lmp.close()
    return output
# lmp.set_variable("cut",cut)  
# # lmp.command

from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (2, 4), 'y': (1, 3)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=2,
    n_iter=3,
)

print(optimizer.max)

for i, res in enumerate(optimizer.res):
    print("Iteration {}: \n\t{}".format(i, res))
    

