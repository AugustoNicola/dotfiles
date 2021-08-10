#!/bin/bash

killall compton
compton -b --config "$HOME/.config/compton/compton.conf"
