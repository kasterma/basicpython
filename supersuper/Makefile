VENV=. venv/bin/activate

venv:
	python -m venv venv
	${VENV} ; pip install -r requirements.txt

clean:
	rm -rf venv

format:
	${VENV} ; black *.py
