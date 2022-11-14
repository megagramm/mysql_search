import sys


help_string = """That app make search through all database tables
Author: Andrey Grey megagramm@gmail.com 2022

-h - show this screen
-t - Required. type of search. mysql db or dumpfile [mysq|mysqldump]
-q - Required. search string
-tt - mysql table type. that type to make searching more fast.
        Params like 'char', 'varchar', 'enum', 'text' etc
-strong [default False] Boolean parameter [True,False] to make strong search like 'param=value'
        if -strong is True. Or search like 'param like `%value%`', when -strong parameter if False
-outfile - file to write output.
If selected mysql type:
    -host - default host is 'localhost'
    -port - default port is '3306'
    -db - database
    -u - username
    -p - password

    Example: "mysql_search -t mysql -q '555-1234' -tt 'varchar' -db test_db"

If selected mysqldump type:
    Filepath to mysqldump-file is a last parameter, after type parameter.
    -file - mysqldump-file path
    Example: "mysql_search -t mysqldump -q '555-1234' -tt 'varchar' -file /home/user/mydumpfile.sql"
"""

if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit('Для вызова справки укажите параметр -h')
    else:
        if sys.argv[1] == '-h':
            exit(help_string)
        else:
            if sys.argv[1] != '-t':
                exit("hh")
            else:
                if sys.argv[2] not in ['mysql', 'mysqldump']:
                    exit("ss")


        for param in sys.argv:
            print(param)
            ...


