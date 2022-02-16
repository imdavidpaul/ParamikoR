import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('HOSTNAME', username='USERNAME', password='PASSWORD', key_filename= '*.ppk')

sftp = ssh.open_sftp()
sftp.put("FILENAME", "REMOTEFILENAME")
sftp.close()

