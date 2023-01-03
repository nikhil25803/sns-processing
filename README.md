## Setup

---

### Create and activate a virtual environment
```powershell
python -m venv env
```

```powershell
env\scripts\activate
```
### Install the dependenies
```
pip install -r requirements.txt
```

### Run the server on local system
First comment out the following section in `main.py`
```python
port = 8000
ngrok_tunnel = ngrok.connect(port)

print('Public URL:', ngrok_tunnel.public_url)

nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
```

Then run the following command in the terminal
```powershell
uvicorn main:app --reload
```

**OR**

### Run the server on `ngrok`
In this case, do not make any changes in the `main.py`. Or if made, just uncomment the `ngrok_tunnel` code.
Then run the following command in the powershell
```
python main.py
```

> Run the server on a URL provided, ends with `.ngrok.io`

**Note**
Running the server will create a `cars_database.db` in the root directory.
