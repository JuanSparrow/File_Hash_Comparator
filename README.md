# File_Hash_Comparator
Search for duplicate files by comparing their MD5 hashes
This script is intended for find duplicated files given a path. 
It uses MD5 hash algorithm for a nice balance between speed and realiability. 
It has been tested in Windows 11 Pro with network and local paths over a sample of 1600 files, about 7GB.
It took more than 3 hours to complete the entire process.
Execution must be done by console.
Results are shown in console.
It starts asking for a path, here, we should add a final slash (/) to the given path.
After the path it calculates number of items to work with and starts calculating their hashes and comparing with files in the given path.
