.. _sec-cuk-iso-ps:

cuk-iso-ps
======================

``cuk-iso-ps`` is a PCB used to assemble an isolated Ćuk converter, meant to be used as an experimental platform for research and teaching in control in power electronics. Assembling  one converter requires two ``cuk-iso-ps`` PCBs and a high-frequency transformer.  

Introduction
------------

A diagram of an isolated Ćuk converter is shown in :numref:`fig-cuk-iso-ps-diagram`.

.. figure:: media/cuk-iso-ps/cuk-iso-diagram.svg
   :name: fig-cuk-iso-ps-diagram
   :scale: 110%
   :align: center
   :alt: Diagram of the isolated Ćuk.
   
   Diagram of the isolated Ćuk converter.

To ease routing of the PCB and have flexibility with respect to the transformer, the converter is implemented with two PCBs, one for each side (primary and secondary). However, because the topology is symmetric, the same PCB can be used for both sides. A simplified diagram of one side is shown in :numref:`fig-cuk-iso-ps-diagram-simplified`. On the left, :math:`V_\text{dc}` is the voltage of the dc link, which can be either the input or output voltage, depending if the board is used for the primary or secondary side. On the right, the board is connected to a high-frequency transformer. (The polarity of the transformer must match the polarity shown in :numref:`fig-cuk-iso-ps-diagram`.)

.. figure:: media/cuk-iso-ps/cuk-iso-diagram-simplified.svg
   :name: fig-cuk-iso-ps-diagram-simplified
   :scale: 110%
   :align: center
   :alt: Simplified diagram of ``cuk-iso-ps``.
   
   Simplified diagram of the ``cuk-iso-ps`` board.

The full diagram of the board, including measurements and switches, is shown in :numref:`fig-cuk-iso-ps-diagram-full`. On the far left, :math:`v_\text{io}` is the input/output voltage, depending if the board is for the primary or secondary side. On the far right, :math:`v_\text{T}` is the connection to the high-frequency transformer. 

The ``cuk-iso-ps`` board is controlled with switches :math:`S_\text{L}`, :math:`S_\text{io}`, and :math:`S_\text{c}`. Switch :math:`S_\text{L}` is a low-side switch that can be used to switch a load to the output. This can be used to emulate load steps. Switch :math:`S_\text{io}` is a high-side switch that can be used to disconnect the converter from its input/output. It was primarily meant to also emulate load steps, or, in case of faults, disconnecting the converter from its input or load. Switch :math:`S_\text{c}` is the main Ćuk switch.

.. figure:: media/cuk-iso-ps/cuk-iso-diagram-full.svg
   :name: fig-cuk-iso-ps-diagram-full
   :scale: 110%
   :align: center
   :alt: Full diagram of ``cuk-iso-ps``.
   
   Full diagram of the ``cuk-iso-ps`` board.

The converter is monitored with three voltage sensors and two current sensors. The input (or output) voltage of the board is monitored with sensors :math:`v_\text{io}` and :math:`v_\text{dc}`. While :math:`v_\text{dc}` measures the voltage across the dc-link capacitor, :math:`v_\text{io}` measures the voltage after the :math:`S_\text{io}` switch. When the switch is closed, both measurements are the same. The voltage of the coupling capacitor is monitored with sensor :math:`v_\text{cc}`. The input (or output) current of the converter is measured with sensor :math:`i_\text{io}`, and the inductor current is monitored with sensor :math:`i_\text{L}`.

Converter and board pinout
--------------------------

:numref:`fig-cuk-iso-ps-board` shows the assembled converter, using two ``cuk-iso-ps`` boards and a high-frequency transformer. The primary side is the input, while the secondary side is the output. The pinout of the signal connectors is shown in :numref:`fig-cuk-iso-ps-pinout-signal-j7`, :numref:`fig-cuk-iso-ps-pinout-signal-j8`, and :numref:`fig-cuk-iso-ps-pinout-signal-j9`. Connectors ``J7`` and ``J8`` have the measurement signals, while  ``J9`` contains the signals for the actuators. Connectors ``J7`` and ``J8`` provide the same set of measurements; the difference is that all measurements in connector ``J8`` are filtered. 

