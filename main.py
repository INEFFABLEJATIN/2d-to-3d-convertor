from fastapi import FastAPI, File, UploadFile
import shutil
from image_processing import image_to_heightmap
from mesh_generator import heightmap_to_mesh

app = FastAPI()


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("File saved at:", file_path)

        height_map = image_to_heightmap(file_path)
        print("Height map created")

        heightmap_to_mesh(height_map)
        print("Mesh created")

        return {"message": "3D model created successfully"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
@app.get("/")
def home():
    return {"message": "2D to 3D API Running Successfully"}
