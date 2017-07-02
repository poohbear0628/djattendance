### How to install Google Or-tools

Download latest dependencies here: https://github.com/google/or-tools/releases/latest

Run the following command:

```
cd ortools
mypython=$(which python)
sudo $mypython ortools/setup.py install

```

If you don't have root privileges:

```
python setup.py install --user
```
