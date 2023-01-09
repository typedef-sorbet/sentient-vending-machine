# Output stuff

OUT_LO = 1
OUT_HI = 0

PIN_CREDIT = 8

# 8 long, right side
# Pins for the wiring harnesses that *would* plug into the selector
# switches, but which this Pi hijacks to be able to vend on-demand
PIN_SWITCH_OUT = [
    10,
    12, 
    16,
    18,
    22,
    24,
    26,
    31
]

# Input stuff

# 8 long, left side
# Pins for the switches on the outside of the machine
PIN_SWITCH_IN = [
    11,
    13,
    15,
    19,
    21,
    23,
    29,
    31
]
