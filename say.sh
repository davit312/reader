#!/bin/bash
pico2wave -w=/tmp/ts.wav "$1"
aplay /tmp/ts.wav
rm /tmp/ts.wav
