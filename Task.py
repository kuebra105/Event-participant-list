from pprint import pprint


registrations: list[str | dict[str, str | bool] | int | None] = [ # that's a list with strings, dicts (with strings and bool) and int
    "Anna", 
    {"name": "Ben", "paid": True}, 
    "Clara", 
    {"name": "Daniel", "paid": False}, 
    "Anna", 
    {"name": "Elisa", "paid": True}, 
    42, 
    None, 
    {"name": "Clara", "paid": True}
]

# 1. Filter the data
filtered_registrations: list[str | dict[str, str | bool]] = []
for participant in registrations:
    if isinstance(participant, dict) or isinstance(participant, str):
        filtered_registrations.append(participant)

# 2. Normalize the data
normalized_registrations: list[dict[str, str | bool]] = []
for participant in filtered_registrations:
    if isinstance(participant, str): 
        normalized_registrations.append({"name": participant, "paid": False})
    else:
        normalized_registrations.append(participant)
print("All registrations:")
pprint(normalized_registrations, width=40)
print()

# 3. Remove duplicates
double: set[str] = set()
corrected_list: list[dict[str, str | bool]] = []
normalized_registrations.reverse()
for participant in normalized_registrations:
    name= participant.get("name")
    if isinstance(name, str) and name not in double:
        double.add(name)
        corrected_list.append(participant)
corrected_list.reverse()
print("Valid registrations:")
pprint(corrected_list, width=40)
print()


# 4. Print statistics
total_participants = len(corrected_list)
print(f"Total number of participants: {total_participants}")

paid_list: list[dict[str, str | bool]] = []
unpaid_list: list[dict[str, str | bool]] = []
for participant in corrected_list:
    if participant["paid"] == True:
        paid_list.append(participant)
    else:
        unpaid_list.append(participant)


print(f"Number of participants that haved paid: {len(paid_list)}")
print("Participants that have not paid yet:")
unpaid_list.sort(key=lambda x: x["name"]) # a list of dictionaries cannot be sorted without specifying which key to sort by; lambda is a function without a name defined directly.
pprint(unpaid_list, width=40)