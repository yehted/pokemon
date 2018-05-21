# Installation

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python setup.py develop

export FLASK_APP=run.py
flask run --host=0.0.0.0
```

Navigate to http://localhost:5000/api/

# Running tests
pip install nose mock
nosetests
