#!/bin/bash

HOST_IP=10.251.83.165
HOST_PORT=8082
WIDTH=640
HEIGHT=480
QUEUE_BYTES=$((2**24)) # 16mb queues between threads

gst-launch-1.0 \
pulsesrc !\
	audioconvert !\
	lamemp3enc target=bitrate bitrate=64 cbr=true !\
	queue max-size-bytes=$QUEUE_BYTES !\
tcpserversink port=$HOST_PORT host=$HOST_IP recover-policy=keyframe sync-method=latest-keyframe
