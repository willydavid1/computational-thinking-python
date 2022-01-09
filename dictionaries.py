my_dict = {
    "david": 35,
    "erika": 32,
    "jaime": 50,
    "nested": {
        "tom": 20
    }
}

my_dict["david"] # 35

my_dict["test"] # KeyError test

my_dict.get('test', 30) # returns 30 if key test does not exist
my_dict.get('david', 30) # 35

# Get Nested
my_dict['nested']['tom']
my_dict.get('nested').get('tom')

# Update value
my_dict["jaime"] = 20


# Add new key
my_dict["pedro"] = 70


# Delete key
del my_dict["jaime"]


# Iter
for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key, val)


# Check if a key exist in a dictionary
'david' in my_dict # True
'Tom' in my_dict # False


# Dictionary Comprehension
my_dict.keys()

my_dict.values()

my_dict.items()

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = { key: val * 2 for (key, val) in dict1.items() }
print(double_dict1)
