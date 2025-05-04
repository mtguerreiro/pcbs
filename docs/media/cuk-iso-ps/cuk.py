import os

import plecsutil as pu

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

import my_matplotlib_themes as mmt
mmt.my_themes.default_tex_report()

# --- Run the simulation  ---
##plecs_file = 'cuk-iso-prototype'
##plecs_file_path = os.path.abspath(os.getcwd())
##
##pm = pu.ui.PlecsModel(
##    plecs_file, plecs_file_path,
##    {},
##    )
##
##data = pm.sim(close_sim=True)
##
##pu.ui.save_data('cuk_plecs', data)

# --- Load data ---
sim = pu.ui.load_data('cuk_plecs')
sim.t = (sim.t - 25e-3 + 2.48e-3) / 1e-3

hw = pu.ui.load_data('cuk_hw')
hw.t = 1 / 100e3 * np.arange(hw.data.shape[0]) / 1e-3

# --- Plot ---

fig, ax = plt.subplots(6, 1, figsize=(7.5, 9.6), sharex=True)

ax[0] = plt.subplot(6,1,1)
ax[0].set_xlim([2.25, 6.25])

ax[0].set_title('Duty-cycle')
ax[0].step(hw.t, hw.data[:, 10], 'C0')
ax[0].step(sim.t, sim.data[:, -1], 'C2')
ax[0].set_ylim([0.34, 0.46])
ax[0].set_yticks([0.35, 0.4, 0.45])
ax[0].set_ylabel('Duty-cycle')

ax[1].set_title('Input inductor current')
ax[1].step(hw.t, hw.data[:, 1], 'C0')
ax[1].step(sim.t, sim.data[:, 0], 'C2')
ax[1].set_ylim([1, 11])
ax[1].set_yticks([2, 6, 10])
ax[1].set_ylabel('Current (A)')

ax[2].set_title('Output inductor current')
ax[2].step(hw.t, hw.data[:, 6], 'C0')
ax[2].step(sim.t, sim.data[:, 1], 'C2')
ax[2].set_ylim([1, 8])
ax[2].set_yticks([2, 4.5, 7])
ax[2].set_ylabel('Current (A)')

ax[3].set_title('Primary-side coupling cap. voltage')
ax[3].step(hw.t, hw.data[:, 4], 'C0')
ax[3].step(sim.t, sim.data[:, 2], 'C2')
ax[3].set_ylim([9, 19])
ax[3].set_yticks([10, 14, 18])
ax[3].set_ylabel('Voltage (V)')

ax[4].set_title('Secondary-side coupling cap. voltage')
ax[4].step(hw.t, hw.data[:, 9], 'C0')
ax[4].step(sim.t, sim.data[:, 3], 'C2')
ax[4].set_ylim([10, 22])
ax[4].set_yticks([12, 16, 20])
ax[4].set_ylabel('Voltage (V)')

ax[5].set_title('Output voltage')
ax[5].step(hw.t, hw.data[:, 8], 'C0', label='Hardware')
ax[5].step(sim.t, sim.data[:, 4], 'C2', label='Simulation')
ax[5].set_ylim([11, 21])
ax[5].set_yticks([12, 16, 20])
ax[5].set_ylabel('Voltage (V)')
ax[5].set_xlabel('Time (ms)')

fig.legend(
    loc='lower center',         # Bottom center of the figure
    ncol=2,                     # Number of columns (adjust as needed)
    bbox_to_anchor=(0.5, -0.03) # Fine-tune position: (x, y) relative to figure
)

plt.savefig('cuk-iso-prototype-model-val-sim-hw.svg')
