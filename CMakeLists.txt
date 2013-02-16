project(dummy)

cmake_minimum_required(VERSION 2.8)

find_package(ITK REQUIRED)
find_package(WrapITK REQUIRED)

itk_wrap_module("${PROJECT_NAME}")
  set(WRAPPER_LIBRARY_DEPENDS ITKCommon)
  itk_auto_load_submodules()
itk_end_wrap_module()

