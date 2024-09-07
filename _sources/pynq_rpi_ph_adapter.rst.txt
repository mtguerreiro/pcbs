.. _sec-pynq-rpi-ph-adapter:

pynq-rpi-ph-adapter
===================

``pynq-rpi-ph-adapter`` is an adapter board that routes all Raspberry and Arduino GPIOs of the Pynq Z2 board to side connectors that are compatible with boards such as :ref:`sec-adc-board-six-channels`, :ref:`sec-digital-isolator-2t6r`, and :ref:`sec-digital-isolator-6t2r`. In total, 48 GPIOs are made available in six different connectors (8 GPIOs per connector).

Board and pinout
----------------

A partially populated board mounted on a Pynq Z2 board is shown in :numref:`fig-pynq-rpi-ph-adapter-board`. The board's pinout is shown in :numref:`fig-pynq-rpi-ph-adapter-pinout`. The mapping between the IOs, equivalent Raspberry/Arduino pins and the actual FPGA pins are shown in Table :ref:`table-pynq-rpi-ph-adapter-pin-mapping`.

.. figure:: media/pynq-rpi-ph-adapter/board.svg
   :name: fig-pynq-rpi-ph-adapter-board
   :scale: 10%
   :align: center
   :alt: Pynq adapter on Pynq board.
   
   Adapter board mounted on a Pynq Z2.


.. figure:: media/pynq-rpi-ph-adapter/pinout.svg
   :name: fig-pynq-rpi-ph-adapter-pinout
   :scale: 150%
   :align: center
   :alt: Pinout of the board.
   
   Board pinout.

.. _table-pynq-rpi-ph-adapter-pin-mapping:

.. csv-table:: Pin mapping
   :file: media/pynq-rpi-ph-adapter/pinout.csv
   :widths: 40, 40, 40, 40, 40, 40
   :header-rows: 1

Compatible boards
-----------------

Some boards that compatible with the ``pynq-rpi-ph-adapter`` are:

* :ref:`sec-adc-board-six-channels`
* :ref:`sec-digital-isolator-2t6r`
* :ref:`sec-digital-isolator-6t2r`

Connecting compatible boards
----------------------------

There are two possibilities when using the ``pynq-rpi-ph-adapter`` with compatible boards. The first option is to solder pin headers on the top of the board, and simply attach a compatible board. The second option is to attach compatible boards via ribbon cables. In this case, the headers must be soldered on the bottom of the adapter board. This is because the ribbon cable matches the pins on both connectors one-to-one, but we need them to be mirrored. For an example of connection via ribbon cables, see :ref:`sec-pynq-rpi-ph-adapter-example`.

Notes
-----

- Both 3V3 and 5V are routed to the side connectors (see pinout in :numref:`fig-pynq-rpi-ph-adapter-pinout`). The 3V3 rail is always routed to the connector; however, the 5V rail can be routed to or isolated from the connectors depending on a jumper resistor (see resistor `R1` on the schematics of the board).

.. _sec-pynq-rpi-ph-adapter-example:

Application example
-------------------

:numref:`fig-pynq-rpi-ph-adapter-buck-example` shows the ``pynq-rpi-ph-adapter`` board connecting the Pynq board with an experimental dc-dc converter. Compatible boards are attached to the ``pynq-rpi-ph-adapter`` board via ribbon cables. For this reason, the male headers were soldered on the bottom of the ``pynq-rpi-ph-adapter`` board.

.. figure:: media/general/pynq-plus-adapters-buck.svg
   :name: fig-pynq-rpi-ph-adapter-buck-example
   :scale: 13%
   :align: center
   :alt: Pynq and adapter boards.
   
   Pynq adapter combined with compatible boards.


.. warning::
   
   * TODO: add constraints file


Fabrication files
-----------------

To get the gerber files used to fabricate the ADC board, checkout commit ``48243a0069cdf400ffa442e71829328903b15db7``, and find the files under ``pynq-rpi-ph-adapter/gerber``.