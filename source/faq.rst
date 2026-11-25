FAQ
===

**My GPU binary runs, but the photosphere never free-streams.**
  The CUDA 12.2 + GCC 11 toolchain on H200 builds a binary whose ray closure is wrong (the
  Eddington tensor stays at I/3 in the thin atmosphere) without any error. Build with CUDA
  12.9 + GCC 13, and check every new GPU binary with the suite (:doc:`build`,
  :doc:`notes_specific_machines`).

**The test decks do not run with my star binary.**
  A binary built with ``-D PROBLEM=star_vet`` runs only that problem generator. Build the
  test binary without ``-D PROBLEM``, in a second build directory (:doc:`build`).

**A run started without** ``mpirun`` **takes minutes instead of seconds.**
  Open MPI binds the process to one core, so the OpenMP threads share it. Set
  ``OMPI_MCA_hwloc_base_binding_policy=none``, or start with ``mpirun -np 1 --bind-to none``
  (:doc:`quickstart`).

**The build was killed on the login node.**
  Many sites limit login-node CPU time; build inside a compute job (:doc:`build`).

**My restart does not behave like the run it continues.**
  On a restart, a key that is not given in the deck or on the command line takes the value
  stored in the restart file, not the code default. Name every production key when you
  restart from a file written with other keys (:doc:`input_file`).

**My wedge run stops with a FATAL about the azimuthal period.**
  On a phi-periodic wedge the width must be a whole number of the ray set's azimuthal
  periods (GL :math:`n_\theta \times n_\phi`: 360 deg / :math:`n_\phi`; LQ10: 90 deg; the
  default icosahedral set: 180 deg). A narrower wedge names ``vet_gd_wall_sym = true`` with
  ``vet_gd_wall_interp = true`` (:doc:`properties`, :doc:`keys`).

**A cubed-sphere run hangs on MI300A.**
  With ROCm 7.2, more than 2 ranks per MI300A on a cubed-sphere mesh hang unless
  ``GPU_MAX_HW_QUEUES=2`` is set; the code stops with a FATAL message that says so. Also set
  ``export HSA_XNACK=1`` before every MI300A run (:doc:`build`).

**An A100 run on a spherical-polar wedge runs out of memory.**
  Name ``vet_gd_band_ring = true`` in ``<rad_vet>``: the same results bit for bit, less memory
  (:doc:`running_the_code`).

**What does a** ``CLEAN WARNING`` **line mean?**
  A handled event that changed the method or created energy; a healthy run prints none.
  Each message is explained on :doc:`outputs`.

**Why is my run slow?**
  ``<hydro>/dt_report = N`` prints which cell and which term set dt (:doc:`running_the_code`).

**Is linear momentum conserved?**
  Not in general; energy, mass and (on the cubed sphere) :math:`L_z` are. What changes it and
  by how much: :doc:`properties`.

**Do CPU and GPU runs agree bit for bit?**
  No, to round-off: the math libraries differ between backends. Restarts, dt retries and
  rank counts are bitwise (:doc:`properties`).

**How do I cite the scheme?**
  See :doc:`scheme`, "How to cite".
