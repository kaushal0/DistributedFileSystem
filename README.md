DFS: Basic Distributed file system

DFS is a distributed file system written in Python with Components as follows:

DirectoryService - (nameserver) - Records mappings between directories and (which hold mappings betweens directories names and File Services)
File Services -(fileserver) - Performs operation of distributing the files.
Locking Service - (lockserver) -(which hold locks about files!)


Working Features:
Uses a REST api
Simple Configuration files - to hold the server configurations (JSON files)
The Directory Service automatically discovers File servers when they contact the server at startup.
Automatic locking of files when they're open in write mode (not yet working)

resistant to failure (you can kill -9 a {file,lock,name}server, it will restart in the same state as when it was killed)

In this assignment the Attempt was to use an upload/download model for the distributed system and to implement nameserver, fileserver, locking and caching.
Basic name server was implemented for which test files client and names were created to run the corresponding servers. This tested if on connection, the client name was recorded in the Directory Server.
File Server has been implemented to handle read operation from the client.


Design
I'll make a report to explain the design and my choices as soon as possible.


How to use?
Run "python names.py 8000" from dfs/test/names. This starts the name server on 8000.
Run "python FileServer.py 8002" from dfs/test/fs. This starts the file server on 8002 and notifies the Directory Server which confirms its connection.
Run "python Client.py 8003" from dfs/test/client. Starts and 8003 and attempts to open a file by connecting to file server.
