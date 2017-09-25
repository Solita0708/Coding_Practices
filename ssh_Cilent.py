mport paramiko
import re
import time
from time import gmtime, strftime

count = 0
loops = 1
ssh_cmd = 'tail -n1 /PATH01/patapon_'+strftime("%Y%m%d", gmtime())+' | grep no | wc -l'

while loops == 1 :
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        client.connect(hostname = 'ip_address', key_filename='/PATH02/.ssh/id_rsa')
        stdin, stdout, stderr = client.exec_command(ssh_cmd)
        x = re.match(r"(?P<Digi1>\d)", stdout.read())
        if str(x.group(1)) == "1":
            count += 1
            if count == 3:
                stdin, stdout, stderr = client.exec_command('curl ip_address'/wakeup.php?player=mark')
                count = 0
    finally:
        client.close()
    time.sleep(5)
