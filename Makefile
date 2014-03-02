.PHONY: geometry-line-test
geometry-line-test:
	python -m geometry.tests.Line_test

.PHONY: geometry-point-test
geometry-point-test:
	python -m geometry.tests.Point_test

.PHONY: geometry-utils-test
geometry-utils-test:
	python -m geometry.tests.utils_test

.PHONY: geometry-test
geometry-test: geometry-line-test geometry-point-test geometry-utils-test

.PHONY: test
test: geometry-test 


.PHONY: clean
clean:
		find . -name "*.pyc" -delete


.SILENT: clean
