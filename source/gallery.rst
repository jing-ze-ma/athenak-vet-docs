Gallery
=======

Worked problems live in a separate repository,
`athenak-vet-gallery <https://github.com/jing-ze-ma/athenak-vet-gallery>`_, one folder per
problem: a README with the steps, the input deck(s) and a Jupyter notebook, executed, with
its plots. The test notebooks run their test through the suite of the code repository
(``tests/vet_clean``), so they need a checkout and a CPU build (:doc:`build`, block 3a):

.. code-block:: bash

   git clone https://github.com/jing-ze-ma/athenak-vet-gallery.git
   export ATHENAK=$PWD/athenak                         # your athenak checkout
   export ATHENA_EXE=$ATHENAK/build_tests/src/athena   # its CPU build
   cd athenak-vet-gallery/radwave
   jupyter nbconvert --to notebook --execute --inplace radwave.ipynb

.. list-table::
   :header-rows: 1
   :widths: 18 30 52

   * - folder
     - suite tests
     - shows (property: :doc:`properties`)
   * - ``star3d-sp``
     - (3-D star, spherical polar)
     - a blue-supergiant envelope on a 60 deg wedge, 4 GPUs: luminosity, slices, profiles (:doc:`stars`)
   * - ``star3d-cs``
     - (3-D star, cubed sphere)
     - a 20.5 Msun red supergiant on the full sphere, 4 GPUs (:doc:`stars`)
   * - ``conservation``
     - ``conservation_sp``, ``conservation_cs``
     - drift of total energy, mass and :math:`L_z` vs cycle
   * - ``restart``
     - ``restart_sp``, ``restart_cs``
     - straight vs restarted run: the difference (0)
   * - ``radwave``
     - ``radwave``
     - radiation-acoustic waves: phase-speed and damping errors vs the trapping parameter
   * - ``wedge_sym``
     - ``wedge_sym``
     - phi mirror symmetry on narrow wedges: wedge-mean :math:`F_\phi` vs the criterion
   * - ``well_balance``
     - ``wb_sp``, ``wb_cs``
     - max :math:`|v|/c_s` vs time of an equilibrium envelope
   * - ``order``
     - ``order_time``, ``order_space``
     - L1 error vs dt and vs N, with a slope-2 line
   * - ``thermal_eq``
     - ``thermal_eq``
     - E(t), T(t) vs the exact ODE
   * - ``nlte``
     - ``nlte_eps1e-1``, ``nlte_eps1e-4``
     - J vs tau against the exact solution
   * - ``momentum_box``
     - ``momentum_box``
     - linear-momentum drift (a report, no criterion)
   * - ``floor_pay``
     - ``floor_pay``
     - total-energy drift with floors paid from the radiation
