from textblob import TextBlob

statement = "Today I went to Barbeque Nation and the food was awesome. I enjoyed the meal."
blob = TextBlob(statement)
print("Sentiment Score: ", blob.sentiment.polarity)  # Result = 1.0

statement2 = "Today I went to Barbeque Nation and the Food was very good"
blob2 = TextBlob(statement2)
print("Sentiment Score: ", blob2.sentiment.polarity)  # Result = 0.909999

statement21 = "Today I went to Barbeque Nation and the Food was good"
blob21 = TextBlob(statement21)
print("Sentiment Score: ", blob21.sentiment.polarity)  # Result = 0.7

statement3 = "Today I went to Barbeque Nation and the Food was bad"
blob3 = TextBlob(statement3)
print("Sentiment Score: ", blob3.sentiment.polarity)  # Result = -0.69

statement4 = "Today I went to Barbeque Nation and the Food was terrible"
blob4 = TextBlob(statement4)
print("Sentiment Score: ", blob4.sentiment.polarity)  # Result = -1.0

print(blob.detect_language())
for word, pos in blob.tags:  # what part of speech each word in a text corresponds to
    print (word, pos)  # the attribute of the TextBlob object we’ll use to access this information is .tags
    """NN: noun
    JJ: adjective
    IN: preposition
    VB_: verb(the _ gets replaced with various letters depending on the form of the verb)"""

for sentence in blob.sentences: # sentences in a text data
    print ("sentence = ", sentence)
for word in blob.sentences[1].words: # words in a sentence
    print ("word = ", word)
for np in blob.noun_phrases: # noun phrases in a text
    print ("noun phrase = ", np)

blob_In_arabic = blob.translate(from_lang='en', to ='ar')
print (blob_In_arabic)

article = """Boston-based money manager, Putnam Investments, has fallen on some hard times. As reported in this Boston Globe article, the company announced that it is going to cut 115 jobs or about 8% of its workforce given the continued outflow of assets from their firm. Currently managing over $150 billion in assets across almost 80 different strategies, the firm blames the rise of passive investing for its current predicament."""

article1 = """Dozens of students were returning from a summer camp when their driver paused to grab a something at a market in Yemen's Saada province. It was there, as the students sat waiting to resume their journey home on Thursday, that a Saudi-led coalition airstrike hit their school bus.
Hours later, well after the blast's violent rumble gave way to sirens and the victim's screams, a clearer sense of the human cost has emerged: At least 29 children under the age of 15, some as young as 6 years old, were killed in the attack, according to the International Committee of the Red Cross.
Citing "local officials," the head of the international aid group's delegation in Yemen says that in total at least 50 people died and dozens more were injured."""

article2 = """BENGALURU: The poor and the needy now have places where they can get food. Public fridges set up by communities at BTM L ayout, Brookfields, Indiranagar, Koramangala and Benson Town have opened an avenue for those with surplus food to help the hungry. NGOs involved in the endeavour say at least 400 people will benefit from these fridges daily."""

article_blob = TextBlob(article1)
mood = 0
for sss in article_blob.sentences:
    print ("sentence = ", sss)
    print ("sentiment = ", sss.sentiment.polarity)
    mood += sss.sentiment.polarity # sum up the sentiment value whether positive or negative
if mood>0:
    mood_str="POSITIVE"
else:
    mood_str = "NEGATIVE"
print ("mood of article is: ", mood_str)
