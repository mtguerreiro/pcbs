.. _sec-amplifier-board-six-channels:

amplifier-board-six-channels
============================

The ``amplifier-board-six-channels`` is a board containing six amplifiers, intended for gain and offset of analog signals. The board supports six analog channels. Its diagram is shown in :numref:`fig-amplifier-board-six-channels-diagram`, where:

* :math:`\text{V}_\text{CC}` and :math:`\text{V}_\text{DD}` are supply inputs. The amplifiers and reference generator can be supplied either with :math:`\text{V}_\text{CC}` (typically 3V3) or :math:`\text{V}_\text{DD}` (typically 5V). 
* :math:`\text{A}_{i1}, \dots, \text{A}_{i6}` are the analog inputs.
* :math:`\text{A}_{o1}, \dots, \text{A}_{o6}` are the analog outputs.

.. figure:: media/amplifier-board-six-channels/diagram.svg
   :name: fig-amplifier-board-six-channels-diagram
   :scale: 150%
   :align: center
   :alt: Diagram of the board.
   
   Diagram of the board.

Board and pinout
----------------

A partially populated board is shown in :numref:`fig-amplifier-board-six-channels-board`. The analog inputs are on the left (connector J1), while the analog outputs are on the right (connector J2).

.. figure:: media/amplifier-board-six-channels/board.svg
   :name: fig-amplifier-board-six-channels-board
   :scale: 10%
   :align: center
   :alt: Partially populated board.
   
   Partially populated board.

The board's pinout is shown in :numref:`fig-amplifier-board-six-channels-pinout`.

.. figure:: media/amplifier-board-six-channels/pinout.svg
   :name: fig-amplifier-board-six-channels-pinout
   :scale: 150%
   :align: center
   :alt: Pinout of the board.
   
   Pinout of the board.


Amplifier compatibility
-----------------------

The board supports any two-channel amplifier having the footprint shown in :numref:`fig-amplifier-board-six-channels-amplifier-footprint`. Example of compatible amplifiers:

* TI's LM358
* Microchip's MCP6002

.. figure:: media/amplifier-board-six-channels/amplifier-footprint.svg
   :name: fig-amplifier-board-six-channels-amplifier-footprint
   :scale: 85%
   :align: center
   :alt: Footprint of amplifier.
   
   Amplifiers's footprint.

Voltage reference compatibility
-------------------------------

The board supports voltage reference ICs having the footprint shown in :numref:`fig-amplifier-board-six-channels-reference-footprint`. Example of compatible references:

* Maxim's MAX6035

.. figure:: media/amplifier-board-six-channels/reference-footprint.svg
   :name: fig-amplifier-board-six-channels-reference-footprint
   :scale: 85%
   :align: center
   :alt: Footprint of reference.
   
   Voltage reference's footprint.


Single channel diagram
----------------------

The board can handle voltage or current signals at its inputs. For current signals, there is the possibility to place a burden resistor from the analog input to ground. For voltage signals, this resistor is not populated on the board. For clarity, the diagram of a single channel is discussed separately depending if the input is a voltage or a current signal. Each channel can also have its own reference, which can be used to offset the inpu signals. Next, the reference generator and the amplifier for each case is discussed.

Channel reference
^^^^^^^^^^^^^^^^^

Each channel has a reference generator, consisting of a voltage divider and an external reference that is common to all amplifiers on the board. The diagram of the reference generator of each channel is shown in :numref:`fig-amplifier-board-six-channels-diagram-single-reference`. The output reference :math:`V'_\text{r}` is

.. math::
   
   V'_\text{r} = \left( \frac{R_2}{R_1+R_2} \right) V_\text{r},

where :math:`V_\text{r}` is a reference signal common to all amplifiers in the board. Each amplifier can have its own reference. Note that :math:`V'_\text{r} \leq V_\text{r}`. For more information regarding :math:`V_\text{r}`, see :ref:`sec-amplifier-board-six-channels-reference`. 

.. figure:: media/amplifier-board-six-channels/diagram-single-reference.svg
   :name: fig-amplifier-board-six-channels-diagram-single-reference
   :scale: 130%
   :align: center
   :alt: Diagram of reference generator of a single channel.
   
   Diagram of reference generator of a single channel.
   
Input is a voltage signal
^^^^^^^^^^^^^^^^^^^^^^^^^

:numref:`fig-amplifier-board-six-channels-diagram-single-voltage` shows the diagram of a single channel, intended for use with voltage signals. By selecting :math:`R_1=R_3` and :math:`R_2=R_4`, the voltage at the output of the amplifier is

