---
layout: post
title: "Week 11: Naming Protocol"
date: 2014-11-10 18:12
categories: notes
---

We need to encode the *type of sensor* and the *location*.

## The Coordinator
The Coordinator has a special NI `MASTER`


## Type of Sensor
- ls - light switch
- pl - plug level sensor
- es - environmental sensor


## Location
- building (four characters)
- floor    (two characters)
  + `-1` basement
  + `01` floor 1
  + `77` 77th floor
- room (five characters)
  + `boots` - bootstrap
  + `vc`    - vc
  + `NWRM1` - Northwest room 1
  + `proto` - prototyping


## Examples
- `eselab-1boots` - Environmental Sensor, eLab, basement, bootstrap
- `eselab-1vc`    - Environmental Sensor, eLab, basement, vc
- `eselab-1proto` - Environmental Sensor, eLab, basement, proto
- `plelab-1boots` - Plug Level Sensor,    eLab, basement, boostrap
- `plelab-1vc`    - Plug Level Sensor,    eLab, basement, vc
