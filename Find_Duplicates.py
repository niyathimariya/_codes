# TCS_NQT
# s=["Headphones","Speakers","Keyboards","Microphones","Headphones","Speakers"]
# Remove duplicates.
# Find count.
# Arrange in ascending order and descending order

def process_list(s):
    # Remove duplicates by converting the list to a set, then back to a list
    s_unique = list(set(s))
    
    # Find count of unique elements
    count = len(s_unique)
    
    # Arrange in ascending order
    s_ascending = sorted(s_unique)
    
    # Arrange in descending order
    s_descending = sorted(s_unique, reverse=True)
    
    return s_unique, count, s_ascending, s_descending

# Example usage
s = ["Headphones", "Speakers", "Keyboards", "Microphones", "Headphones", "Speakers"]
s_unique, count, s_ascending, s_descending = process_list(s)
print("Unique elements:", s_unique)
print("Count of unique elements:", count)
print("Ascending order:", s_ascending)
print("Descending order:", s_descending)