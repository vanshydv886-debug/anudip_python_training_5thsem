from collections import Counter
import re

resume = """
Name: Rahul Sharma

Email: rahul123@gmail.com
Phone: 9876543210

Skills:
Python, Java, SQL, Python, HTML, CSS, SQL

Education:
Bachelor of Computer Applications from ABC College

Projects:
Student Management System using Python and SQL
Online Shopping Website using HTML, CSS and JavaScript

Achievements:
Won Coding Competition
Completed Python Certification
"""

# Total Words
words = resume.split()
total_words = len(words)

# Total Characters
total_characters = len(resume)

# Extract Email IDs
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', resume)

# Extract Phone Numbers (10 digits)
phones = re.findall(r'\b\d{10}\b', resume)

# Extract Skills
skills_section = resume.split("Skills:")[1].split("Education:")[0]
skills = [skill.strip() for skill in skills_section.split(",")]

# Skill Count
skill_count = len(skills)

# Skill Frequency Report
skill_freq = Counter(skills)

# Duplicate Skills
duplicate_skills = [skill for skill, count in skill_freq.items()
                    if count > 1]

# Word Frequency
clean_words = []

for word in words:
    word = word.lower().strip(".,:")
    clean_words.append(word)

word_freq = Counter(clean_words)

# Repeated Keywords
repeated_keywords = [word for word, count in word_freq.items()
                     if count > 1]

# Most Frequent Word
most_frequent_word = max(word_freq, key=word_freq.get)

# Most Frequent Skill
most_frequent_skill = max(skill_freq, key=skill_freq.get)

# Output
print("========== RESUME ANALYSIS REPORT ==========")

print("Total Words:", total_words)
print("Total Characters:", total_characters)

print("\nEmail Found:", len(emails))
print("Email IDs:", emails)

print("\nPhone Numbers Found:", len(phones))
print("Phone Numbers:", phones)

print("\nTotal Skills Mentioned:", skill_count)

print("\nSkill Frequency Report:")
print(dict(skill_freq))

print("\nDuplicate Skills:")
print(duplicate_skills)

print("\nRepeated Keywords:")
print(repeated_keywords)

print("\nMost Frequent Word:", most_frequent_word)
print("Most Frequent Skill:", most_frequent_skill)

print("\n========== SUMMARY DASHBOARD ==========")
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Emails Found:", len(emails))
print("Phone Numbers Found:", len(phones))
print("Most Frequent Skill:", most_frequent_skill)