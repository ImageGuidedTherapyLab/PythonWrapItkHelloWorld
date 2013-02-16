project(dummy)

cmake_minimum_required(VERSION 2.8)

find_package(ITK REQUIRED)
find_package(WrapITK REQUIRED)

WRAP_LIBRARY("${PROJECT_NAME}")
  set(WRAPPER_LIBRARY_DEPENDS Base)
  AUTO_INCLUDE_MODULES()
END_WRAP_LIBRARY()

