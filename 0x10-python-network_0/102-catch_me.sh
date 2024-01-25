#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton servers
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
