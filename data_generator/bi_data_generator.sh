#!/bin/bash
splunk_tcp_host=localhost
splunk_tcp_port=1514
MAXWAIT=30

while :
do
    uuid=$(uuidgen)
    start_time=$(date +%s)
    echo "Starting Job job_name=etl_task_1 job_state=start job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    echo "Starting Process job_name=etl_task_1 process_name=read_from_sql process_state=start job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    amount_to_sleep=$((RANDOM % MAXWAIT))
    sleep $amount_to_sleep
    echo "Finishing Process job_name=etl_task_1 process_name=read_from_sql process_state=end time_taken=$amount_to_sleep job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    echo "Starting Process job_name=etl_task_1 process_name=parse_data process_state=start job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    amount_to_sleep=$((RANDOM % MAXWAIT))
    sleep $amount_to_sleep
    echo "Finishing Process job_name=etl_task_1 process_name=parse_data process_state=end time_taken=$amount_to_sleep job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    echo "Starting Process job_name=etl_task_1 process_name=upload_data process_state=start job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    amount_to_sleep=$((RANDOM % MAXWAIT))
    sleep $amount_to_sleep
    echo "Finishing Process job_name=etl_task_1 process_name=upload_data process_state=end time_taken=$amount_to_sleep job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    echo "Finishing Job job_name=etl_task_1 job_state=end job_run_id=$uuid start_time=$start_time" > "/dev/tcp/$splunk_tcp_host/$splunk_tcp_port"
    echo "Starting Loop Again..."
    sleep 120
done
