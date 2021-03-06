# Overview

This tool will save configs locally and optionally upload them to a TFTP server. Put your device IPs or hostnames in devices.txt.

# Setup

```
git clone https://github.com/bbartik/cisco-backup.git
cd cisco-backup
virtualenv .venv
pip install -r requirements
```

# Usage 1 - Save locally

```
$ python backup_ios.py 
Enter username: jbeam
Enter password: 
Backing up config for 172.28.87.44
Backing up config for 172.28.87.45
All done, bye.
```

# Usage 2 - Upload via TFTP

```
$ python backup_ios.py --upload 172.28.87.10
Enter username: jbeam
Enter password: 
Error creating './configs' directory, it may already exist.
Backing up config for 172.28.87.44.
Config uploaded to 172.28.87.10.
Backing up config for 172.28.87.45.
Config uploaded to 172.28.87.10.
All done, bye.
```

# Usage 3 - Use SSH keyfile

```
$ python backup_ios.py --upload 172.28.87.10 --identity bbartik
Enter identity file (Ex: '~/.ssh/id_rsa'): ~/.ssh/bbartik
Error creating './configs' directory, it may already exist.
Backing up config for 172.28.87.45.
Authentication failed for 172.28.87.45...skipping.
Backing up config for 172.28.87.44.
Config uploaded to 172.28.87.10.
All done, bye.
```
