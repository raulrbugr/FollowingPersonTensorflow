# FollowingPersonTensorflow

video: https://www.youtube.com/watch?v=jdCHuUhuZG0

This repository contains a little example that you can use to develop more interesting projets.

The interesting point with this project is the architecture that uses the rover.

This architecture consists on two main points

-Raspberry Pi2: send the video stream and use the actuators.
-Jetson TX1: receive the video stream via IP and process with tensorflow

How can comunicate Jetson and Rpi?
With a shared directory and writing and reading from a file
