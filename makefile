all: Makefile itkDummy.h
	make -f Makefile
Makefile: CMakeLists.txt itkDummy.wrap
	cmake -DCMAKE_INSTALL_PREFIX=$(ITK_HOME) -DBUILD_SHARED_LIBS=ON  -DCMAKE_BUILD_TYPE=Debug -DCMAKE_VERBOSE_MAKEFILE=ON -DITK_WRAP_PYTHON=ON -DITK_WRAP_double=ON -DWrapITK_DIR=$(ITK_HOME)/lib/cmake/ITK-4.3/WrapITK -DINSTALL_WRAP_ITK_COMPATIBILITY=ON -DITK_USE_SYSTEM_GCCXML=ON -DITK_USE_SYSTEM_SWIG=ON -DPYTHON_EXECUTABLE=$(EPD_ROOT)/bin/python -DPYTHON_INCLUDE_DIR=$(EPD_ROOT)/include/python2.7 -DPYTHON_LIBRARY=$(EPD_ROOT)/lib/libpython2.7.so
	# FIXME terrible hack for path errors and small bugs...
	rsync -avvz $(ITK_HOME)/lib/cmake/ITK-4.3/WrapITK/Configuration/Typedefs/ Typedefs/
	cp Typedefs/ITKCommonBaseSwigInterface.h.in Typedefs/ITKCommonBaseSwigInterface.h
clean:
	rm -rf CMakeCache.txt CMakeFiles/ lib/ Generators/ ITKIOFactoryRegistration/ Makefile Typedefs/ cmake_install.cmake gcc_xml.inc install_wrapitk_compatibility.cmake itkDummy.cxx itkDummy.xml itkDummySwigInterface.h.in dummyPython.cpp itkDummyPython.cpp

