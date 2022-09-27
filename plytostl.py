#requires python 3.6

import open3d as o3d
import os
import sys

# Load point cloud
def stl_convert(filename:str, search_dir:str):
    """Takes in either .ply or .las file and creates a .stl file. Returns stl filename."""
    pcd = o3d.io.read_point_cloud(os.path.join(search_dir, filename))

    # Voxel downsample
    voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.00005)

    # Estimate normals
    voxel_down_pcd.estimate_normals()

    # Poisson reconstruction
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        poisson_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(voxel_down_pcd, depth=9)
        poisson_mesh.compute_triangle_normals()

    # Filtering Mesh
    poisson_mesh.filter_smooth_simple(number_of_iterations=5)
    poisson_mesh.paint_uniform_color([1, 0.706, 0])
    #o3d.visualization.draw_geometries([poisson_mesh], window_name="Open3D", width=800, height=600)

    #Export as STL
    outfile = ".".join(filename.split(".")[:-1]) + ".stl"
    o3d.io.write_triangle_mesh(os.path.join(search_dir, outfile), poisson_mesh)
    return outfile

if __name__ == "__main__":
    if len(sys.argv) > 1:
        stl_convert(f"{sys.argv[1]}", ".")
    else:
        stl_convert("test.ply", ".")


