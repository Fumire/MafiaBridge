VERSION = 37

all: __pycache__/main.cpython-$(VERSION).pyc
	python3 main.py

__pycache__/main.cpython-$(VERSION).pyc: main.py __pycache__/variable.cpython-$(VERSION).pyc __pycache__/engine.cpython-$(VERSION).pyc
	python3 -c "import py_compile; py_compile.compile(r'$<')"

__pycache__/engine.cpython-$(VERSION).pyc: engine.py
	python3 -c "import py_compile; py_compile.compile(r'$<')"

__pycache__/variable.cpython-$(VERSION).pyc: variable.py
	python3 -c "import py_compile; py_compile.compile(r'$<')"

clean:
	rm -rfv __pycache__
	rm -fv *.pyc
