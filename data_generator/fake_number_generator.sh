#!/bin/bash
splunk_tcp_host=localhost
splunk_tcp_port=1514

while :
do
    echo "Fake number generator starting." > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 1
    echo "Fake number successfully generated. fake_number=$RANDOM" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 1
    echo "Fake number generator finishing." > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 5
    echo "Looping..."
done
