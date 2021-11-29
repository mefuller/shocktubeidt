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
import matplotlib.colors as mcolors
import numpy as np

# https://matplotlib.org/stable/api/markers_api.html
markers = ["o", "s", "*", "^", "v", ">", "<", "h", "p", "D", "+", "|"]

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
styles = ["-", "--", ":", "-."]

# https://matplotlib.org/stable/gallery/color/named_colors.html
colors = list(mcolors.TABLEAU_COLORS)

def comp_mix_mech(mixes, mechs, temps, IDTs, ofname):
    """
    Routine to plot comparison of igntion delay times for matrix of mechanisms and compositions.
    Prints and saves plot showing absolute values and relative times.
    """
    wdth = np.ones(1)
    hght = [
        3,
        1,
    ]  # make the Arrhenius plots 3 times larger than the comparison plot
    gs = gridspec.GridSpec(2, 1, width_ratios=wdth, height_ratios=hght)

    # https://matplotlib.org/stable/api/markers_api.html
    # MarkerList = ["o", "s", "*", "^", "v", ">", "<", "h", "p", "D", "+", "|"]

    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    styles = ["-", "--", ":", "-."]

    # https://matplotlib.org/stable/gallery/color/named_colors.html
    colors = list(mcolors.TABLEAU_COLORS)

    # Plot figures at 2.64" width: standard ProCI column
    fig = plt.figure(dpi=600, figsize=(2.64, 3.5))

    ax = plt.subplot(gs[0])
    for q, X in enumerate(mixes):
        for w, M in enumerate(mechs):
            plt.semilogy(
                (1000.0 / temps),
                IDTs[q, w, :],
                ls=styles[w % len(styles)],
                lw=2,
                color=colors[q % len(colors)],
            )

    # ax.legend(loc="best", fontsize=2)
    ax.grid()
    ax.set_ylabel("Ignition Delay (s)", fontsize=12)
    # ax.tick_params(labelsize=8)

    ax = plt.subplot(gs[1])
    for q, X in enumerate(mixes):
        for w, M in enumerate(mechs):
            plt.plot(
                (1000.0 / temps),
                IDTs[q, w, :] / IDTs[q, 0, :],
                ls=styles[w % len(styles)],
                lw=2,
                color=colors[q % len(colors)],
            )

    # ax.legend(loc='best',fontsize=14)
    # ax.grid()
    ax.set_xlabel("1000/T (1/K)", fontsize=12)
    ax.set_ylabel("Ratio", fontsize=12)
    ax.yaxis.set_major_locator(MaxNLocator(4))
    # ax.tick_params(labelsize=6)

    fig.tight_layout()
    fig.savefig(ofname)


def comp_mix(mixes, mechs, temps, IDTs, ofname):
    """
    Routine to plot comparison of igntion delay times for matrix of mechanisms and compositions.
    Compares IDT of different mixtures for each mechanism.
    Prints and saves plot showing absolute values and relative times.
    """
    for w, M in enumerate(mechs):
        wdth = np.ones(1)
        hght = [
            3,
            1,
        ]  # make the Arrhenius plots 3 times larger than the comparison plot
        gs = gridspec.GridSpec(2, 1, width_ratios=wdth, height_ratios=hght)

        # https://matplotlib.org/stable/api/markers_api.html
        # MarkerList = ["o", "s", "*", "^", "v", ">", "<", "h", "p", "D", "+", "|"]

        # https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
        styles = ["-", "--", ":", "-."]

        # https://matplotlib.org/stable/gallery/color/named_colors.html
        colors = list(mcolors.TABLEAU_COLORS)

        # Plot figures at 2.64" width: standard ProCI column
        fig = plt.figure(dpi=600, figsize=(2.64, 3.5))

        ax = plt.subplot(gs[0])
        for q, X in enumerate(mixes):
            plt.semilogy(
                (1000.0 / temps),
                IDTs[q, w, :],
                ls=styles[w % len(styles)],
                lw=2,
                color=colors[q % len(colors)],
            )

        # ax.legend(loc="best", fontsize=2)
        ax.grid()
        ax.set_ylabel("Ignition Delay (s)", fontsize=12)
        # ax.tick_params(labelsize=8)

        ax = plt.subplot(gs[1])
        for q, X in enumerate(mixes):
            plt.plot(
                (1000.0 / temps),
                IDTs[q, w, :] / IDTs[q, 0, :],
                ls=styles[w % len(styles)],
                lw=2,
                color=colors[q % len(colors)],
            )

        # ax.legend(loc='best',fontsize=14)
        # ax.grid()
        ax.set_xlabel("1000/T (1/K)", fontsize=12)
        ax.set_ylabel("Ratio", fontsize=12)
        ax.yaxis.set_major_locator(MaxNLocator(4))
        # ax.tick_params(labelsize=6)

        # split ofname at extension
        fext = ofname.split(".")[-1]
        fname = ofname.replace("." + fext, "")

        fig.tight_layout()
        fig.savefig(f"{fname}-mech{w}.{fext}")


def comp_mech(mixes, mechs, temps, IDTs, ofname):
    """
    Routine to plot comparison of igntion delay times for matrix of mechanisms and compositions.
    Compares IDT of different mechanisms for each mixtures.
    Prints and saves plot showing absolute values and relative times.
    Use mechanism name of "data" to plot with symbols, not lines.
    """
    for q, X in enumerate(mixes):
        wdth = np.ones(1)
        hght = [
            3,
            1,
        ]  # make the Arrhenius plots 3 times larger than the comparison plot
        gs = gridspec.GridSpec(2, 1, width_ratios=wdth, height_ratios=hght)

        # Plot figures at 2.64" width: standard ProCI column
        fig = plt.figure(dpi=600, figsize=(2.64, 3.5))

        ax = plt.subplot(gs[0])
        for w, M in enumerate(mechs):
            if M.strip().lower() == "data":
                plt.semilogy(
                    (1000.0 / temps),
                    IDTs[q, w, :],
                    marker=markers[w % len(markers)],
                    ms=8,
                    color=colors[q % len(colors)],
                )
            else:
                plt.semilogy(
                    (1000.0 / temps),
                    IDTs[q, w, :],
                    ls=styles[w % len(styles)],
                    lw=2,
                    color=colors[q % len(colors)],
                )

        # ax.legend(loc="best", fontsize=2)
        ax.grid()
        ax.set_ylabel("Ignition Delay (s)", fontsize=12)
        # ax.tick_params(labelsize=8)

        ax = plt.subplot(gs[1])
        for w, M in enumerate(mechs):
            plt.plot(
                (1000.0 / temps),
                IDTs[q, w, :] / IDTs[q, 0, :],
                ls=styles[w % len(styles)],
                lw=2,
                color=colors[q % len(colors)],
            )

        # ax.legend(loc='best',fontsize=14)
        # ax.grid()
        ax.set_xlabel("1000/T (1/K)", fontsize=12)
        ax.set_ylabel("Ratio", fontsize=12)
        ax.yaxis.set_major_locator(MaxNLocator(4))
        # ax.tick_params(labelsize=6)

        # split ofname at extension
        fext = ofname.split(".")[-1]
        fname = ofname.replace("." + fext, "")

        fig.tight_layout()
        fig.savefig(f"{fname}-mix{q}.{fext}")
