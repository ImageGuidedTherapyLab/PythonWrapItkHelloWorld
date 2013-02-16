
Wrap an external project with python bindings
==============================================

http://www.itk.org/Wiki/ITK/Release_4/Wrapping/BuildProcess#External_Project

## example output

 >>> import itk
 >>> df = itk.Dummy.F.New()
 >>> df.GetValue()
 1.0
 >>> drgb = itk.Dummy.RGBUC.New()
 >>> drgb.GetValue()
 itkRGBPixel(1  1  1)
