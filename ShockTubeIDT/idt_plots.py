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
from cividisHexValues import cividis_map

# https://matplotlib.org/stable/api/markers_api.html
markers = ["o", "s", "*", "^", "v", ">", "<", "h", "p", "D", "+", "|"]

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
styles = ["-", "--", ":", "-."]

# https://matplotlib.org/stable/gallery/color/named_colors.html
tabcolors = list(mcolors.TABLEAU_COLORS)

def line_colors(n: int, cmap: list = None):
    """
    With n lines and given colormap, cmap, return evenly spaced set of colors
    for plotting. If using multiple line styles (quantity s), recommend passing
    n%s as first argument to utilize more widely-spaced colors.
    Default to using cividis color map with option to override.
    """

    # cividis color map values from
    # https://github.com/pnnl/cmaputil/blob/master/colormaps/cividisHexValues.txt
    if cmap is None:
        cmap = cividis_map

    # check n
    if n < 1 or not isinstance(n, int):
        print(f"A positive integer number of lines is required; {n} was requested")
        print("Exiting")
        return

    # check cmap
    a = len(cmap)  # get dimensions of colormap
    if n > a:
        print(f"Requesting {n} lines when colormap contains only {a} entries!")
        print("Exiting")
        return

    clist = []  # initialize empty list for colors
    clist.append(cmap[0][:])  # first entry is first line

    if n > 1:
        # pull evenly spaced values without linear interpolation
        for k in range(1, n):
            q = float(k * (a - 1)) / float(n - 1)
            clist.append(cmap[int(np.rint(q))][:])

    return clist

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

    # Plot figures at 2.64" width: standard ProCI column
    fig = plt.figure(dpi=600, figsize=(2.64, 3.5))

    #import colors
    #colors = tabcolors
    colors = line_colors(len(mixes))

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

        # Plot figures at 2.64" width: standard ProCI column
        fig = plt.figure(dpi=600, figsize=(2.64, 3.5))

        #import colors
        #colors = tabcolors
        colors = line_colors(len(mixes))

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

        #import colors
        #colors = tabcolors
        colors = line_colors(len(mixes))

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

def comp_mech_data(mixes, mechs, temps, IDTs, ofname, Tdata = None, Taudata = None, RelPlot = True):
    """
    Routine to plot comparison of igntion delay times for matrix of mechanisms and compositions.
    Compares IDT of different mechanisms for each mixtures.
    Prints and saves plot showing absolute values and relative times.
    **test function for data, dropping relative plot**
    """
    for q, X in enumerate(mixes):
        if RelPlot:
            wdth = np.ones(1)
            hght = [
                3,
                1,
            ]  # make the Arrhenius plots 3 times larger than the comparison plot
            gs = gridspec.GridSpec(2, 1, width_ratios=wdth, height_ratios=hght)

            # Plot figures at 2.64" width: standard ProCI column
            fig = plt.figure(dpi=600, figsize=(2.64, 3.5))
        else:
            wdth = [1]
            hght = [1]
            gs = gridspec.GridSpec(len(hght), len(wdth), width_ratios=wdth, height_ratios=hght)

            # Plot figures at 2.64" width: standard ProCI column
            fig = plt.figure(dpi=600, figsize=(2.64, 2.64))

        #import colors
        #colors = tabcolors
        colors = line_colors(len(mechs))

        ax = plt.subplot(gs[0])
        for w, M in enumerate(mechs):
            plt.semilogy(
                    (1000.0 / temps),
                    IDTs[q, w, :],
                    ls=styles[w % len(styles)],
                    lw=2,
                    color=colors[w % len(colors)],
                )
        # add data
        if Tdata is not None:
            if Taudata is not None:
                try:
                    plt.semilogy(
                            (1000.0 / Tdata[q, w, :]),
                            Taudata[q, w, :],
                            ls='none',
                            marker=markers[q],
                            ms=8,
                            markerfacecolor='none',
                            markeredgewidth=1,
                            color=colors[q],
                        )
                except:
                    print(f"Unable to plot data at mix {q} and mechanism {w}:")
                    print(X)
                    print(M)
            else:
                print("WARNING: experimental values for temperature have been passed, but not IDT values")
        elif Taudata is not None:
            print("WARNING: experimental IDT values have been passed, but not for temperature")

        # ax.legend(loc="best", fontsize=2)
        ax.grid()
        ax.set_ylabel("Ignition Delay (s)", fontsize=12)
        # ax.tick_params(labelsize=8)

        if RelPlot:
            ax = plt.subplot(gs[1])
            for w, M in enumerate(mechs):
                plt.plot(
                    (1000.0 / temps),
                    IDTs[q, w, :] / IDTs[q, 0, :],
                    ls=styles[w % len(styles)],
                    lw=2,
                    color=colors[w % len(colors)],
                )
            ax.set_ylabel("Ratio", fontsize=12)
            ax.yaxis.set_major_locator(MaxNLocator(4))

        # ax.legend(loc='best',fontsize=14)
        # ax.grid()
        ax.set_xlabel("1000/T (1/K)", fontsize=12)
        # ax.tick_params(labelsize=6)

        # split ofname at extension
        fext = ofname.split(".")[-1]
        fname = ofname.replace("." + fext, "")

        fig.tight_layout()
        fig.savefig(f"{fname}-mix{q}.{fext}")
