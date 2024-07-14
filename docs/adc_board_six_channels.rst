.. _sec-adc-board-six-channels:

adc-board-six-channels
======================

The ``adc-board-six-channels`` is a board containing six ADCs, intended for single-ended measurements. The boad supports ADCs with SOT-23-6 package and SPI interface.

A diagram of the board is shown in  :numref:`fig-adc-board-six-channels-diagram`, where:

* Signals :math:`\text{A}_1, \dots, \text{A}_6` are the analog inputs.
* :math:`\bar{\text{CS}}` and :math:`\text{CLK}` are the chip select and clock signals. These two signals are shared between all ADCs on the board.
* :math:`\text{SD}_1, \dots, \text{SD}_6` are the data outputs of the ADCs.

.. figure:: img/adc-board-six-channels/diagram.svg
   :name: fig-adc-board-six-channels-diagram
   :scale: 150%
   :align: center
   :alt: Diagram of the board.
   
   Diagram of the board.


