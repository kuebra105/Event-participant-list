# Event-participant-list

## Task

You are organizing a small event and have received a list of registrations. However, the data is mixed and unstructured. Your job is to clean up the data and extract useful information.

```python
registrations = [
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
```
### 1. Filter the data
Remove all invalid entries (e.g. `int`, `None`).

### 2. Normalize the data
Create a list of dictionaries in the following format:  
`{"name": <Name>, "paid": <True/False>}`  
All entries that are just strings (like `"Anna"`) should be assumed **not paid**.

### 3. Remove duplicates
Each participant should appear **only once**.  
If someone appears multiple times and has paid in at least one entry, they should count as paid.

### 4. Print statistics
- How many participants are there in total?  
- How many have paid?  
- Print a **sorted list** of participants who haven’t paid yet (no duplicates).

### 📚 Tips
- Use `isinstance()` to check types.  
- Use `for` loops, `if` statements, lists, and dictionaries.
- Use a `set()` to remove duplicates.