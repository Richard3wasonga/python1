num1,num2 = 200,123

if num1 < num2:
    print(f"sure {num1} is less than {num2}")
elif num1 == num2:
    print(f"sure {num1} is equal to {num2}")
else:
    print(f"{num1} is greater than {num2}")
sentence ='''
This is a random sentence i have just written.
'''

if "have" in sentence:
    print("The word have is in sentence")

if "monumental" in sentence:
    print("The word monumental is not in sentence")

if len(sentence) > 10:
    print("This is a very long sentence")
