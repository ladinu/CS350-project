.PHONY: point-test
point-test:
	python Point_test.py

.PHONY: clean
clean:
		rm -rf *.pyc

.SILENT: clean
