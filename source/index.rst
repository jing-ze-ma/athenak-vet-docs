AthenaK VET radiation documentation
===================================

.. image:: /_static/vet_hero.png
   :alt: 3-D star tests: a blue-supergiant envelope on a spherical-polar wedge (left) and a red supergiant on a cubed sphere (right)
   :align: center
   :width: 100%

The clean VET scheme is a grey radiation-hydrodynamics scheme for
`AthenaK <https://github.com/IAS-Astrophysics/athenak>`_ (``src/rad_vet/``,
``<rad_vet>/scheme = clean``): two-moment radiation transport with the energy density on
cells and the flux on cell faces, closed by a variable Eddington tensor from
short-characteristic ray sweeps, integrated with an IMEX SDIRK2 scheme (implicit radiation
and gas-radiation exchange, explicit AthenaK hydrodynamics), in a well-balanced formulation
for stellar envelopes.

**57 days of a blue supergiant in 6.0 hours on one node of 4 H200**: wall times of the star runs,
a comparison with Athena++ on CPUs and where the time goes are on :doc:`performance`.

Figures and movies of the five star runs are on :doc:`star_runs`.

Its properties, each with how it is achieved and the test that shows it, are on
:doc:`properties`: energy and mass conserved to round-off; :math:`L_z` exact on the cubed
sphere (on spherical polar exact except where the face-flux cone cut acts, booked in a
ledger); positivity of the density by construction; well-balanced envelopes; measured order of accuracy (see :doc:`properties`);
bitwise restarts, dt retries and rank counts; CPU and GPU agreement to round-off;
Cartesian, spherical-polar and cubed-sphere meshes with one implementation.

The release code is the ``vet-clean-release`` branch of
`github.com/jing-ze-ma/athenak <https://github.com/jing-ze-ma/athenak/tree/vet-clean-release>`_.

This site covers how to obtain, build and run the code, the method and its tests. Worked
problems with notebooks are in the companion repository
`athenak-vet-gallery <https://github.com/jing-ze-ma/athenak-vet-gallery>`_ (:doc:`gallery`).

.. toctree::
   :caption: Getting Started
   :maxdepth: 1

   requirements
   download
   build

.. toctree::
   :caption: Quickstart
   :maxdepth: 1

   quickstart

.. toctree::
   :caption: Performance
   :maxdepth: 1

   performance

.. toctree::
   :caption: Gallery
   :maxdepth: 1

   star_runs

.. toctree::
   :caption: Running
   :maxdepth: 1

   running_the_code
   input_file
   outputs
   analysis
   notes_specific_machines

.. toctree::
   :caption: The VET scheme
   :maxdepth: 1

   scheme
   properties

.. toctree::
   :caption: Reference
   :maxdepth: 1

   keys
   tests

.. toctree::
   :caption: Worked problems
   :maxdepth: 1

   stars
   gallery

.. toctree::
   :caption: Help
   :maxdepth: 1

   faq

.. rubric:: About this site

The layout, theme, style sheet and publishing workflow of this site, and the separate
tutorial repository, follow the `IAS AthenaK documentation
<https://github.com/IAS-Astrophysics/athenak-docs>`_ and `AthenaK gallery
<https://github.com/IAS-Astrophysics/athenak-gallery>`_; we thank their authors. The text of
most pages is generated from ``docs/vet_clean/`` of the code repository
(``tools/sync_from_code.py``).
