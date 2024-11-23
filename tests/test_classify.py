def test_classify_document(client):

    payload = {
        "text": "This is a sample document for python modules.",
        "categories": ["education", "politics", "technology"]
    }

    response = client.post("/classify/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "classification" in data
    assert "labels" in data["classification"]
    assert "scores" in data["classification"]
    assert len(data["classification"]["labels"]) == len(payload["categories"])