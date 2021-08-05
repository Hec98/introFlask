# Intro Flask
## Intoduction
* Add venv
```sh
python3 -m venv venv
```
* Activate venv
```sh
. venv/bin/activate
```
* Install Flask
```sh
pip3 install Flask
```
* Add neovim if used
```sh
pip3 install neovim
```
* Export for development
```sh
export FLASK_APP=helloWorld.py && export FLASK_ENV=development
```
* Flask run
```sh
flask run
```
### HTTP methods via curl
* GET
```sh
curl -X GET http://127.0.0.1:5000/post/1
```
```sh
curl -X GET http://127.0.0.1:5000/json
```
* POST
```sh
curl -X POST http://127.0.0.1:5000/post/1
```
* PUT
```sh
curl -X PUT http://127.0.0.1:5000/post/1
```
* POST sending data
```sh
curl -d "key1=data1&key2=data2" -X POST http://127.0.0.1:5000/form
```
* Redirect
```sh
curl -X GET http://127.0.0.1:5000/redirect
```
[![logoN1-w.png](https://i.postimg.cc/bvwkKP8Y/logoN1-w.png)](https://github.com/Hec98)
