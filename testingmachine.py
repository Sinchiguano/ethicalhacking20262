# import subprocess

# host = "172.17.130.102"
# user = "jenn"
# port = "22"

# print("=" * 45)
# print("       ETHICAL HACKING SSH LAB")
# print("=" * 45)

# print(f"\n[+] Target: {host}")
# print(f"[+] User:   {user}")
# print(f"[+] Port:   {port}")

# print("\n[+] Testing network connectivity...")

# ping = subprocess.run(
#     ["ping", "-c", "1", host],
#     stdout=subprocess.DEVNULL
# )

# if ping.returncode == 0:
#     print("[+] Host is reachable.")

#     print("[+] Starting SSH connection...\n")

#     subprocess.run([
#         "ssh",
#         f"{user}@{host}",
#         "-p",
#         port
#     ])

# else:
#     print("[-] Host is not reachable.")

import subprocess
import getpass

host = "172.17.130.102"
user = "jenn"
port = "22"

password = getpass.getpass("Jenn's SSH password: ")

print(f"\n[+] Connecting to {user}@{host}...")

subprocess.run([
    "sshpass", "-p", password,
    "ssh",
    "-p", port,
    "-o", "StrictHostKeyChecking=accept-new",
    f"{user}@{host}"
])