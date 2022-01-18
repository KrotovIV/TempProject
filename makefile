run: main.py
	python3 main.py

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

lint:
	python3 -m flake8 ./

format:
	python3 -m black -l 79 ./