.. math::
   
   v'_\text{o} = V'_\text{r} + \left( \frac{R_2}{R_1} \right) v_\text{i}.

Thus, in this configuration, it is possible to add an offset of :math:`V'_\text{r}` and a gain of :math:`R_2/R_1` to the input signal. This is useful when conditioning a signal with a range between of -10V and 10V to a range of 0 to 3 V for an ADC, for example. 

A low-pass RC filter is placed at the output of the amplifier. Note that if this filter is used, the output signal won't be buffered anymore. Resistor :math:`R_\text{f}` can also be used as series resistor to help with ringing, in case the amplifier needs to drive a capacitive line.

.. figure:: media/amplifier-board-six-channels/diagram-single-voltage.svg
   :name: fig-amplifier-board-six-channels-diagram-single-voltage
   :scale: 130%
   :align: center
   :alt: Diagram of single channel for voltage signals.
   
   Single channel diagram for voltage inputs.

Another possibility is to use the channel as a buffer. This can be accomplished by simply removing :math:`R_2` and :math:`R_3`, and shorting :math:`R_1` and :math:`R_4`.

Input is a current signal
^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to use the board with current signals as well. Every channel contains a resistor between its input signal and ground that can be used as a burden resistor. The configuration of the channel for a current signal is shown in :numref:`fig-amplifier-board-six-channels-diagram-single-current`, where the input signal is a current source :math:`i_\text{i}` referred to the same ground as the amplifier board,  :math:`R_\text{B}` is the  burden resistor.

The burden resistor at the input is compensated by a burden resistor in series with :math:`R_3`. selecting :math:`R_1=R_3` and :math:`R_2=R_4`, the voltage at the output of the amplifier is

.. math::
   
   v'_\text{o} = V'_\text{r} + \left( \frac{R_2}{R_1+R_\text{B}} \right) R_\text{B}i_\text{i}.

.. figure:: media/amplifier-board-six-channels/diagram-single-current.svg
   :name: fig-amplifier-board-six-channels-diagram-single-current
   :scale: 130%
   :align: center
   :alt: Diagram of single channel for current signals.
   
   Single channel diagram for current inputs.
   
   
.. _sec-amplifier-board-six-channels-reference:

Voltage reference
-----------------

The board has a voltage reference source that is shared with all amplifiers. This reference is intended to be generated by a voltage reference IC. However, it is also possible to use the supply rails as reference by shorting the IC's supply and output pins.

Supplying the board
-------------------

As shown in :numref:`fig-amplifier-board-six-channels-diagram`, the amplifiers can be powered either with :math:`\text{V}_\text{CC}` (typically 3.3 V) or :math:`\text{V}_\text{DD}`  (typically 5 V). The voltage source is selected by populating the proper resistor on the PCB, as indicated in :numref:`fig-amplifier-board-six-channels-supply`. Depending on which resistor is populated and which is not, the amplifiers and voltage reference are powered as follows:

* R55 populated, R16 not placed: amplifiers and reference chip are powered with 5 V (:math:`\text{V}_\text{DD}`)
* R56 not placed, R15 populated: amplifiers and reference chip are powered with 3.3 V (:math:`\text{V}_\text{CC}`)

.. figure:: media/amplifier-board-six-channels/supply.png
   :name: fig-amplifier-board-six-channels-supply
   :scale: 50%
   :align: center
   :alt: Selecting the supply rail for the amplifier board.
   
   Selecting the supply rail for the amplifier board.

.. note::
   :math:`\text{V}_\text{DD}` and :math:`\text{V}_\text{CC}` do not have to necessarily be 5 V and 3.3 V. You can choose if you want to power the ADCs with :math:`\text{V}_\text{DD}` or :math:`\text{V}_\text{CC}`, as long as the chosen rail is within the voltage levels of the amplifier and voltage reference chips.

Why this number of channels?
----------------------------

Originally, the board was intended to be used in three-phase systems, to sample three voltage and three current signals. That's why the board was designed with six analog channels.


Application example
-------------------

The board shown in :numref:`fig-amplifier-board-six-channels-board` was used  to adapt the output signal of a tachometer to the input of a microcontroller's ADC. The supply rails were used as the reference, and the tachometer's -12~12V signal was converter to the ADC's 0~3V range.

Fabrication files
-----------------

To get the gerber files used to fabricate the isolator board, checkout commit ``9ccb289f878a5144997fc79c7e62c2e65202115a``, and find the files under ``amplifier-board-six-channels/gerber``
