Here are the instructions for downloading the flights database.  This assumes that you have alread installed MySQL, including MySQL workbench.

1. Download flights.zip from this URL: https://www.dropbox.com/s/wyn3jemzlagwq8b/flights.zip?dl=0

2. Copy the zip file to a folder on your local machine.  On my PC, I created a folder called c:dataflights.

3. Unzip the six files in the folder.  There will be a single .SQL script file and five .CSV files that will be loaded into 5 tables in your flights database.

4. Launch MySQL workbench.

5. Create a new MySQL schema (database) called flights.

6. Make the flights database yor default schema.

7. Open the script loadflights.sql.  If you copied the files to a different folder on your PC, or you copied to a Mac folder, you'll need to modify each of the five LOAD commands in the script to point to the correct file location.    Also note: if you get an error indicating you can't execute the statement as it is running the 'secure-file-priv' option (a MySQL configuration setting) then change your script LOAD commands from LOAD DATA INFILE to LOAD DATA LOCAL INFILE.

** UPDATE **:  If you are using MySQL 8.0.11 the command LOAD DATA LOCAL INFILE does not run (it will work with MySQL 5.6 or 5.7).  If this is the case, please note that MySQL has a configuration turned on by default called "secure-file-priv".  This configuration restricts the directories from which you can load data to only the one specified in the 'options file', which is typically located on "C:\ProgramData\MySQL\MySQL Server 8.0\my.ini" (in Windows 10).    If you open that file, you will notice only a specified directory is allowed for reading (typically, "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads"), so you can place the filght csv files there and change the SQL script to read from that directory.   Another option is to change the 'my.ini' file to allow reading data from another directory, for example:

# Secure File Priv.
secure-file-priv="C:\data\flights"

once the 'my.ini' file has been saved, you would have to restart MySQL server (either by restarting the computer or by restarting the service).  At that point the 'loadflights.sql' script should run fine.


8. Run the loadflights.sql script.  Your script should return a table with row counts for each of the tables loaded

Here is a 3 minute video that shows how to perform the MySQL Workbench steps outlined above:
-- SHOW VARIABLES LIKE "secure_file_priv";
				C:\ProgramData\MySQL\MySQL Server 8.0\Uploads

Upload CSV files must be stored in above directory

https://youtu.be/rnFxtaKGP4U

For those of you that still had an issue with permissions in MySQL (related to secure-file-priv settings), you can make use of the sql scripts attached to the link below.   They contain the sql script to create the tables as well as insert the  data.   Please note you need to create the flights schema first, and then run the scripts on that schema.

There are 5 scripts in total you must run (one for each table). Please note some scripts  are quite large, so it may take MySQL Workbench 10+  minutes to open them.  That is fine, you can wait until the script is open on Workbench and  then run it.

https://www.dropbox.com/s/qhgk65zv8syrq6d/flights_withdata.zip?dl=0

Aggregation in SQL

Please go through this material if you are new or at all confused about how to use SQL aggregation!   This additional reading and the 6 minute video below are from Software Carpentry:

Examples:  http://v4.software-carpentry.org/databases/aggregation.html  Please note that these examples use sqlite instead of MySQL.

https://youtu.be/ZjuL-pfkUOA

Attached Files
File HOL SQL SELECT basics.pdf (288.516 KB)
File HOL_SQLSelectBasics.sql (2.299 KB)
These ungraded hands-on labs will help you build your skills working with selecting, filtering and sorting information in a SQL SELECT statement.  Solutions to all problems are immediately available, but you’ll learn the material more durably if you attempt each problem before consulting its solution.

All of the queries use tables in the flights database.  You may find the data descriptions here helpful:

http://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf


Attached Files
File HOL SQL Aggregration.pdf (232.194 KB)
File HOL_SQLAggregations.sql (1.64 KB)
These ungraded hands-on labs will help you build your skills working with aggregating information in a SQL SELECT statement.  Solutions to all problems are immediately available, but you’ll learn the material more durably if you attempt each problem before consulting its solution.

All of the queries use tables in the flights database.  You may find the data descriptions here helpful:

http://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf