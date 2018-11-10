PY_EXE_DIR:=$(PWD)/dist/zyWAF_AT_api
RPM_BUILD_ROOT:=~/rpmbuild

info:
	py_exe_dir=$(PY_EXE_DIR)
	rpm_build_root=$(RPM_BUILD_ROOT)


py_exe:
	pyinstaller zyWAF_AT_api.py
	mkdir dist/zyWAF_AT_api/data


rpm_package:
	rpmdev-setuptree
	cp rpm_package.spec $(RPM_BUILD_ROOT)/SPECS/rpm_package.spec
	cp -sR $(PY_EXE_DIR)/* $(RPM_BUILD_ROOT)/BUILD/
	rpmbuild -bb $(RPM_BUILD_ROOT)/SPECS/rpm_package.spec
	mkdir rpm
	cp -sR $(RPM_BUILD_ROOT)/RPMS/* ./rpm/


all:
	make py_exe
	make rpm_package


clear_py_exe:
	rm -rf dist
	rm -rf build
	rm -rf __pycache__


clear_rpm:
	rm -rf ~/rpmbuild


clear_all:
	make clear_rpm
	make clear_py_exe