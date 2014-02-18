.PHONY: point-test
point-test:
	python Point_test.py

.PHONY: point-util-test
point-util-test:
	python PointUtils_test.py

.PHONY: clean
clean:
		rm -rf *.pyc

.SILENT: clean
