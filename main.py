import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('HOSTNAME', username='USERNAME', password='PASSWORD', key_filename='*.ppk')

stdin, stdout, stderr = ssh.exec_command('ls -a')
print (stdout.readlines())
ssh.close()
