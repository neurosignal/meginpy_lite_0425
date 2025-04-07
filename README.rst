.. -* mode: rst -*-

================
meginpy_lite_0425
================

A module to convert string type digitization into extra type headshape points.

It is a temporary workaround until the string gets support by mne-tools. 
It utilizes MEGIN's *show_fiff* utility to correctly read all digitization 
types and then feed back to the file. Optionally the file with the denser digitization 
points can be written. If the *show_fiff* is not available on the same machine, 
provide hostname, username, and password for a computer where *show_fiff* is installed.
The module seamlessly connect to the host machine and perform the task, 
if the data is readable to the host machine. 

How to use
===========

There are two ways to use the module: i) by installing, ii) adding it to your script


 