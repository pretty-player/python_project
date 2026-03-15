from collections import deque, namedtuple, ChainMap, Counter, OrderedDict, defaultdict

# --- 1. Deque (Double-Ended Queue) ---
# Perfect for queues and stacks; faster than lists for adding/removing at the start.
print("--- Deque ---")
dq = deque(["Task2", "Task3"])
dq.append("Task4")      # Add to right
dq.appendleft("Task1")  # Add to left
print(f"Full Deque: {dq}")
dq.pop()                # Remove from right
dq.popleft()            # Remove from left
print(f"After pops: {dq}\n")


# --- 2. NamedTuple ---
# Gives names to tuple indexes. Makes code much more readable.
print("--- NamedTuple ---")
Student = namedtuple('Student', ['name', 'id', 'grade'])
s1 = Student(name="Alice", id="A101", grade="A")
print(f"Student details: Name={s1.name}, ID={s1.id}, Grade={s1.grade}\n")


# --- 3. ChainMap ---
# Groups multiple dictionaries into a single view. Great for app settings.
print("--- ChainMap ---")
default_settings = {"theme": "light", "font": "Arial"}
user_settings = {"theme": "dark"}
# It searches from left to right; user settings override defaults
settings = ChainMap(user_settings, default_settings)
print(f"Active Theme: {settings['theme']}") # 'dark'
print(f"Active Font: {settings['font']}\n")  # 'Arial'


# --- 4. Counter ---
# A dictionary subclass for counting hashable objects.
print("--- Counter ---")
word = "mississippi"
char_counts = Counter(word)
print(f"Character frequency in '{word}': {dict(char_counts)}")
print(f"Two most common: {char_counts.most_common(2)}\n")


# --- 5. OrderedDict ---
# Remembers the order items were inserted. (Note: standard dicts do this now,
# but OrderedDict is still useful for reordering operations).
print("--- OrderedDict ---")
ord_dict = OrderedDict()
ord_dict['first'] = 1
ord_dict['second'] = 2
ord_dict['third'] = 3
print(f"OrderedDict items: {list(ord_dict.items())}\n")


# --- 6. DefaultDict ---
# Prevents KeyError by providing a default value for a non-existent key.
print("--- DefaultDict ---")
marks_data = [('Math', 90), ('Science', 85), ('Math', 95), ('History', 80)]
# We initialize it with a list factory
subject_marks = defaultdict(list)
for subject, mark in marks_data:
    subject_marks[subject].append(mark)

print("Grouped Marks:")
for sub, marks in subject_marks.items():
    print(f"{sub}: {marks}")