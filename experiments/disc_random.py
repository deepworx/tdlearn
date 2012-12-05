# -*- coding: utf-8 -*-
"""
Convergence speed comparison of TD methods on a (uniformly) random MDP
@author: Christoph Dann <cdann@cdann.de>
"""

import td
import examples
from task import LinearDiscreteValuePredictionTask
import numpy as np
import matplotlib.pyplot as plt
import features
import policies
import regtd
n = 10
n_a = 5
n_feat = 10
mdp = examples.RandomMDP(n, n_a)
phi = features.lin_random(n_feat, n, constant=True)
#phi = features.eye(n)
gamma = .95
np.random.seed(3)
beh_pol = policies.Discrete(np.random.rand(n, n_a))
tar_pol = policies.Discrete(np.random.rand(n, n_a))
#tar_pol=beh_pol
task = LinearDiscreteValuePredictionTask(mdp, gamma, phi, np.zeros(phi.dim),
                                         policy=beh_pol, target_policy=tar_pol)


lstd = td.LSTDLambda(lam=0, phi=phi)
lstd.name = r"LSTD({})".format(0)
lstd.color = "b"
methods.append(lstd)

lstd = td.LSTDLambdaJP(lam=0, phi=phi)
lstd.name = r"LSTD-JP({})".format(0)
lstd.color = "b"
methods.append(lstd)


tau=0.1
lstd = regtd.DLSTD(tau=tau, lam=0, phi=phi)
lstd.name = r"D-LSTD({}) $\tau={}$".format(0,tau)
lstd.color = "b"
#methods.append(lstd)

tau=0.0001
lstd = regtd.LSTDl1(tau=tau, lam=0, phi=phi)
lstd.name = r"LSTD-l1({}) $\tau={}$".format(0,tau)
lstd.color = "b"
methods.append(lstd)

tau=0.1
lstd = regtd.LarsTD(tau=tau, lam=0, phi=phi)
lstd.name = r"LarsTD({}) $\tau={}$".format(0,tau)
lstd.color = "b"
#methods.append(lstd)

l = 500
n_eps = 1
n_indep = 1

error_every = 1
name = "disc_random"
title = "{}-State Random MDP ({} trials)".format(n, n_indep)
criterion = "RMSPBE"
criteria = ["RMSPBE", "RMSE", "RMSBE"]
if __name__ == "__main__":
    from experiments import *
    mean, std, raw = run_experiment(n_jobs=1, **globals())
    for m in methods:
        print m.name, m.theta[-1]
    #save_results(**globals())
    plot_errorbar(**globals())