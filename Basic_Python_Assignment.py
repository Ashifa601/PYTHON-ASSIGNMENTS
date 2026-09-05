# Survey Feedback Analyzer

# Step 1: Preloaded Feedback Data

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):

    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Clean Feedback

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text = ' '.join(text.split())

    text = text.lower()

    feedback_data['Feedback'][i] = text


# Step 4: Word Count Function

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("\nNumber of feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Number of feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Number of feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# Step 5: Final Cleaned Feedback Data

print("\nFinal Cleaned Feedback Data:")
print(feedback_data)


# Average Rating

average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])

print("\nAverage Rating:", round(average_rating, 2))


# Longest Feedback

longest_feedback = ""
longest_word_count = 0
longest_name = ""

for i in range(len(feedback_data['Feedback'])):

    words = feedback_data['Feedback'][i].split()
    word_count = len(words)

    if word_count > longest_word_count:
        longest_word_count = word_count
        longest_feedback = feedback_data['Feedback'][i]
        longest_name = feedback_data['Name'][i]

print("\nLongest Feedback:")
print("Name:", longest_name)
print("Feedback:", longest_feedback)
print("Word Count:", longest_word_count)


# Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:
        unique_words.add(word)

print("\nUnique Words:")
print(sorted(unique_words))


# Optional: Sort Feedbacks by Rating

sorted_data = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[3],
    reverse=True
)

print("\nFeedbacks Sorted by Rating:")

for item in sorted_data:
    print(item)