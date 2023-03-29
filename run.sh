# python app.py
# pip freeze > requirements.txt


# python app.py
# python3 -m venv ejemplo
# sleep 5
# source ejemplo/bin/activate
# pip install -r requirements.txt
# sleep 5


uvicorn index:app --reload --host 0.0.0.0 --port 3003 --workers 1