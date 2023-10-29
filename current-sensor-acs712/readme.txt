Current sensor
--------------

The board was designed with ACS712 in mind. However, it will work with the following ACS sensors:
- ACS711
- ACS712
- ACS725
- ACS730
- ACS70331
- ACS71240

The only difference is pin 6, which can be a filter, NC, or a fault signal. Beforing using one of these sensors, consult the datasheet for the proper configuration on the board.