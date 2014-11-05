---
layout: post
title:  "Debugging XBee"
date:   2014-11-03 14:32:02
categories: xbee
---

## AT Commands
The following information is adapted from this [helpful blog post.](http://https417.blogspot.com/2014/02/xbee-series-2-are-you-listening-can-you.html)

- ATCH
  + The current channel the XBee is on. This is set after joining a network.
    The router and coordinator should be on the same network. This field is
    not writeable.
- ATID
  + What PAN ID are you at. All of your XBees need to have the same PAN ID.
- ATNR
  + What's your network joining status.
- ATCN
  + Leave command mode.
- ATDL
  + Destination Low Address (of the router you want to talk to). Set this to
    the other radio's ATSL. **very important**.
- ATDH
  + Destination High Address.
- ATSL
  + The router's Low Address.
- ATSH
  + The XBee's High Address
