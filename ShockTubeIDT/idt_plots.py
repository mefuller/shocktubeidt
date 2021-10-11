"""
Copyright 2021 Mark E. Fuller

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


def comp_mix_mech(mixes, mechs, temps, pres, IDTs, labels, ofname):
    wdth = np.ones(1)
    hght = [
        3,
        1,
    ]  # basically this just says to make the Arrhenius plots 3 times larger than the relative error plots
    gs = gridspec.GridSpec(2, 1, width_ratios=wdth, height_ratios=hght)

    MarkerList = ["o", "s", "*", "^", "v", ">", "<", "h", "p", "D", "+", "|"]
    styles = ["-", "--", ":", "-."]
    colors = ["k", "r", "b", "g", "tab:orange"]

    # start by plotting on one figure - may break down to one per compositions
    fig = plt.figure(dpi=600, figsize=(2.64, 3.5))
    ax = plt.subplot(gs[0])

    for q, X in enumerate(mixes):
        for w, M in enumerate(mechs):
            ind = (q * len(mixes)) + w
            plt.semilogy(
                (1000.0 / temps),
                IDTs[q, w, :],
                ls=styles[w],
                lw=2,
                color=colors[q],
                label=labels[ind],
            )

    ax.legend(loc="best", fontsize=2)
    ax.grid()
    # ax.set_xlabel('1000/T (1/K)', fontsize=12)
    ax.set_ylabel("Ignition Delay (s)", fontsize=12)
    # ax.tick_params(labelsize=8)

    ax = plt.subplot(gs[1])
    for q, X in enumerate(mixes):
        for w, M in enumerate(mechs):
            ind = (q * len(mixes)) + w
            plt.plot(
                (1000.0 / temps),
                IDTs[q, w, :] / IDTs[q, 0, :],
                ls=styles[w],
                lw=2,
                color=colors[q],
                label=labels[ind],
            )

    # ax.legend(loc='best',fontsize=14)
    # ax.grid()
    ax.set_xlabel("1000/T (1/K)", fontsize=12)
    ax.set_ylabel("Ratio", fontsize=12)
    ax.yaxis.set_major_locator(MaxNLocator(4))
    # ax.tick_params(labelsize=6)

    fig.tight_layout()
    fig.savefig(ofname)
    # plt.show()
    # plt.close()
