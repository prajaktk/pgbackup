pgbackup
========

CLI for backing up remote Postgresql database either locally or s3.

Preparing for Development
________________________

1. Ensure ``pip`` and ``pipenv`` is installed.
2. Clone repo
3. ``cd`` into the repo
4. Fetch dependencies ``make install``
5. Activate virtualenv ``pipenv shell`` 

Usage
-----

pass in a full db url, the storage driver and destination

S3 example

::

  $ pgbackup postgres://test@test.com:5432/db_one --driver s3 backups_bucket

Local example

::

  $ pgbackup postgres://test@test.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

  $ make

if virtualenv is not active, use:

::

  $ pipenv run make 



