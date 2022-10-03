"""
main routes file
"""


from typing import Optional
from fastapi import APIRouter, UploadFile, File
from utils.predictor import predict

router = APIRouter(prefix="/audio", tags=["audio"])


@router.get("/")
def read_root():
    """
    Testing this shit
    """
    return {"Hello": "World"}


@router.post("")
async def get_prediction(file: UploadFile = File(...)):
    """
    The function runs the Model receives the audio file
    the file is then passed to the model and the prediction is returned
    as response
    """
    print("name of the file", file.filename)
    try:
        contents = file.file.read()
        with open(file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    prediction = predict(contents)

    return {"prediction": prediction}
