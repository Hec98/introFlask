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
* Export 
```sh
export FLASK_APP=holamundo.py
```
* Export for development
```sh
export FLASK_ENV=development
```
* Flask run
```sh
flask run
```
***### HTTP methods via curl
```sh
curl -X GET http://127.0.0.1:5000/post/1
```
```sh
curl -X POST http://127.0.0.1:5000/post/1
```
```sh
curl -X PUT http://127.0.0.1:5000/post/1
```
