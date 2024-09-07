.. _sec-digital-isolator-2t6r:

digital-isolator-2t6r
=====================

The ``digital-isolator-2t6r`` is a board containing two digital isolators, providing a total of 2 TX channels and 6 RX channels. The board supports digital isolators with SOIC-16W package. A diagram of the board is shown in :numref:`fig-digital-isolator-2t6r-diagram`, where:

* :math:`\text{V}_\text{DDA}`/:math:`\text{GNDA}` and  :math:`\text{V}_\text{DDB}`/:math:`\text{GNDB}` are the supply to each side.
* :math:`\text{RX1}_\text{A}, \dots, \text{RX6}_\text{A}` are the RX pins on side A.
* :math:`\text{TX1}_\text{A}` and :math:`\text{TX2}_\text{A}` are the TX pins on side A.
* :math:`\text{RX1}_\text{B}` and :math:`\text{RX2}_\text{B}` are the RX pins on side B.
* :math:`\text{TX1}_\text{B}, \dots, \text{TX6}_\text{B}` are the TX pins on side B.

.. figure:: img/digital-isolator-2t6r/diagram.svg
   :name: fig-digital-isolator-2t6r-diagram
   :scale: 150%
   :align: center
   :alt: Diagram of the board.
   
   Diagram of the board.

.. note::
   TX and RX pins are defined with respect to the board. Thus, TX pins on the board are outputs, and RX pins are inputs.

.. note::
   The board is denoted ``2t6r`` based on the number of TX and RX of side A. This is typically the side that would be connected to the target application, while side B is connected to the controller (thus providing the controller with 2 TX and 6 RX channels).

.. note::
   - TODO: make reference to Pynq header board.


Board and pinout
----------------

A fully populated board is shown in :numref:`fig-digital-isolator-2t6r-board`. The two TX signals and six RX signals are on the left (connector J2). The board's pinout is shown in :numref:`fig-digital-isolator-2t6r-pinout`.

.. figure:: img/digital-isolator-2t6r/board.svg
   :name: fig-digital-isolator-2t6r-board
   :scale: 15%
   :align: center
   :alt: Populated board.
   
   Populated board.

.. figure:: img/digital-isolator-2t6r/pinout.svg
   :name: fig-digital-isolator-2t6r-pinout
   :scale: 150%
   :align: center
   :alt: Pinout of the board.
   
   Pinout of the board.


Digital isolator compatibility
------------------------------

The board supports any isolator having the footprint shown in :numref:`fig-digital-isolator-2t6r-footprint`. Example of compatible isolators:

* Analog Devices' ADuM1401
* Texas Instruments' ISO6741
* Skyworks' Si8641

.. figure:: img/digital-isolator-2t6r/dig-iso-footprint.svg
   :name: fig-digital-isolator-2t6r-footprint
   :scale: 85%
   :align: center
   :alt: Footprint of isolator.
   
   Isolator's footprint.

.. note::
   The ENA and ENB pins are connected to their respective VDD pins on the board through a pull-up resistor. Should you instead need a low level on ENA/ENB to enable the chip, it is possible to simply do a solder bridge between EN and GND on the board.

.. note::
   The footprint of the isolator of this board is the same as in the :ref:`sec-digital-isolator-6t2r` board.

Isolator diagram
--------------------

The diagram of a single isolator is show in :numref:`fig-digital-isolator-2t6r-diagram-single`. TX lines contain a series resistor to help with ringing in case of driving capacitive lines. In most cases, a value of 10R-47R should be enough. The inputs contain a pull-down resistor to prevent floating signals at the input of the isolator. These might not be necessary depending on the part used. For example, ADuM1401 does not contain any pull down resistors (see `here <https://ez.analog.com/interface-isolation/f/q-a/86929/adum14x-does-adum14x-has-internal-pull-up-or-pull-down-resistor>`__ and `here <https://ez.analog.com/interface-isolation/f/q-a/84971/adum-unused-inputs>`__), while ISO6741 might (see `here <https://e2e.ti.com/support/isolation-group/isolation/f/isolation-forum/1216369/iso6740-input-pull-down-resistor-tolerance>`__).

.. figure:: img/digital-isolator-2t6r/diagram-single.svg
   :name: fig-digital-isolator-2t6r-diagram-single
   :scale: 130%
   :align: center
   :alt: Diagram of single isolator.
   
   Diagram of single isolator.


Usage as 6 TX and 2 RX
-----------------------

If this board has 2 TX and 6 RX channels on side A, and I need 6 TX and 2 RX channels instead, can't I simply use the board through side B instead? Why is there a :ref:`sec-digital-isolator-6t2r` board for this purpose?

Using the board from side B to get 6 TX and 2 RX channels is perfectly fine. Note, however, that the connections will be mirrored. 

In order to keep the same connections, but reversed TX and RX, board was :ref:`sec-digital-isolator-6t2r` designed. The main motivation for this is designing a single connector board for a controller that has a standard type of connector, and different applications would use different boards depending on the number of required TX and RX channels.

.. note::
   - TODO: mention relation to pynq adapter board.

Why this number of channels?
----------------------------

Originally, the board was intended to be used along the :ref:`sec-adc-board-six-channels`, to provide digital isolation. Thus, the number of TX and RX were chosen to be compatible with the ADC board.

Application example
-------------------

This board has been used as part of research projects on dc/dc converters, to isolate an FPGA from the converters. One example is shown in :numref:`fig-general-buck-boost-setup-dig-iso`. In this case, two boards were used as in  interface between the FPGA and the ADCs, thus providing isolated measurements. In this setup, the Si8641 chip was used, with signals of 16.7 MHz.

.. figure:: img/general/buck-boost-setup.jpeg
   :name: fig-general-buck-boost-setup-dig-iso
   :scale: 50%
   :align: center
   :alt: Buck/boost setup.
   
   2T6R isolator boards put to use.


Fabrication files
-----------------

To get the gerber files used to fabricate the isolator board, checkout commit ``b51d6b563e844d826048459c406fef7229853c5a``, and find the files under ``digital-isolator-2t6r/gerber``.
