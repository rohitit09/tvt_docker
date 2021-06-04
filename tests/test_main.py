import json

def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_sum(app, client):
    payload = '[1,2,3]'
    res= client.put(
        "/sum",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    assert res.json['status'] == 200
    assert res.json['result'] == 6

def test_sum1(app, client):
    payload = '[1,2,"a"]'
    res= client.put(
        "/sum",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    assert res.json['status'] == 400
    assert res.json['error'] == 'All inputs must be numeric'

def test_sum2(app, client):
    payload = '[1,2]'
    res= client.put(
        "/sum",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    assert res.json['status'] == 400
    assert res.json['error'] == 'Exactly 3 numbers are required'

def test_sum3(app, client):
    payload = '[1,2,a]'
    res= client.put(
        "/sum",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    assert res.json['status'] == 400
    assert res.json['error'] == 'input format not correct'

def test_sum4(app, client):
    payload = '[1,2,15]'
    res= client.put(
        "/sum",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    assert res.json['status'] == 200
    assert res.json['result'] == 18

