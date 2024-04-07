#!/usr/bin/env python3

# Takes a ViewDat D40 output and converts it to a flat format file

# The format of the file is
# 0 Time in GPS seconds
# 1 External 1 Voltage
# 2 External 2 Voltage
# 3 USB  Voltage
# 4 Battery 1 Voltage
# 5 Battery 2 Voltage
# 6 Power source in use
# 7 Internal Temperature
# 8 Radio Temperature
# 9 Cell Temperature


external1=None
external2=None
battery1=None
battery2=None
USB=None
power_source=None
internalTemp=None
radioTemp=None
cellTemp=None
inRecord=False
week=None

#import fileinput
import pprint
import sys
import csv
import re
import binascii
from JCMBSoftPyLib import GPS_TIME


writer = csv.writer(sys.stdout)

line_num=0

pattern = r'\s*([\w\s\=\#\(\)]+)\s*:\s+([.\d+-]*)'

for line in sys.stdin:
    line=line.rstrip("\n")
#    print(binascii.hexlify(line.encode("utf-8")))

    if line.startswith("TYPE 40: Diagnostics"):
        inRecord=True
        output_fields=[None]*10
        continue

    if line == "":
        if inRecord:
            writer.writerow(output_fields)
        inRecord=False
        continue

# Dictionary to store parsed data
    data = {}

# Extract key-value pairs using regular expression
    values = re.match(pattern, line)

    if values != None:
#        print(line)
        key=values[1].strip()
#        pprint.pprint(key)
        value=float(values[2])
#        pprint.pprint(value)

        if key=="Seconds":
            output_fields[0]=GPS_TIME.Week_Seconds_To_Unix(week,value)
        elif key=="Week":
            week=value
        elif key=="External Voltage #1 (V)":
            output_fields[1]=value
        elif key=="External Voltage #2 (V)":
            output_fields[2]=value
        elif key=="Unknown type  20":
            output_fields[3]=value
        elif key=="Battery Voltage #1 (V)":
            output_fields[4]=value
        elif key=="Battery Voltage #2 (V)":
            output_fields[5]=value
        elif key=="Battery Voltage #2 (V)":
            output_fields[5]=value
        elif key=="Active Power Source (0 = port1)":
            output_fields[6]=int(value)
        elif key=="Temperature (degrees Celsius)":
            output_fields[7]=value
        elif key=="Radio Temperature":
            output_fields[8]=value
        elif key=="Modem Temperature":
            output_fields[9]=value



#       Time=GPS_TIME.Week_Seconds_To_Unix(int(fields[0]),float(fields[1]))
#       output_fields=[None]*12
#       output_fields[0]=Time

#       for field in range(n_fields):
#            print field
#            print "ID"
#            print fields[3+2*field]
#            print "VALUE"
#            print fields[4+2*field]
#            field_id=int(fields[3+2*field])
#            field_value=fields[4+2*field]
#            print field_id,field_value
#            output_fields[1+field]=field_value
#            print output_fields

