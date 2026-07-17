import subprocess
import platform


def list_devices():

    system = platform.system()

    devices = []


    if system == "Darwin":

        result = subprocess.run(
            [
                "diskutil",
                "list"
            ],
            capture_output=True,
            text=True
        )


        for line in result.stdout.splitlines():

            if "/dev/disk" in line:

                devices.append(
                    line.strip()
                )


    elif system == "Linux":

        result = subprocess.run(
            [
                "lsblk",
                "-o",
                "NAME,SIZE,TYPE,MOUNTPOINT"
            ],
            capture_output=True,
            text=True
        )


        devices = result.stdout.splitlines()


    else:

        devices.append(
            "Unsupported OS: " + system
        )


    return devices
