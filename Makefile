.PHONY: geometry-test
geometry-test:
	python Geometry_test.py

.PHONY: point-printer-test
point-printer-test:
	python PointPrinter_test.py

.PHONY: point-util-test
point-util-test:
	python PointUtils_test.py

.PHONY: clean
clean:
		rm -rf *.pyc

.SILENT: clean
