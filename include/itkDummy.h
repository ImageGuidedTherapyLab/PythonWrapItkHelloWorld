#ifndef __itkDummy_h
#define __itkDummy_h

#include "itkObject.h"

namespace itk
{
/** \class Dummy
 * \brief a dummy class to return a dummy value
 */
template< class TValue >
class ITK_EXPORT Dummy: public Object
{
public:
  /** Standard class typedefs. */
  typedef Dummy                      Self;
  typedef Object                     Superclass;
  typedef SmartPointer< Self >       Pointer;
  typedef SmartPointer< const Self > ConstPointer;

  /** Method for creation through the object factory. */
  itkNewMacro(Self);

  /** Run-time type information (and related methods). */
  itkTypeMacro(Dummy, Object);

  TValue GetValue() const
  {
    //return NumericTraits<TValue>::OneValue();
    return static_cast<TValue>(1.0);
  }
 protected:
  Dummy() {};
  ~Dummy() {};
  virtual void PrintSelf(std::ostream& os, Indent indent) const
  {
    Superclass::PrintSelf( os, indent );
  }

private:
  Dummy(const Self &);    //purposely not implemented
  void operator=(const Self &); //purposely not implemented
};
} // end namespace itk

#endif

