import trimesh

# Load mesh files from specified paths
mesh_path_15 = "/home/dhiren/13_Images/Model_1.obj"
mesh_path_25 = "/home/dhiren/25_Images/Model_2.obj"

mesh_15 = trimesh.load(mesh_path_15, force='mesh')
mesh_25 = trimesh.load(mesh_path_25, force='mesh')

# Display mesh statistics
print("15 Views Mesh:")
print(f"  Number of Vertices: {len(mesh_15.vertices)}")
print(f"  Number of Faces: {len(mesh_15.faces)}")
print(f"  Bounding Box Volume: {mesh_15.bounding_box.volume:.2f}")

print("\n25 Views Mesh:")
print(f"  Number of Vertices: {len(mesh_25.vertices)}")
print(f"  Number of Faces: {len(mesh_25.faces)}")
print(f"  Bounding Box Volume: {mesh_25.bounding_box.volume:.2f}")
