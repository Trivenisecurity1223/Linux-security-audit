import platform
import socket
import getpass

print("===== LINUX SYSTEM SECURITY AUDIT =====")

print("Username:", getpass.getuser())
print("Hostname:", socket.gethostname())
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", platform.python_version())

print("\n===== NETWORK SECURITY AUDIT =====")

hostname = socket.gethostname()

try:
    ip_address = socket.gethostbyname(hostname)
    print("IP Address:", ip_address)
except Exception:
    print("Could not determine IP address")

print("\nDNS Test:")
try:
    print("google.com ->", socket.gethostbyname("google.com"))
except Exception:
    print("DNS lookup failed")

print("\n===== PORT CHECK =====")

ports = [21, 22, 23, 25, 53, 80, 443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex(("example.com", port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED/FILTERED")

    sock.close()

print("\n===== AUDIT COMPLETE =====")
