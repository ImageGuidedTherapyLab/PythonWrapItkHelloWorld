import itk 
import vtk
import vtk.util.numpy_support as vtkNumPy 

pixeltype = itk.D 
dim = 3 
traitstype = itk.DefaultStaticMeshTraits[pixeltype, dim, dim, pixeltype] 
pointsettype = itk.PointSet[ pixeltype, dim, traitstype ] 
pointset1 = pointsettype.New() 
print dir(pointset1)


pointType = itk.Point[pixeltype,dim] 
pp = pointType() 
pp.SetElement(0,1)
pp.SetElement(1,3)
pp.SetElement(2,5)
pointset1.SetPoint(1, pp)
pp.Fill(2)
pointset1.SetPoint(2, pp)
pp.Fill(4)
pointset1.SetPoint(3, pp)
print "# point",pointset1.GetNumberOfPoints()
pointExists = pointset1.GetPoint(0, pp)
print pp


# write vtk points file
vtkpoints= vtk.vtkPoints()
vertices= vtk.vtkCellArray()
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(0,0,0) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(2,3,4) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(5,9,2) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(4,5,6) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(7,8,5) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(0,0,1) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(0,1,0) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(1,0,0) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(0,1,1) )
vertices.InsertNextCell( 1 ); vertices.InsertCellPoint( vtkpoints.InsertNextPoint(1,1,0) )

polydata = vtk.vtkPolyData()
polydata.SetPoints(vtkpoints)
polydata.SetVerts( vertices )
# data pointer
pd = polydata.GetPointData()
DeepCopy = 1
# color the points
vtkdataarray = vtkNumPy.numpy_to_vtk( range(10) , DeepCopy) 
vtkdataarray.SetName("similarity")
pd.AddArray( vtkdataarray )
# displacments
vtkvectorarray = vtkNumPy.numpy_to_vtk( [(1,1,2),(1,2,2),(1,9,2),(4,1,2),(7,1,2),(6,1,2),(1,4,2),(1,3,2),(1,1,0),(0,1,2)] , DeepCopy) 
vtkvectorarray.SetName("displacement")
pd.AddArray( vtkvectorarray )

polydatawriter = vtk.vtkPolyDataWriter()
polydatawriter.SetFileName("test.vtk")
polydatawriter.SetInput(polydata)
polydatawriter.Update()
