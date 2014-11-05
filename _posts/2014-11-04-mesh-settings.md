---
layout: post
title:  "Mesh Networking Settings for Series 2 XBees"
date:   2014-11-04 14:32:02
categories: xbee mesh
---

## Coordinator
- reset to factory settings
- load the latest firmware in "Coordinator API" mode
- set PANID to 2001
- set Destination High (DH) to 'FFFF'
- set Destination Low (DL) to '0'


## Router
- reset to factory settings
- load the latest firmware in "Router AT" mode
- set PANID to 2001
- ensure Destination High (DH) to '0'
- ensure Destination Low (DL) to '0'
- set NI to a unique string ("one", "two", "three") -> unique name for router
- set D0 to '0' (Disabled [0]) -> disable analog / digital port 0
- set D3 to '2' (ADC [2]) -> enable analog / digital port 3
- set IR to '3E8' -> 1000ms

### Kill-A-Watt
- follow above 'Router' settings
- after that, set D0 to '2' (ADC [2]) -> enable analog / digital port 0
