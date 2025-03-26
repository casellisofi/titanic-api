import numpy as np
from app.schemas import PassengerData
from app.utils.preprocessing import convert_passenger_to_array

def test_convert_passenger_to_array():
    data = PassengerData(pclass=2, sex=1, age=28.0, sibsp=0, parch=0, fare=20.0, embarked=1)
    arr = convert_passenger_to_array(data)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1, 7)
    assert arr[0][1] == 1  
