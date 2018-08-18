all: __pycache__/main.cpython-37.pyc
	python3 main.py

__pycache__/main.cpython-37.pyc: main.py __pycache__/variable.cpython-37.pyc
	python3 -c "import py_compile; py_compile.compile(r'main.py')"

__pycache__/variable.cpython-37.pyc: variable.py
	python3 -c "import py_compile; py_compile.compile(r'variable.py')"

clean:
	rm -rf __pycache__
	rm -f *.pyc