.. figure:: media/cuk-iso-ps/board.svg
   :name: fig-cuk-iso-ps-board
   :scale: 12%
   :align: center
   :alt: Cuk converter assembled from two ``cuk-iso-ps`` boards.
   
   Ćuk converter assembled from two ``cuk-iso-ps`` boards.

.. figure:: media/cuk-iso-ps/pinout-signal-j7.svg
   :name: fig-cuk-iso-ps-pinout-signal-j7
   :scale: 50%
   :align: center
   :alt: Pinout of connector J7.
   
   Pinout of connector J7.


.. figure:: media/cuk-iso-ps/pinout-signal-j8.svg
   :name: fig-cuk-iso-ps-pinout-signal-j8
   :scale: 50%
   :align: center
   :alt: Pinout of connector J8.
   
   Pinout of connector J8.


.. figure:: media/cuk-iso-ps/pinout-signal-j9.svg
   :name: fig-cuk-iso-ps-pinout-signal-j9
   :scale: 50%
   :align: center
   :alt: Pinout of connector J9.
   
   Pinout of connector J9.


Powering the board
------------------

The power stage and the electronics are powered separately. The range of the input voltage to the power stage depends mostly on the blocking characteristics of the power MOSFETs used.  However, the PCB has not been tested with more than 30 V at the input or output. It is also possible to use very low voltage levels at the input, for example, 2 V. Such low voltages can be used for debugging and calibration purposes.

The electronics is powered with 12 V. This voltage is directly used to power the gate drivers. Internally, a linear regulator uses the 12 V to create a 5 V rail. This rail is used to power the amplifiers and current sensors. Furthermore, the 5 V rail is connected to connectors ``J7``, ``J8``, and ``J9``, so that adapter boards can be powered from the converter. 


Models
------

Two models were built based on the assembled prototype: an LTSpice model and a PLECS model. The LTSpice model was used to design the converter and mainly see the voltage and current stress on the MOSFETs, and the effects of the snubber circuit. The PLECS model was built to support control design.

For the prototype, the following parts were used:

- Transformer: `NA5871-AL 800 W Planar Transformer <https://www.coilcraft.com/en-us/products/transformers/planar-transformers/planar/na5871/>`_, :math:`N`: 5/3
- Input inductor (:math:`L_1`): `Wurth Elektronik 74437429203101 <https://de.rs-online.com/web/p/smd-induktivitat/2585656?gb=b>`_, 100 uH
- Output inductor (:math:`L_2`): `Wurth Elektronik 74437429203151 <https://de.rs-online.com/web/p/smd-induktivitat/2585656?gb=b>`_, 150 uH
- Coupling capacitors (:math:`C_1`, :math:`C_2`): `EPCOS B32674D4475K000 <https://de.rs-online.com/web/p/folienkondensatoren/8829367?gb=b>`_, 4.7 uF (two were placed in parallel, resulting in 9.4 uF for  :math:`C_1` and :math:`C_2`)
- Input and output capacitors (:math:`C_\text{o}`): `Nichicon UCS2C331MHD <https://de.rs-online.com/web/p/aluminium-elektrolytkondensatoren/7152192?gb=b>`_ 330 uF
- Main switches: N-channel MOSFET `IPP200N25N3GXKSA1 <https://de.rs-online.com/web/p/mosfet/7545500?gb=s>`_, 250 V, 64 A, 20 mOhms
- Load switch: N-channel MOSFET `TK39A60W <https://de.rs-online.com/web/p/mosfet/8962366?gb=s>`_, 600 V, 39 A, 65 mOhms
- Snubber capacitor: `EPCOS B32621 <https://de.rs-online.com/web/p/folienkondensatoren/8961584?gb=b>`_, 10nF
- Snubber resistors: two 22 Ohms in parallel at the primary side, three 22 Ohms in parallel at the secondary-side

Drivers

