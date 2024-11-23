import os

def test_upload_file(client):

    file_content = b"Hello, World! Sample content of the PDF file."
    file_name = "sample.pdf"
    with open(file_name, "wb") as f:
        f.write(file_content)

    with open(file_name, "rb") as f:
        response = client.post("/upload/", files={"file": f})

    os.remove(file_name)

    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == file_name
    assert data["message"] == "File uploaded and processed"