itk_module_test()

set(ITKHelloWorldTests
itkDummyTest.cxx
)

set(ITKHelloWorld-Test_LIBRARIES
    "${ITKHelloWorld-Test_LIBRARIES};${PYTHON_LIBRARY}")

CreateTestDriver(ITKHelloWorld "${ITKHelloWorld-Test_LIBRARIES}"
    "${ITKHelloWorld}")

itk_add_test(NAME itkDummyTest
    COMMAND ITKHelloWorldTestDriver itkDummyTest)

