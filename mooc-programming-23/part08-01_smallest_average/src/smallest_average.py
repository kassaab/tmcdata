def smallest_average(person1: dict, person2: dict, person3: dict):
    person1Aver = (person1['result1'] + person1['result2'] + person1['result3'])/3
    person2Aver = (person2['result1'] + person2['result2'] + person2['result3'])/3
    person3Aver = (person3['result1'] + person3['result2'] + person3['result3'])/3

    if person1Aver < person2Aver and person1Aver < person3Aver:
        return person1
    elif person2Aver < person1Aver and person2Aver < person3Aver:
        return person2
    return person3


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))