from CGAL import CGAL_Kernel
from CGAL import CGAL_Triangulation_3
t=CGAL_Triangulation_3 .Delaunay_triangulation_3()
l=[]
l.append(CGAL_Kernel.Point_3(1,1,1))
l.append(CGAL_Kernel.Point_3(2,2,2))
l.append(CGAL_Kernel.Point_3(441,41,84))
l.append(CGAL_Kernel.Point_3(1,1,8))
t.insert_range(l)

for p in t.finite_vertices():
  print p.point()