- Gate drivers for main switches and load switch: `DGD0211C <https://www.diodes.com/assets/Datasheets/DGD0211C.pdf>`_
- Gate driver resistors for main switches: two 6.8 Ohms in parallel.
- Transistor for high-side drive: `PMBTA44,215 <https://de.rs-online.com/web/p/bipolare-transistoren/8015675?gb=b>`_

Sensors

- :math:`L_1` and :math:`L_2` inductor current sensors: `ACS730KLCTR-40AB-T <https://www.mouser.de/ProductDetail/Allegro-MicroSystems/ACS730KLCTR-40AB-T?qs=pUKx8fyJudBionxJgUyS8Q%3D%3D>`_, +- 40 A
- Input and output current sensors: `ACS712ELCTR-20A-T <https://www.mouser.de/ProductDetail/Allegro-MicroSystems/ACS712ELCTR-20A-T?qs=pUKx8fyJudBUdhIPMFjOBQ%3D%3D>`_, +- 20 A
- Amplifiers: `MCP6487 <https://www.microchip.com/en-us/product/mcp6487>`_

.. note::
   
   The ACS712 current sensors were acquired from Aliexpress. All remaining parts were acquired from Mouser or RS.


LTSpice model
^^^^^^^^^^^^^

- :download:`LTSpice model <media/cuk-iso-ps/cuk-iso-prototype.asc>`

The LTSpice model simulates the power stage of the converter. Most of the parasitics included in the LTSpice model were obtained as maximum values from the datasheet of each part. However, the equivalent series resistance (ESR) of the input and output inductors and of the output capacitor were obtained experimentally.

The values obtained were:

- :math:`R_\text{L,1}`: 42.43 mOhms
- :math:`R_\text{L,2}`: 10.26 mOhms
- :math:`R_\text{C,o}`: 131 mOhms

The ESR of the inductors were obtained by measuring the average voltage across the inductors with a multimeter. Then, the input/output currents were measured, and this was used to determine the ESR. The ESR of the output capacitor was estimated based on its measured voltage ripple and estimated current ripple.

The simulation has some reasonable agreement with the hardware. :numref:`fig-cuk-iso-prototype-model-val-ltspice-vds` and :numref:`fig-cuk-iso-prototype-model-val-vds` show the drain-source voltages of the MOSFETs, obtained in LTSpice and experimentally. The shape of the waveforms match quite well, but the drain-source voltage of the switch on the secondary has a higher peak value.

.. figure:: media/cuk-iso-ps/cuk-iso-prototype-model-val-ltspice-vds.png
   :name: fig-cuk-iso-prototype-model-val-ltspice-vds
   :scale: 20%
   :align: center
   :alt: Vds LTSpice cuk iso
   
   Simulated drain-source voltage of MOSFETs. Yellow: Primary-side MOSFET. Blue: Secondary-side MOSFET.

.. figure:: media/cuk-iso-ps/cuk-iso-prototype-model-val-vds.png
   :name: fig-cuk-iso-prototype-model-val-vds
   :scale: 20%
   :align: center
   :alt: Vds experimental cuk iso
   
   Experimental drain-source voltage of MOSFETs. Yellow (CH1): Primary-side MOSFET. Blue (CH2): Secondary-side MOSFET.

The table below shows steady-state input/output measurements obtained with multimeters. These measurements were obtained with 50% duty-cycle, 200 ns of dead time and switching frequency of 100 kHz. Input and output voltages were measured at the converter's terminals. 

The output stage measurements show good agreement between simulation and  experiments. However, we see higher current (and power) on the experiments, which is probably because the prototype has more losses. 

================== =========== ============ =========
Quantity           Simulation  Experimental Error (%)
================== =========== ============ =========
Input voltage        16.88 V     16.88 V          -    
Input current        2.473       2.575 A      3.96  
Input power         41.74 W     43.47 W     4.14   
Output voltage      28.66 V     28.42 V      0.83   
Output current     1.30 A       1.30 A       0    
Output power       37.32 W      36.95 W     0.99   
Efficiency          89.4%       84.6%         -  
================== =========== ============ =========

PLECS model
^^^^^^^^^^^

- :download:`PLECS model <media/cuk-iso-ps/cuk-iso-prototype-control-model.plecs>`

