from collections import Counter
import string

article = """
Technology is transforming the modern world at a rapid pace. Businesses,
educational institutions, healthcare organizations, and governments are
increasingly adopting digital solutions to improve efficiency and provide
better services. The growth of artificial intelligence, cloud computing,
and data analytics has created new opportunities for innovation and
economic development. Many companies are investing heavily in research
and development to remain competitive in a constantly changing market.

Education has also benefited from technological advancements. Students
can access online learning platforms, digital libraries, and interactive
educational tools from anywhere in the world. Teachers are able to create
engaging learning experiences through multimedia content and virtual
classrooms. Technology has made education more accessible and flexible
for learners of all ages.

Healthcare systems are using technology to improve patient care and
medical research. Electronic health records, telemedicine, and advanced
diagnostic equipment help doctors provide accurate and timely treatment.
Researchers use powerful computing systems to analyze large amounts of
medical data and discover new treatments for diseases.

Despite these advantages, technology also presents challenges. Concerns
about data privacy, cybersecurity, and digital inequality continue to
grow. Organizations must implement strong security measures to protect
sensitive information. Governments and businesses must work together to
ensure that technological progress benefits society as a whole.

The future of technology is expected to bring even more innovations.
Artificial intelligence, automation, renewable energy systems, and smart
cities will likely play an important role in shaping the future. As
technology continues to evolve, individuals and organizations must adapt
to new developments and opportunities while addressing the challenges
that accompany progress.
"""

# Total Characters
total_characters = len(article)

# Total Sentences
sentences = article.split(".")
sentences = [s.strip() for s in sentences if s.strip()]
total_sentences = len(sentences)

# Remove punctuation and convert to lowercase
clean_text = article.lower()

for ch in string.punctuation:
    clean_text = clean_text.replace(ch, "")

words = clean_text.split()

# Total Words
total_words = len(words)

# Vowels and Consonants
vowels = 0
consonants = 0

for ch in clean_text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Longest and Shortest Word
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# Word Frequencies
word_freq = Counter(words)

# Most Frequent Word
most_frequent_word = max(word_freq, key=word_freq.get)

# Words Appearing Once
appear_once = [word for word, count in word_freq.items() if count == 1]

# Words Appearing More Than 5 Times
more_than_five = [word for word, count in word_freq.items() if count > 5]

# Count Words Starting with Each Alphabet
alphabet_count = {}

for word in words:
    first = word[0]
    alphabet_count[first] = alphabet_count.get(first, 0) + 1

# Unique Words
unique_words = set(words)

# Average Word Length
average_word_length = sum(len(word) for word in words) / total_words

# Vocabulary Size
vocabulary_size = len(unique_words)

# Output
print("========== ARTICLE ANALYSIS ==========")
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Frequent Word:", most_frequent_word)

print("\nWord Frequency Dictionary:")
print(dict(word_freq))

print("\nWords Appearing Only Once:")
print(appear_once)

print("\nWords Appearing More Than 5 Times:")
print(more_than_five)

print("\nWords Starting With Each Alphabet:")
print(alphabet_count)

print("\nUnique Words:")
print(unique_words)

print("\n========== TEXT SUMMARY ==========")
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Average Word Length:", round(average_word_length, 2))
print("Most Frequent Word:", most_frequent_word)
print("Vocabulary Size:", vocabulary_size)