#dog age

dog_age = float(input("Enter dog age: "))
dog_years = 0.0

if dog_age <= 2:
    dog_years = dog_age * 10.5
else:
    dog_years = 2 * 10.5
    dog_years_after = dog_age - 2
    dog_years += dog_years_after * 4

print(f"The dog's age in dog's years is: {dog_years} years")