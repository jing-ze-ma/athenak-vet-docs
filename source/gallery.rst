Notebooks
=========

Worked problems live in a separate repository,
`athenak-vet-notebooks <https://github.com/jing-ze-ma/athenak-vet-notebooks>`_, one folder per
problem: a README with the steps, the input deck(s) and a Jupyter notebook, executed, with
its plots. The test notebooks run their test through the suite of the code repository
(``tests/vet_clean``), so they need a checkout and a CPU build (:doc:`build`, block 3a):

.. code-block:: bash

   git clone https://github.com/jing-ze-ma/athenak-vet-notebooks.git
   export ATHENAK=$PWD/athenak                         # your athenak checkout
   export ATHENA_EXE=$ATHENAK/build_tests/src/athena   # its CPU build
   cd athenak-vet-notebooks/radwave
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
     - ``order_time``, ``order_space``, ``order_stiff``
     - L1 error vs dt, vs N and vs the steps per period (stiff exchange), with a slope-2 line
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
   * - ``beams_shadow``
     - ``idort_beams``, ``idort_beams_mb``, ``idort_shadow``, ``idort_shadow_gl``
     - crossing beams (with a beam-width ladder) and the shadow of an ellipse vs the exact beams
   * - ``cylinder``
     - ``idort_cylinder``
     - E, energy flux and face momentum around an emitting cylinder vs exact transport
   * - ``radshock``
     - ``radshock``, ``radshock_m5``
     - Lowrie & Edwards radiative shocks vs the semi-analytic profiles
