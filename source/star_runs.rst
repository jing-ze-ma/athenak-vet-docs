Star runs
=========

2-D maps and movies of five 3-D runs of massive stars, each on one node of 4 H200 GPUs. The wall times, the
comparison with CPU runs and the cost of each module are on :doc:`performance`. How to set up a star run:
:doc:`stars`.

Each figure of one star shows three maps:

- left: the radial velocity :math:`v_r` in km/s at the photosphere of each column, Rosseland optical depth
  :math:`\tau_R = 2/3` (the same for all five stars; linear between cell centres, no smoothing);
- middle: the effective temperature :math:`T_{\rm eff}` in :math:`10^3` K of each column, from the comoving flux
  at its :math:`\tau_R = 2/3` (also the same for all five stars);
- right: the density relative to the mean of its shell, :math:`\delta\rho/\langle\rho\rangle`, on a slice in radius
  and angle. Grey is gas near the density floor (at most 1.5 times the floor).

Axes are in solar radii and degrees. :math:`R_{\rm ph,IC}` is the photosphere radius of the initial model. The scale
bar on the maps is a length at the median photosphere radius of the dump shown, exact at the equator: 10
:math:`R_\odot` for bsg, 1 for m35mms, 0.1 for m35zams, 100 for t9l62 and 10 for t9mlt.

Two notes on the velocity maps. Thin nested contour lines and small speckled patches inside some cells of the flow
(most clearly in m35mms, also in bsg and t9mlt) may come from the interpolation between radial cells or the search for
the photosphere; this was not examined. The t9l62 map shows mostly outflow at the photosphere.

.. figure:: star_runs/doc_strip.png
   :alt: radial velocity and effective temperature of the five stars
   :width: 100%

   The five stars at their newest dumps: :math:`v_r` (top) and :math:`T_{\rm eff}` (bottom). bsg at 57.0 d, m35mms at
   10.0 d, m35zams at 10.0 d, t9l62 at 27.75 d, t9mlt at 22.25 d. The wedges have different widths (see the axes), and
   each panel has its own colour limits.

Figures
-------

.. figure:: star_runs/doc_bsg.png
   :alt: 2-D maps of the bsg run
   :width: 100%

   bsg at its last dump, 57.0 d: 16.8 million cells, 57.0 d of model time in **6.0 h**. :math:`v_r` at
   :math:`\tau_R = 2/3` in each column; slice from 34 to 54 :math:`R_\odot` in the plane :math:`\phi = 0`.

.. figure:: star_runs/doc_m35mms.png
   :alt: 2-D maps of the m35mms run
   :width: 100%

   m35mms at its last dump, 10.0 d: 22.0 million cells, 10.0 d of model time in **19.9 h** (two builds, one
   restart). :math:`v_r` at :math:`\tau_R = 2/3` in each column; slice from 0.86 to 1.06
   :math:`R_{\rm ph,IC}` in the equatorial plane. Surface and envelope only; the velocity of the deep stable layer is
   not shown.

.. figure:: star_runs/doc_m35zams.png
   :alt: 2-D maps of the m35zams run
   :width: 100%

   m35zams at its last dump, 10.0 d: 6.3 million cells, 10.0 d of model time in **20.1 h** (two builds, one
   restart). :math:`v_r` at :math:`\tau_R = 2/3` in each column; slice from 0.95 to 1.02
   :math:`R_{\rm ph,IC}` in the equatorial plane.

.. figure:: star_runs/doc_t9l62.png
   :alt: 2-D maps of the t9l62 run
   :width: 100%

   t9l62 at 27.75 d: 67.1 million cells, **18.6 h** up to 26.5 d (two builds, one restart; the run continues).
   :math:`v_r` at :math:`\tau_R = 2/3` in each column; slice from 0.42 to 7.0 :math:`R_{\rm ph,IC}` in the
   equatorial plane. Surface and envelope only; the velocity of the deep stable layer is not shown.

.. figure:: star_runs/doc_t9mlt.png
   :alt: 2-D maps of the t9mlt run
   :width: 100%

   t9mlt (adaptive mixing-length start) at 22.25 d: 67.1 million cells, **16.0 h** up to 21.5 d (one build; the run
   continues). A partial-test run, not a validated prediction. :math:`v_r` at :math:`\tau_R = 2/3` in each
   column; slice from 0.62 to 1.12 :math:`R_{\rm ph,IC}` in the equatorial plane. Surface and envelope only; the
   velocity of the deep stable layer is not shown.

Movies
------

The same three maps in time, from the start of the run to the day given, every dump, with fixed colour limits. No
sound. Press play; the bsg, t9l62 and t9mlt movies last 10 s, the m35 movies 40 s.

.. raw:: html

   <video controls muted playsinline preload="metadata" width="100%"
          poster="_static/star_runs/mov_bsg_poster.png" src="_static/star_runs/mov_bsg.mp4">
   </video>

