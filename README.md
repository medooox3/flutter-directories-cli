# flutter-directories-cli
A simple python script to make it easy to execute flutter commands on multiple unrelated projects.


### How to use
```sh 
python3 flupy.py --help
python3 flupy.py clean <directory>  # cleans all flutter projects build directories in <directory.
python3 flupy.py get .  # runs flutter pub get in all flutter projects in under current directory

# if you are on windows use:
python flupy.py clean <dir>
```

