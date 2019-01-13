import ratings

def test_rate():
    rating = ratings.rate({1: 55, 2: 143, 3: 0, 4: 200, 5: 98})
    assert rating == 3.62
