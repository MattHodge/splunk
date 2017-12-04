import time
import socket
import uuid
from random import randint

SPLUNK_TCP_HOST = '127.0.0.1'
SPLUNK_TCP_PORT = 1514
MIN_RANDOM_INT = 5
MAX_RANDOM_INT = 10
SLEEP_TIME_BETWEEN_RUNS = 60
JOB_NAME = "test_xxx"
FAKE_PROCESSES = [
    "export_data_from_sql",
    "transform_data",
    "upload_data_to_ftp",
    "clean_up"
]


def get_uuid():
    return str(uuid.uuid4())


def get_unixtime():
    # If you use actual unix time, splunk will attempt to parse it and it will make the log ordering incorrect.
    return int(time.time() / 2)


def get_random_int():
    return randint(MIN_RANDOM_INT, MAX_RANDOM_INT)


def get_start_job_message(**kwargs):
    return "Starting Job job_name={job_name} job_state=start job_run_id={job_run_id} start_time={job_start_time}".format(
        job_name=kwargs['job_name'],
        job_run_id=kwargs['job_run_id'],
        job_start_time=kwargs['job_start_time']
    )


def get_end_job_message(**kwargs):
    return "Finishing Job job_name={job_name} job_state=end job_run_id={job_run_id} start_time={job_start_time}".format(
        job_name=kwargs['job_name'],
        job_run_id=kwargs['job_run_id'],
        job_start_time=kwargs['job_start_time']
    )


def get_start_process_message(process_name, **kwargs):
    return "Starting Process process_name={process_name} job_name={job_name} process_state=start job_run_id={job_run_id} start_time={job_start_time}".format(
        process_name=process_name,
        job_name=kwargs['job_name'],
        job_run_id=kwargs['job_run_id'],
        job_start_time=kwargs['job_start_time']
    )


def get_end_process_message(process_name, time_taken, **kwargs):
    return "Finished Process process_name={process_name} time_taken={time_taken} job_name={job_name} process_state=end job_run_id={job_run_id} start_time={job_start_time}".format(
        process_name=process_name,
        time_taken=time_taken,
        job_name=kwargs['job_name'],
        job_run_id=kwargs['job_run_id'],
        job_start_time=kwargs['job_start_time']
    )


def send_string_tcp(ip_address, tcp_port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, tcp_port))
    s.send(message)
    s.close()

while True:
    job_info = {
        "job_name": JOB_NAME,
        "job_run_id": get_uuid(),
        "job_start_time": get_unixtime()
    }

    job_start_msg = get_start_job_message(**job_info)
    print(job_start_msg)
    send_string_tcp(SPLUNK_TCP_HOST, SPLUNK_TCP_PORT, job_start_msg)

    for process in FAKE_PROCESSES:
        process_start = get_start_process_message(process, **job_info)
        print(process_start)
        send_string_tcp(SPLUNK_TCP_HOST, SPLUNK_TCP_PORT, process_start)

        sleep_time = get_random_int()
        time.sleep(sleep_time)

        process_end = get_end_process_message(process, sleep_time, **job_info)
        print(process_end)
        send_string_tcp(SPLUNK_TCP_HOST, SPLUNK_TCP_PORT, process_end)

    job_end_msg = get_end_job_message(**job_info)
    print(job_end_msg)
    send_string_tcp(SPLUNK_TCP_HOST, SPLUNK_TCP_PORT, job_end_msg)

    print("Sleeping for {0}.".format(
        SLEEP_TIME_BETWEEN_RUNS
    ))
    time.sleep(30)
