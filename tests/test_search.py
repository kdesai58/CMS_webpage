def test_search_documents(client):

    query = {"query": "educational content", "top_k": 3}

    response = client.post("/search/", json=query)

    assert response.status_code == 200
    data = response.json()
    assert "query" in data
    assert "results" in data
    assert len(data["results"]) <= 3