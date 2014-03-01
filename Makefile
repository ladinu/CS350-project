.PHONY: geometry-test
geometry-test:
	python test_Geometry.py

.PHONY: geometryUtils-test
geometryUtils-test:
	python test_GeometryUtils.py

.PHONY: point-util-test
point-util-test:
	python test_PointUtils.py

.PHONY: convexhull-test
convexhull-test:
	python test_ConvexHull.py

.PHONY: clean
clean:
		rm -rf *.pyc

.PHONY: h
h:
	python hullDrive.py

.PHONY: test
test: geometry-test geometryUtils-test point-util-test

.SILENT: clean