The PLECS models above can be used for closed-loop simulation. The model includes ADCs and PWMs. In the simulation, as in the hardware, the PWM is generated based on a triangle carrier, and the measurements are triggered when the carrier reaches its peak value. In this way, the current of the inductors are sampled as its average value. Moreover, using this scheme can reduce switching noise in the measurements. 

The model is a reasonable representation of the prototype. :numref:`fig-cuk-iso-ps-prototype-sensors-meas-sim` and :numref:`fig-cuk-iso-ps-prototype-sensors-meas-exp` show a comparison between the measurements obtained from the simulation and from the prototype. The results were obtained with an input voltage of 20 V, a permanent load of 22 Ohms, a switched load of 20 Ohms, and a duty-cycle of 0.47. Both figures show the measurements as seen by the controller, assuming the controller obtains signals from an ADC, and then these readings are converted back to the actual measurements. 

:numref:`fig-cuk-iso-ps-prototype-sensors-meas-sim` and :numref:`fig-cuk-iso-ps-prototype-sensors-meas-exp` show the system's response when there is a load step (a 20 Ohm resistor is connected to the permanent 22 Ohm resistor). As the figures show, the shape of the waveforms are well represented by the simulation (although the exact numerical values don't match perfectly).

.. figure:: media/cuk-iso-ps/cuk-iso-prototype-sensors-meas-sim.png
   :name: fig-cuk-iso-ps-prototype-sensors-meas-sim
   :scale: 28%
   :align: center
   :alt: Open-loop simulated measurements
   
   Simulation results.

.. figure:: media/cuk-iso-ps/cuk-iso-prototype-sensors-meas-exp.png
   :name: fig-cuk-iso-ps-prototype-sensors-meas-exp
   :scale: 28%
   :align: center
   :alt: Open-loop experimental measurements
   
   Experimental results.

.. note::
   
   In the PLECS model, noise is added to the current measurements. This is because the current measurements are quite noisy in the hardware (as opposed to the voltage measurements, which are quite clean). 
   
   The standard deviation that was used to model the noise was obtained from hardware experiments.

.. note::
   
   The parameters of the PLECS model were adjusted to better match the transient observed in the measurements. Thus, the parameters in the LTSpice model and PLECS model may not necessarily match.


Known issues
------------

* :math:`S_\text{io}` switch: in the current version of the prototype, a P-channel MOSFET was used to realize this high-side switch. In practice, this didn't work quite well because the on resistance of the P-channel used was too large. Moreover, to fully drive the MOSFET, a large-ish output voltage was required, which made things more difficult when debugging the converter with low voltages. Thus, in the assembled prototype, this switch as shorted and not used. For future versions, it would be better to use a relay or an N-channel MOSFET with proper driving.
  
* Snubber: the snubber used in this version of the prototype is very large. It improves ringing on the MOSFETs quite well but also is very lossy, and the resistors get very hot. For this reason, with the current snubber circuit, it is only possible to continuously run the converter for a couple of seconds. Despite this limitation, the converter has been used with up to 200 W of load.

* Filtered measurements: initially, there was a concern regarding switching noise affecting the measurements. For this reason, all measurements have a filtered counterpart, and an additional connector was dedicated for these measurements. The idea was to compare the raw and filtered measurements. However, overall, no significant noise was observed in the raw measurements. Although the raw current measurements is significantly noisier, it was within the levels expected from the current sensors. In a future version, the dedicated connector with filtered measurements can be removed. The raw or filtered signal can be routed to a single measurements connector, and the measurement that goes to the connector can be selected with a jumper.


Additional notes
----------------

* A dead-time of 200 ns seemed to improve :math:`V_\text{DS}` on the primary. With 100 ns, ringing on :math:`V_\text{DS}` got worse, with 200 ns it got much better. Increasing beyond 200 ns did not improve much (however, it seems like the losses were lower as the dead time increased)

Fabrication files
-----------------

To get the gerber files used to fabricate the converter, checkout commit ``7783b334fa4f7df7ff749daa6876e2eef62db06c``, and find the files under ``cuk-iso-ps/gerber``.
