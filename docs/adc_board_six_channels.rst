.. _sec-adc-board-six-channels:

adc-board-six-channels
======================

The ``adc-board-six-channels`` is a board containing six ADCs, intended for single-ended measurements. The boad supports ADCs with SOT-23-6 package and SPI interface.

A diagram of the board is shown in  :numref:`fig-adc-board-six-channels-diagram`, where:

* :math:`\text{V}_\text{CC}` and :math:`\text{V}_\text{DD}` are supply inputs. The ADCs can be supplied either with :math:`\text{V}_\text{CC}` (typically 3V3) or :math:`\text{V}_\text{DD}` (typically 5V). This depends on the specific ADC mounted on the board.
* :math:`\text{A}_1, \dots, \text{A}_6` are the analog inputs.
* :math:`\bar{\text{CS}}` and :math:`\text{CLK}` are the chip select and clock signals. These two signals are shared among all ADCs on the board.
* :math:`\text{SD}_1, \dots, \text{SD}_6` are the data outputs of the ADCs.

.. figure:: img/adc-board-six-channels/diagram.svg
   :name: fig-adc-board-six-channels-diagram
   :scale: 150%
   :align: center
   :alt: Diagram of the board.
   
   Diagram of the board.

Board pinout
------------



ADC compability
---------------

Single input diagram
--------------------


Isolation
---------

Voltage supply
--------------

Fabrication files
-----------------
