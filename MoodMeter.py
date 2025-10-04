from textblob import TextBlob

print("="*50)
print("Welcome to SENTIMENT ANALYZER!! 😊")
print("="*50)

print("This Program tells you about the type of text you have written: ")
print("It is Positive 😃")
print("It is Negative ☹️")
print("It is Neutral 😐")

print("To exit this program, Kindly type - 'quit' ")
print("="*50)

while True:
    user_input = input("Enter your text: ")

    if user_input.lower()=="quit":
        print("Bye!Hope you enjoyed it!")
        break

    if user_input.strip()=="":
        print("Please enter something")
        continue

    blob = TextBlob(user_input)
    Polarity = blob.sentiment.polarity
    Subjectivity = blob.sentiment.subjectivity


    print("="*50)
    print("RESULT: ")
    print("Polarity Score: ",round(Polarity,2))
    print("Subjectivity Score: ",round(Subjectivity,2))

    if(Polarity> 0.1):
        print("Positive 😃")
    elif (Polarity<-0.1):
        print("Negative ☹️")
    else:
        print("Neutral 😐")

    





