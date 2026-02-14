import numpy as np
import trimesh

def heightmap_to_mesh(height_map):
    h, w = height_map.shape
    vertices = []
    faces = []

    for y in range(h):
        for x in range(w):
            z = height_map[y, x] * 10
            vertices.append([x, y, z])

    vertices = np.array(vertices)

    for y in range(h - 1):
        for x in range(w - 1):
            i = y * w + x
            faces.append([i, i+1, i+w])
            faces.append([i+1, i+w+1, i+w])

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    mesh.export("outputs/model.stl")
