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

import cantera as ct
import pandas as pd

ct.suppress_thermo_warnings()


def ignition_delay(gas):
    """
    Returns an ignition delay time from a Cantera Solution object.

    Set desired temperature, pressure, and composition before calling.

    This function currently returns the maximum rate of pressure rise as the IDT.
    If the returned value is 1 second, the mixture did not ignite (max. simulation time).
    """

    r = ct.IdealGasReactor(contents=gas, name="Batch Reactor")
    reactorNetwork = ct.ReactorNet([r])

    # This is a starting estimate. If you do not get an ignition within this time, increase it
    estimatedIgnitionDelayTime = 1.0
    t = 0

    # chemical or pressure-based IDT?
    # Chem IDT for peak OH concentration used for HONO vs HNO2 ProCI
    ChemIDT = False

    if ChemIDT:
        # now compile a list of all variables for which we will store data
        stateVariableNames = [r.component_name(item) for item in range(r.n_vars)]
        # use the above list to create a DataFrame
        timeHistory = pd.DataFrame(columns=stateVariableNames)
    else:
        # data frame to store only pressure history
        pressuretime = pd.DataFrame(columns=["time", "pressure"])

    counter = 1
    while t < estimatedIgnitionDelayTime:
        t = reactorNetwork.step()
        if counter % 10 == 0:
            # We will save only every 10th value. Otherwise, this takes too long
            # Note that the species concentrations are mass fractions
            if ChemIDT:
                timeHistory.loc[t] = reactorNetwork.get_state()
            else:
                pressuretime.loc[t] = t, gas.P
        counter += 1

    if ChemIDT:
        # We will use the 'oh' species to compute the ignition delay
        # time if maximum OH
        tau = timeHistory["OH"].idxmax()
    else:
        # dp/dt IDT
        dpdtdf = pressuretime.diff()
        dpdtdf["dPdt"] = dpdtdf["pressure"] / dpdtdf["time"]
        tau = dpdtdf["dPdt"].idxmax()

    return tau
