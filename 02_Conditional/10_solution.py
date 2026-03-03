#  10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years- Puppy food, Cat:>5 years-Senior cat food).

pet = "Cat"
age = 1

if (pet == "Dog" and age < 2):
    pet_food = "Puppy food"
elif (pet == "Cat" and age > 5):
    pet_food = "Senior cat food"
else:
    pet_food = "No specific food category."

print("Type of pet food: ",pet_food )