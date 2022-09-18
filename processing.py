import open3d as o3d

# Load point cloud
i_path = "C:\\Users\\kostu\Documents\\bunny.tar\\bunny\\data\\bun180.ply"
o_path = "C:\\Users\\kostu\Desktop\\3dscan2print"
pcd = o3d.io.read_point_cloud(i_path)

# Voxel downsample
voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.00005)
# o3d.visualization.draw_geometries([voxel_down_pcd], window_name="Open3D", width=800, height=600)

# Estimate normals
voxel_down_pcd.estimate_normals()
# o3d.visualization.draw_geometries([voxel_down_pcd], window_name="Open3D", width=800, height=600, point_show_normal = True)

# Poisson reconstruction
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    poisson_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(voxel_down_pcd, depth=9)
    poisson_mesh.compute_triangle_normals()
# o3d.visualization.draw_geometries([poisson_mesh], window_name="Open3D", width=800, height=600)

# Filtering Mesh
poisson_mesh.filter_smooth_simple(number_of_iterations=5)
poisson_mesh.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([poisson_mesh], window_name="Open3D", width=800, height=600)

# # Mesh Decimation
# poisson_mesh.compute_vertex_normals()
# poisson_mesh.subdivide_loop(number_of_iterations=2)
# o3d.visualization.draw_geometries([poisson_mesh], window_name="Open3D", width=800, height=600)

#Export as STL
o3d.io.write_triangle_mesh(o_path+".\\mesh.stl", poisson_mesh)





# def voxelization ():
#     poisson_mesh.scale(1 / np.max(poisson_mesh.get_max_bound() - poisson_mesh.get_min_bound()), center = poisson_mesh.get_center())
#     voxels = o3d.geometry.VoxelGrid. create_from_triangle_mesh(poisson_mesh,voxel_size=0.05)
#     return voxels

# #Scaling
# poisson_mesh.scale(0.5, center=poisson_mesh.get_center())
# o3d.visualization.draw_geometries([poisson_mesh], window_name="Open3D", width=800, height=600)
