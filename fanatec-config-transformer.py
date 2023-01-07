#!/usr/bin/python3

import xml.etree.ElementTree as ET
import os
import math

path = "<path goes here>"
dir_list = os.listdir(path)

for folder in dir_list:
    subfolders = os.listdir(path+"/"+folder)

    for subfolder_file in subfolders:
        if subfolder_file.endswith(".pws"):
            
            config_file = path+"/"+folder+"/"+subfolder_file
            tree = ET.parse(config_file)
            file_str = str(config_file)
            tree = ET.parse(file_str)
            root = tree.getroot()

            #the following section takes FF value and multiplies by 1.25 then rounds up to a whole value

            for ffb in root.findall("TuningMenu"):
                ffb_value = ffb.find("FF")
                brf_value = ffb.find("BRF")

                ffb_value_str = ffb_value.text
                new_ffb_value = int(ffb_value_str) * 1.25
                ffb_dd1_value_int = math.ceil(new_ffb_value)
                ffb_dd1_value = str(ffb_dd1_value_int)

                ffb_value.text = ffb_dd1_value
                brf_value.text = "95"

            #here we can change the wheel type which I assume gets rid of the error message when loading on DD1

            for wheel_type in root.findall("Device"):
                wheel_type.set("WheelType", "14")
                wheel_type.set("BaseType", "7")

            tree.write(config_file)


