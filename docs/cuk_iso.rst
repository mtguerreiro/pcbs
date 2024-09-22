.. _sec-cuk-iso:

cuk-iso
======================

``cuk-iso`` is a PCB used to assemble an isolated Ćuk converter, meant to be used as an experimental platform for research and teaching in control in power electronics. Assembling  one converter requires two ``cuk-iso`` PCBs and a high-frequency transformer.  

Introduction
------------

A diagram of an isolated Ćuk converter is shown in :numref:`fig-cuk-iso-diagram`.

.. figure:: media/cuk-iso/cuk-iso-diagram.svg
   :name: fig-cuk-iso-diagram
   :scale: 110%
   :align: center
   :alt: Diagram of the isolated Ćuk.
   
   Diagram of the isolated Ćuk converter.

To ease routing of the PCB and have flexibility with respect to the transformer, the converter is implemented with two PCBs, one for each side (primary and secondary). However, because the topology is symmetric, the same PCB can be used for both sides. A simplified diagram of one side is shown in :numref:`fig-cuk-iso-diagram-simplified`. On the left, :math:`V_\text{dc}` is the voltage of the dc link, which can be either the input or output voltage, depending if the board is used for the primary or secondary side. On the right, the board is connected to a high-frequency transformer. (The polarity of the transformer must match the polarity shown in :numref:`fig-cuk-iso-diagram`.)

.. figure:: media/cuk-iso/cuk-iso-diagram-simplified.svg
   :name: fig-cuk-iso-diagram-simplified
   :scale: 110%
   :align: center
   :alt: Simplified diagram of ``cuk_iso``.
   
   Simplified diagram of the ``cuk_iso`` board.

The full diagram of the board, including measurements and switches, is shown in :numref:`fig-cuk-iso-diagram-full`. On the far left, :math:`v_\text{io}` is the input/output voltage, depending if the board is for the primary or secondary side. On the far right, :math:`v_\text{T}` is the connection to the high-frequency transformer. 

The ``cuk_iso`` board is controlled with switches :math:`S_\text{L}`, :math:`S_\text{io}`, and :math:`S_\text{c}`. Switch :math:`S_\text{L}` is a low-side switch that can be used to switch a load to the output. This can be used to emulate load steps.Switch :math:`S_\text{io}` is a high-side switch can be used to disconnect the converter from its input/output. It was primarily meant to also emulate load steps, or, in case of faults, disconnecting the converter from its input or load. Switch :math:`S_\text{c}` is the main Ćuk switch.

.. figure:: media/cuk-iso/cuk-iso-diagram-full.svg
   :name: fig-cuk-iso-diagram-full
   :scale: 110%
   :align: center
   :alt: Full diagram of ``cuk_iso``.
   
   Full diagram of the ``cuk_iso`` board.

Known issues
------------

* :math:`S_\text{io}`
* Snubber
