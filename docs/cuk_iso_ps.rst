.. _sec-cuk-iso-ps:

cuk-iso-ps
======================

``cuk-iso-ps`` is a PCB used to assemble an isolated Ćuk converter, meant to be used as an experimental platform for research and teaching in control in power electronics. Assembling  one converter requires two ``cuk-iso-ps`` PCBs and a high-frequency transformer.  

Introduction
------------

A diagram of an isolated Ćuk converter is shown in :numref:`fig-cuk-iso-ps-diagram`.

.. figure:: media/cuk-iso/cuk-iso-ps-diagram.svg
   :name: fig-cuk-iso-ps-diagram
   :scale: 110%
   :align: center
   :alt: Diagram of the isolated Ćuk.
   
   Diagram of the isolated Ćuk converter.

To ease routing of the PCB and have flexibility with respect to the transformer, the converter is implemented with two PCBs, one for each side (primary and secondary). However, because the topology is symmetric, the same PCB can be used for both sides. A simplified diagram of one side is shown in :numref:`fig-cuk-iso-ps-diagram-simplified`. On the left, :math:`V_\text{dc}` is the voltage of the dc link, which can be either the input or output voltage, depending if the board is used for the primary or secondary side. On the right, the board is connected to a high-frequency transformer. (The polarity of the transformer must match the polarity shown in :numref:`fig-cuk-iso-ps-diagram`.)

.. figure:: media/cuk-iso/cuk-iso-ps-diagram-simplified.svg
   :name: fig-cuk-iso-ps-diagram-simplified
   :scale: 110%
   :align: center
   :alt: Simplified diagram of ``cuk-iso-ps``.
   
   Simplified diagram of the ``cuk-iso-ps`` board.

The full diagram of the board, including measurements and switches, is shown in :numref:`fig-cuk-iso-ps-diagram-full`. On the far left, :math:`v_\text{io}` is the input/output voltage, depending if the board is for the primary or secondary side. On the far right, :math:`v_\text{T}` is the connection to the high-frequency transformer. 

The ``cuk-iso-ps`` board is controlled with switches :math:`S_\text{L}`, :math:`S_\text{io}`, and :math:`S_\text{c}`. Switch :math:`S_\text{L}` is a low-side switch that can be used to switch a load to the output. This can be used to emulate load steps. Switch :math:`S_\text{io}` is a high-side switch can be used to disconnect the converter from its input/output. It was primarily meant to also emulate load steps, or, in case of faults, disconnecting the converter from its input or load. Switch :math:`S_\text{c}` is the main Ćuk switch.

.. figure:: media/cuk-iso/cuk-iso-diagram-full.svg
   :name: fig-cuk-iso-ps-diagram-full
   :scale: 110%
   :align: center
   :alt: Full diagram of ``cuk-iso-ps``.
   
   Full diagram of the ``cuk-iso-ps`` board.

The converter is monitored with three voltage sensors and two current sensors. The input (or output) voltage of the board is monitored with sensors :math:`v_\text{io}` and :math:`v_\text{dc}`. While :math:`v_\text{dc}` measures the voltage across the dc-link capacitor, :math:`v_\text{io}` measures the voltage after the :math:`S_\text{io}` switch. When the switch is closed, both measurements are the same. The voltage of the coupling capacitor is monitored with sensor :math:`v_\text{cc}`. The input (or output) current of the converter is measured with sensor :math:`i_\text{io}`, and the inductor current is monitored with sensor :math:`i_\text{L}`.

Converter and board pinout
--------------------------

:numref:`fig-cuk-iso-ps-board` shows the assembled converter, using two ``cuk-iso-ps`` boards and a high frequency transformer. The primary side is the input, while the secondary side is the output. The pinout of the board is shown in .

.. figure:: media/cuk-iso/board.svg
   :name: fig-cuk-iso-ps-board
   :scale: 12%
   :align: center
   :alt: Cuk converter assembled from two ``cuk-iso-ps`` boards.
   
   Ćuk converter assembled from two ``cuk-iso-ps`` boards.

Powering the board
------------------

Models
------

Known issues
------------

* :math:`S_\text{io}`
* Snubber
