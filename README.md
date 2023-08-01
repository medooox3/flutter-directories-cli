# flutter-directories-cli
A simple python script to make it easy to execute flutter commands on multiple unrelated projects.

0. Install python (https://www.python.org/)
1. Download or clone this project.
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `flupy.py' to the root folder that contains your projects and excute the commands.

### How to use the script
```sh 
python3 flupy.py --help
python3 flupy.py clean <directory>  # cleans all flutter projects build directories in <directory.
python3 flupy.py get .  # runs `flutter pub get` in all flutter projects in under current directory

# if you are on windows use:
python flupy.py clean <dir>
```

