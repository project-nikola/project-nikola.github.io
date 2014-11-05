---
layout: post
title:  "Debugging Xbee"
date:   2014-11-03 14:32:02
categories: xbee
---

## AT Commands
The following information is adapted from this [helpful blog post.](http://https417.blogspot.com/2014/02/xbee-series-2-are-you-listening-can-you.html)
- ATCH
  + What channel you are on. Not writeable. This gets set after you've joined
    a network. Hopefully your ROuter and Coordinator are on the same one.
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
  + The router you're pluggined into over the wire's Low Address.
- ATSH
  + The XBee you're plugged into's High Address.
