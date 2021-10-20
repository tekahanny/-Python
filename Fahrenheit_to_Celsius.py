# class Fahrenheit_to_Celsius:
#     def __init__(self, fahrenheit):
#         self.fahrenheit = fahrenheit

#     def formula(self):
#         celsius = (self.fahrenheit - 32) * (5/9)
#         return celsius

# print("Enter Tempreature in Fahrenheit: ")
# fah = int(input())
# change = Fahrenheit_to_Celsius(fah)
# cel = change.formula()
# print(f"{fah} Fahrenheit is {cel} Celsius")


class Coffee:
    def __init__(self, cream, sugar, half_and_half):
        self.cream = cream
        self.sugar = sugar
        self.half_and_half = half_and_half
 
 
morning_joe = Coffee(True, False, True)
print(morning_joe.cream)
print(morning_joe.sugar)
print(morning_joe.half_and_half)
 
for val in [
    "cream",
    "pumpkin spice",
    "cinnamon",
    "sugar",
    "half_and_half",
]:
    print()
    print(hasattr(morning_joe, val))
    print()
    if hasattr(morning_joe, val):
        setattr(
            morning_joe, val, not getattr(morning_joe, val)
        )
 
print(
    morning_joe.cream,
    morning_joe.sugar,
    morning_joe.half_and_half,
)



        


        
p