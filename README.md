# MD5-Hash-Finder
Some method to fast find password hash

# Tests
For example we using [this](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) (133 MB) dict. Generating hash:passw took 1 min 2 sec on my PC (1 4344 392 entries; HDD, i3). From 133 Mb I earned 520 Mb /hash/ dir.  
Find hash took ~1 sec.  
Now file storage is almost devalued. For 5$ you can buy a cheap VPS with 1 Tb Raid5 HDD.

# Description
`generate.py` - to generate has:passw files  
`find.py` - find hash after making files
