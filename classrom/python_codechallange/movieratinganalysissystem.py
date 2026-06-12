#program for movie rating analyser

ratings = {     "Inception": 4.8,     "Avatar": 4.3,     "Titanic": 4.5,     "Joker": 4.7,     "Frozen": 3.8,     "Interstellar": 4.9,     "Dune": 4.6,     "Up": 4.1,     "Coco": 4.4,     "Cars": 3.9 } 

print("rating above 4.5 : ")
for movie , rate in ratings.items() :
    if rate > 4.5:
        print(movie)

#highest rate movie
highest_rate = max(ratings , key = ratings.get)
print("highest_rate : " , "(" , ratings[highest_rate] , ")" , sep = " ")

#lowest rating movie
lowest_rate = min(ratings , key = ratings.get)
print("lowest_rate : ", "(" , ratings[lowest_rate] , ")" , sep =" " )

#average rating
average_rating = sum(ratings.values()) / len(ratings)
print("Average Rating:", round(average_rating, 2))

# Create recommendation list (rating >= 4.5)
recommendations = []

for movie, rating in ratings.items():
    if rating >= 4.5:
        recommendations.append(movie)

print("Recommended Movies:", recommendations)
