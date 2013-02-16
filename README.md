
Wrap an external project with python bindings
==============================================

http://www.itk.org/Wiki/ITK/Release_4/Wrapping/BuildProcess#External_Project

## example output

```
>>> import dummyPython
>>> df = dummyPython.itkDummyF_New()
>>> dir(df)
['AddObserver', 'BreakOnError', 'Clone', 'CreateAnother', 'DebugOff', 'DebugOn', 'GetCommand', 'GetDebug', 'GetGlobalWarningDisplay', 'GetMTime', 'GetMetaDataDictionary', 'GetNameOfClass', 'GetPointer', 'GetReferenceCount', 'GetTimeStamp', 'GetValue', 'GlobalWarningDisplayOff', 'GlobalWarningDisplayOn', 'HasObserver', 'InvokeEvent', 'Modified', 'New', 'Print', 'RemoveAllObservers', 'RemoveObserver', 'SetDebug', 'SetGlobalWarningDisplay', 'SetMetaDataDictionary', '__New_orig__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__swig_destroy__', '__weakref__', 'cast', 'this', 'thisown']
>>> df.GetValue()
1.0
```
