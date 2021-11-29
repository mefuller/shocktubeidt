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
tabcolors = list(mcolors.TABLEAU_COLORS)

def line_colors(n: int, cmap: list = None):
    """
    With n lines and given colormap, cmap, return evenly spaced set of colors
    for plotting. If using multiple line styles (quantity s), recommend passing
    n%s as first argument to utilize more widely-spaced colors.
    Default to using cividis color map with option to override.
    """
    print(n)
    # cividis color map values from
    # https://github.com/pnnl/cmaputil/blob/master/colormaps/cividisHexValues.txt
    if cmap is None:
        cmap = [
            "#00204c",
            "#00204e",
            "#002150",
            "#002251",
            "#002353",
            "#002355",
            "#002456",
            "#002558",
            "#00265a",
            "#00265b",
            "#00275d",
            "#00285f",
            "#002861",
            "#002963",
            "#002a64",
            "#002a66",
            "#002b68",
            "#002c6a",
            "#002d6c",
            "#002d6d",
            "#002e6e",
            "#002e6f",
            "#002f6f",
            "#002f6f",
            "#00306f",
            "#00316f",
            "#00316f",
            "#00326e",
            "#00336e",
            "#00346e",
            "#00346e",
            "#01356e",
            "#06366e",
            "#0a376d",
            "#0e376d",
            "#12386d",
            "#15396d",
            "#17396d",
            "#1a3a6c",
            "#1c3b6c",
            "#1e3c6c",
            "#203c6c",
            "#223d6c",
            "#243e6c",
            "#263e6c",
            "#273f6c",
            "#29406b",
            "#2b416b",
            "#2c416b",
            "#2e426b",
            "#2f436b",
            "#31446b",
            "#32446b",
            "#33456b",
            "#35466b",
            "#36466b",
            "#37476b",
            "#38486b",
            "#3a496b",
            "#3b496b",
            "#3c4a6b",
            "#3d4b6b",
            "#3e4b6b",
            "#404c6b",
            "#414d6b",
            "#424e6b",
            "#434e6b",
            "#444f6b",
            "#45506b",
            "#46506b",
            "#47516b",
            "#48526b",
            "#49536b",
            "#4a536b",
            "#4b546b",
            "#4c556b",
            "#4d556b",
            "#4e566b",
            "#4f576c",
            "#50586c",
            "#51586c",
            "#52596c",
            "#535a6c",
            "#545a6c",
            "#555b6c",
            "#565c6c",
            "#575d6d",
            "#585d6d",
            "#595e6d",
            "#5a5f6d",
            "#5b5f6d",
            "#5c606d",
            "#5d616e",
            "#5e626e",
            "#5f626e",
            "#5f636e",
            "#60646e",
            "#61656f",
            "#62656f",
            "#63666f",
            "#64676f",
            "#65676f",
            "#666870",
            "#676970",
            "#686a70",
            "#686a70",
            "#696b71",
            "#6a6c71",
            "#6b6d71",
            "#6c6d72",
            "#6d6e72",
            "#6e6f72",
            "#6f6f72",
            "#6f7073",
            "#707173",
            "#717273",
            "#727274",
            "#737374",
            "#747475",
            "#757575",
            "#757575",
            "#767676",
            "#777776",
            "#787876",
            "#797877",
            "#7a7977",
            "#7b7a77",
            "#7b7b78",
            "#7c7b78",
            "#7d7c78",
            "#7e7d78",
            "#7f7e78",
            "#807e78",
            "#817f78",
            "#828078",
            "#838178",
            "#848178",
            "#858278",
            "#868378",
            "#878478",
            "#888578",
            "#898578",
            "#8a8678",
            "#8b8778",
            "#8c8878",
            "#8d8878",
            "#8e8978",
            "#8f8a78",
            "#908b78",
            "#918c78",
            "#928c78",
            "#938d78",
            "#948e78",
            "#958f78",
            "#968f77",
            "#979077",
            "#989177",
            "#999277",
            "#9a9377",
            "#9b9377",
            "#9c9477",
            "#9d9577",
            "#9e9676",
            "#9f9776",
            "#a09876",
            "#a19876",
            "#a29976",
            "#a39a75",
            "#a49b75",
            "#a59c75",
            "#a69c75",
            "#a79d75",
            "#a89e74",
            "#a99f74",
            "#aaa074",
            "#aba174",
            "#aca173",
            "#ada273",
            "#aea373",
            "#afa473",
            "#b0a572",
            "#b1a672",
            "#b2a672",
            "#b4a771",
            "#b5a871",
            "#b6a971",
            "#b7aa70",
            "#b8ab70",
            "#b9ab70",
            "#baac6f",
            "#bbad6f",
            "#bcae6e",
            "#bdaf6e",
            "#beb06e",
            "#bfb16d",
            "#c0b16d",
            "#c1b26c",
            "#c2b36c",
            "#c3b46c",
            "#c5b56b",
            "#c6b66b",
            "#c7b76a",
            "#c8b86a",
            "#c9b869",
            "#cab969",
            "#cbba68",
            "#ccbb68",
            "#cdbc67",
            "#cebd67",
            "#d0be66",
            "#d1bf66",
            "#d2c065",
            "#d3c065",
            "#d4c164",
            "#d5c263",
            "#d6c363",
            "#d7c462",
            "#d8c561",
            "#d9c661",
            "#dbc760",
            "#dcc860",
            "#ddc95f",
            "#deca5e",
            "#dfcb5d",
            "#e0cb5d",
            "#e1cc5c",
            "#e3cd5b",
            "#e4ce5b",
            "#e5cf5a",
            "#e6d059",
            "#e7d158",
            "#e8d257",
            "#e9d356",
            "#ebd456",
            "#ecd555",
            "#edd654",
            "#eed753",
            "#efd852",
            "#f0d951",
            "#f1da50",
            "#f3db4f",
            "#f4dc4e",
            "#f5dd4d",
            "#f6de4c",
            "#f7df4b",
            "#f9e049",
            "#fae048",
            "#fbe147",
            "#fce246",
            "#fde345",
            "#ffe443",
            "#ffe542",
            "#ffe642",
            "#ffe743",
            "#ffe844",
            "#ffe945",
        ]

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

def comp_mech_data(mixes, mechs, temps, IDTs, ofname, Tdata, Taudata):
    """
    Routine to plot comparison of igntion delay times for matrix of mechanisms and compositions.
    Compares IDT of different mechanisms for each mixtures.
    Prints and saves plot showing absolute values and relative times.
    **hacked up right now to plot one data set on first figure**
    **also hacked to change up colors/styles**
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
        if q == 0:
            plt.semilogy(
                    (1000.0 / Tdata),
                    Taudata,
                    ls='none',
                    marker=markers[0],
                    ms=8,
                    markerfacecolor='none',
                    markeredgewidth=1,
                    color=colors[1],
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
                color=colors[w % len(colors)],
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
