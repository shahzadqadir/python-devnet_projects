import paramiko

def cisco_ssh_commands(hostname, username, password, command):
    """Return command outputs"""
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = conn.exec_command(command)
    stdout = stdout.readlines()
    return stdout

output = cisco_ssh_commands("2.2.2.2", "ans", "cisco123", "show ip protocols")
for line in output:
    print(line.strip())
