set(DOCUMENTATION "Hello World")

itk_module(ITKBufferConvertion
  DEPENDS
    ITKCommon  
  TEST_DEPENDS 
    ITKTestKernel
  DESCRIPTION 
    "${DOCUMENTATION}"   
  )  
