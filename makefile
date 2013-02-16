ITK_GCCXML_INSTALL=/opt/apps/ITK/gccxml-gcc-4.4.3
all: Makefile itkDummy.h
	make -f Makefile
Makefile: CMakeLists.txt
	cmake -DBUILD_SHARED_LIBS=ON  -DCMAKE_BUILD_TYPE=Debug -DCMAKE_VERBOSE_MAKEFILE=ON -DITK_WRAP_PYTHON=ON -DITK_WRAP_double=ON -DINSTALL_WRAP_ITK_COMPATIBILITY=OFF -DITK_USE_SYSTEM_GCCXML=ON -DGCCXML=$(ITK_GCCXML_INSTALL)/bin/gccxml -DITK_USE_SYSTEM_SWIG=ON -DPYTHON_EXECUTABLE=$(EPD_ROOT)/bin/python -DPYTHON_INCLUDE_DIR=$(EPD_ROOT)/include/python2.7 -DPYTHON_LIBRARY=$(EPD_ROOT)/lib/libpython2.7.so ../InsightToolkit-4.3.0
