datalist = [
    1876, 9.81, 3+4j,
      False, 'Itachi', 
      (5, -3), [7, 14], 
      {"Clan": 'Uchiha', "Ability": 'Sharingan'}
      ]

for item in datalist:
    print(f"Type of {item} is {type(item)}")

# Output:

"""
    Type of 1876 is <class 'int'>
    Type of 9.81 is <class 'float'>
    Type of (3+4j) is <class 'complex'>
    Type of False is <class 'bool'>
    Type of Itachi is <class 'str'>
    Type of (5, -3) is <class 'tuple'>
    Type of [7, 14] is <class 'list'>
    Type of {'Clan': 'Uchiha', 'Ability': 'Sharingan'} is <class 'dict'>
"""