# Django Project with DBBackup
This repository contains a Django project set up with DBBackup for managing database backups. DBBackup is a Django application that provides easy-to-use backup and restore functionalities for various database engines.

# Usage
## Installation:
### Clone the repository to your local machine:
```bash
git clone https://github.com/codewithpradip/django_db_backup.git
```
### Install required Python packages:
```bash
pip install -r requirements.txt
```
### Backup and Restore:
To manually initiate a backup:
``` bash
python manage.py dbbackup --clean
```
To restore a backup:
```bash
python manage.py dbrestore
```

# Contributing
Contributions to this project are welcome! Fork the repository, make changes, and submit a pull request.
