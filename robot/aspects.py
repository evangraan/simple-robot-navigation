import os.path

log_name: str = 'robot'
log_file: str = 'robot.log'


def load_file_as_list(file_name):
    entries = []
    if not os.path.isfile(file_name):
        return entries

    with open(file_name) as file:
        entries = [line.rstrip('\r\n') for line in file]

    return entries

def sanitize( value: str) -> str:
    if value:
        return value.rstrip('\r\n').lstrip().rstrip()

    return value