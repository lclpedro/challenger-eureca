## Tutorial Excution Code

1. Clone the project with git.
```
$ git clone https://github.com/lclpedro/project-eureca.git
```

2. Entry in project and create virtual env for python.
```
$ cd project-eureca
$ virtualenv -p python3 env
$ source env/bin/activate
```

Case you not installed virtualenv
```
$ sudo pip install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```

After pre-requisits hour of install requirements of app.

```
$ pip install -r requirements.txt
```

Execution python file and await return response.

```
$ python main.py

```

Preview response

```
      tconst originalTitle averageRating numVotes
0  tt0138534          John           8.1       25
3  tt0942798          John           7.9      173
2  tt0441769          John           7.5       13
5  tt1095864          John           7.0        5
4  tt1095185          John           6.6        9
1  tt0296026          John           6.1        9
```


