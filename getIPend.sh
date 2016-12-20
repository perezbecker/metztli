#!/bin/bash
Value=$1

ifconfig wlan0 | grep "inet addr:" | cut -d: -f2 | awk '{print $1}' | awk -F\. '{print $Value}'
