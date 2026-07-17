import subprocess


def list_devices():

    result=subprocess.run(
        [
            "diskutil",
            "list"
        ],
        capture_output=True,
        text=True
    )

    devices=[]

    for line in result.stdout.splitlines():

        if "/dev/disk" in line:

            devices.append(
                line.strip()
            )

    return devices
