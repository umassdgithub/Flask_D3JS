from flask import Flask, request,Response, render_template
import requests
import json
import glob

import pydicom
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")


@app.route('/data', methods=['GET'])
def returnData():
    
    fileNumber=request.args.get("file")
    # Sanity Check
    print(fileNumber)
    if fileNumber is None:
        fileNumber = "brain_001.dcm" 

    try:
        dicom_dataset = pydicom.dcmread(f"./Data/volume/{fileNumber}")
        
        return json.dumps(dicom_dataset.pixel_array.tolist())
    except Exception as ex:
        return str({"error":ex.__str__()})
@app.route("/files")
def files():
    files_list = [fl.split("/")[-1] for fl in glob.glob("./Data/volume/*.dcm")]
    return json.dumps(files_list)

if __name__ == '__main__':
    app.run(port=5001, debug=True)