bsg, 0 to 57.0 d: all 115 dumps, 12 h apart, at 24 frames per second. **6.0 h** on one node.

.. raw:: html

   <video controls muted playsinline preload="metadata" width="100%"
          poster="_static/star_runs/mov_m35mms_poster.png" src="_static/star_runs/mov_m35mms.mp4">
   </video>

m35mms, 0 to 10.0 d: all 481 dumps, 30 min apart, at 12 dumps per second (40 s, 30 frames per second). **19.9
h** on one node. Frames interpolated: cross-faded between dumps, so a frame between two dumps is a mix of two
states of the flow; the time stamp is not blended. Surface and envelope only; the velocity of the deep stable
layer is not shown.

.. raw:: html

   <video controls muted playsinline preload="metadata" width="100%"
          poster="_static/star_runs/mov_m35zams_poster.png" src="_static/star_runs/mov_m35zams.mp4">
   </video>

m35zams, 0 to 10.0 d: all 481 dumps, 30 min apart, at 12 dumps per second (40 s, 30 frames per second). **20.1
h** on one node. Frames interpolated: cross-faded between dumps.

.. raw:: html

   <video controls muted playsinline preload="metadata" width="100%"
          poster="_static/star_runs/mov_t9l62_poster.png" src="_static/star_runs/mov_t9l62.mp4">
   </video>

t9l62, 0 to 27.75 d (the run continues): all 223 dumps, 3 h apart, at 24 frames per second. **18.6 h** on one
node up to 26.5 d. The colour limits of :math:`T_{\rm eff}` are 4.9 to 10.0 :math:`\times 10^3` K, so the
first, hotter days are saturated. Surface and envelope only; the velocity of the deep stable layer is not
shown.

.. raw:: html

   <video controls muted playsinline preload="metadata" width="100%"
          poster="_static/star_runs/mov_t9mlt_poster.png" src="_static/star_runs/mov_t9mlt.mp4">
   </video>

t9mlt, 0 to 22.25 d (the run continues): all 179 dumps, 3 h apart, at 24 frames per second. **16.0 h** on one
node up to 21.5 d. The colour limits of :math:`T_{\rm eff}` are 9.0 to 29.5 :math:`\times 10^3` K. A
partial-test run, not a validated prediction. Surface and envelope only; the velocity of the deep stable layer is not
shown.

3-D videos
----------

Perspective view with a fixed camera. The surface is the photosphere (:math:`\tau_R = 2/3`), coloured by
:math:`T_{\rm eff} = (F_r/\sigma)^{1/4}` with the lab-frame flux; the relief is at true scale. A quarter is cut
out, and its faces are coloured by :math:`v_r` out to the local photosphere. The scale bar is exact at the depth of the near side
of the photosphere: 10 :math:`R_\odot` for bsg, 1 for m35mms, 0.1 for m35zams, 100 for t9l62 and 10 for t9mlt. Softer
lighting (t9l62, t9mlt) means an ambient share of 0.8: the lit colour is 0.83 to 1.01 of the colour bar. No sound.

.. raw:: html

   <video controls muted playsinline preload="none" width="100%"
          poster="_static/star_runs/mov3d_bsg_poster.png" src="_static/star_runs/mov3d_bsg.mp4">
   </video>

bsg.

.. raw:: html

   <video controls muted playsinline preload="none" width="100%"
          poster="_static/star_runs/mov3d_m35mms_poster.png" src="_static/star_runs/mov3d_m35mms.mp4">
   </video>

m35mms. Frames interpolated: cross-faded between dumps. The cut faces start at 0.86 :math:`R_{\rm ph,IC}`.

.. raw:: html

   <video controls muted playsinline preload="none" width="100%"
          poster="_static/star_runs/mov3d_m35zams_poster.png" src="_static/star_runs/mov3d_m35zams.mp4">
   </video>

m35zams. Frames interpolated: cross-faded between dumps. The cut faces start at 0.93 :math:`R_{\rm ph,IC}`.

.. raw:: html

   <video controls muted playsinline preload="none" width="100%"
          poster="_static/star_runs/mov3d_t9l62_poster.png" src="_static/star_runs/mov3d_t9l62.mp4">
   </video>

t9l62. The movie starts at 9.5 d, and its first five days are saturated (:math:`T_{\rm eff}` limits 4.9 to
10.0 :math:`\times 10^3` K). The cut faces start at 0.42 :math:`R_{\rm ph,IC}`. The surface has softer
lighting.

.. raw:: html

   <video controls muted playsinline preload="none" width="100%"
          poster="_static/star_runs/mov3d_t9mlt_poster.png" src="_static/star_runs/mov3d_t9mlt.mp4">
   </video>

t9mlt. :math:`T_{\rm eff}` limits 9.0 to 29.5 :math:`\times 10^3` K. The cut faces start at 0.62 :math:`R_{\rm
ph,IC}`. The surface has softer lighting. A partial-test run, not a validated prediction.
