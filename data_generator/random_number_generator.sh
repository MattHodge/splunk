#!/bin/bash
splunk_tcp_host=localhost
splunk_tcp_port=1514

while :
do
    echo "Random number generator starting." > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 1
    echo "Random number successfully generated. fake_number=$RANDOM fake_number_2=$RANDOM" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 5
    echo "Random number generator finishing." > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    sleep 60
    echo "Looping..."
done
