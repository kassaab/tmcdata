import json


def get_datatype(value):
    if isinstance(value, dict):
        return {"type": "object", "properties": get_datatypes_dict(value)}
    elif isinstance(value, list):
        return {"type": "list", "items": get_datatypes_list(value)}
    else:
        datatype_name = type(value).__name__
        if datatype_name == "int":
            datatype_name = "integer"
        elif datatype_name == "float":
            datatype_name = "number"
        elif datatype_name == "bool":
            datatype_name = "boolean"
        elif datatype_name == "str":
            datatype_name = "string"
        return {"type": datatype_name}

def get_datatypes_dict(dictionary):
    datatype_dict = {}
    for key, value in dictionary.items():
        datatype = get_datatype(value)
        datatype_dict[key] = datatype
    return datatype_dict

def get_datatypes_list(lst):
    datatypes = []
    for item in lst:
        datatype = get_datatype(item)
        datatypes.append(datatype)
    return datatypes

def extract_datatypes(input_data):
    datatype_dict = get_datatypes_dict(input_data)
    return datatype_dict


with open('file1.json', 'r') as file:
    input_data = json.load(file)


datatype_dict = extract_datatypes(input_data)
schema = json.dumps(datatype_dict, indent=4)


print(schema)





# with open('file1.json') as f:
#     # data = f.read()
#     data = json.load(f)
# # students = json.loads(data)

# # print(data)
# schema = {}
# dval = {}
# for key, value in data.items():
#     if isinstance(value, int):
#         fty = 'int'
#     elif isinstance(value, float):
#         fty = 'float'
#     elif isinstance(value, bool):
#         fty = 'bool'
#     elif isinstance(value, str):
#         fty = 'str'
#     elif isinstance(value, dict):
#         fty = 'dict'
#         dval = value
#     elif isinstance(value, list):
#         ty = 'list'
    
#     schema[key] = {"type": fty}
#     # if fty == 'dict':
#     #     print(f'dval= {dval}')

#     if fty == 'dict':
#         for k, val in dval.items():
#             if isinstance(val, int):
#                 ity = 'int'
#             elif isinstance(val, float):
#                 ity = 'float'
#             elif isinstance(val, bool):
#                 ity = 'bool'
#             elif isinstance(val, str):
#                 ity = 'str'
            
#             schema[key] = {"type": fty, "items": ity}

            
       

# print(schema)











# for d in data:
#     print(d['name'], end=' ')
#     print(d['age'], 'years', end=' ')
#     hobbies = ', '.join(d['hobbies'])
#     print(f'({hobbies})')















# def print_persons(filename: str):
#     with open(filename) as myfile:
#         data = myfile.read()
#     students = json.loads(data)

#     for student in students:
#         print(student['name'], end=' ')
#         print(student['age'], 'years', end=' ')
#         hobbies = ', '.join(student['hobbies'])
#         print(f'({hobbies})')

# if __name__ == '__main__':
#     if False:
#         students_info = input("Student information: ")
#     else:
#         students_info = "file1.json"
    
#     print_persons(students_info)