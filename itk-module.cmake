set(DOCUMENTATION "Hello World")

itk_module(ITKHelloWorld
  DEPENDS
    ITKCommon  
  TEST_DEPENDS 
    ITKTestKernel
  DESCRIPTION 
    "${DOCUMENTATION}"   
  )  
