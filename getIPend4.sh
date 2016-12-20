#!/bin/bash

/sbin/ifconfig wlan0 | grep "inet addr:" | cut -d: -f2 | awk '{print $1}' | awk -F\. '{print $4}'
