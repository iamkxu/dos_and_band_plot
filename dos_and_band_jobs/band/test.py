import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib.pyplot as plt


run = BSVasprun('./vasprun.xml', parse_projected_eigen=True)
bs = run.get_band_structure("KPOINTS")


n = 0
for kpoints, e in zip(bs.kpoints, bs.bands[Spin.up][9,:]):
    n += 1
    if n == 11:
        print('...')
    if 10 < n < 90:
        continue
    print("kx = %5.3f ky = %5.3f kz = %5.3f eps(k) = %8.4f" %(tuple(kpoints.frac_coords) + (e,)))


bsplot = BSPlotter(bs)
bsplot.get_plot(ylim=(-20, 10), zero_to_efermi=True)
print(bs.efermi)
ax = plt.gca()
ax.set_title("NiO Band Structure", fontsize=20)
xlim = ax.get_xlim()
ax.hlines(0, xlim[0], xlim[1], linestyles='dashed', color='black')
ax.plot((), (), 'b-', label="spin up")
ax.plot((), (), 'r--', label="spin down")
ax.legend(fontsize=16, loc='upper left')
#  plt.show()
