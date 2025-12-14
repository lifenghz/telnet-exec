import telnetlib
import time

HOST = "192.168.1.100"   # 目标IP
PORT = 23                # Telnet端口
USERNAME = "admin"
PASSWORD = "admin123"
COMMANDS = [
    "uname -a",
    "ls",
    "exit"
]

def telnet_run():
    tn = telnetlib.Telnet(HOST, PORT, timeout=10)

    tn.read_until(b"login: ")
    tn.write(USERNAME.encode("ascii") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("ascii") + b"\n")

    time.sleep(1)

    for cmd in COMMANDS:
        tn.write(cmd.encode("ascii") + b"\n")
        time.sleep(1)

    output = tn.read_all().decode("ascii", errors="ignore")
    tn.close()

    return output


if __name__ == "__main__":
    result = telnet_run()
    print(result)
