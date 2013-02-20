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
vtkpoints.InsertNextPoint(0,0,0) 
vtkpoints.InsertNextPoint(2,3,4) 
vtkpoints.InsertNextPoint(5,9,2) 
vtkpoints.InsertNextPoint(4,5,6) 
vtkpoints.InsertNextPoint(7,8,5) 
vtkpoints.InsertNextPoint(0,0,1) 
vtkpoints.InsertNextPoint(0,1,0) 
vtkpoints.InsertNextPoint(1,0,0) 
vtkpoints.InsertNextPoint(0,1,1) 
vtkpoints.InsertNextPoint(1,1,0) 

lines = vtk.vtkCellArray()

for iii in range(9):
  line = vtk.vtkLine()
  line.GetPointIds().SetId(0,iii)
  line.GetPointIds().SetId(1,iii+1)
  lines.InsertNextCell( line );

polydata = vtk.vtkPolyData()
polydata.SetPoints(vtkpoints)
polydata.SetLines( lines  )
# data pointer
pd = polydata.GetPointData()
cd = polydata.GetCellData()
DeepCopy = 1
# color the points
vtkdataarray = vtkNumPy.numpy_to_vtk( range(9) , DeepCopy) 
vtkdataarray.SetName("similarity")
cd.AddArray( vtkdataarray )
# displacments
vtkvectorarray = vtkNumPy.numpy_to_vtk( [(1,1,2),(1,2,2),(1,9,2),(4,1,2),(7,1,2),(6,1,2),(1,4,2),(1,3,2),(1,1,0),(0,1,2)] , DeepCopy) 
vtkvectorarray.SetName("displacement")
pd.AddArray( vtkvectorarray )

polydatawriter = vtk.vtkPolyDataWriter()
polydatawriter.SetFileName("test.vtk")
polydatawriter.SetInput(polydata)
polydatawriter.Update()
