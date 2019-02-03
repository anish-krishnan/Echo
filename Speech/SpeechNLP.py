# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from Person import Person

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = 'Hi my name is John'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
entities = client.analyze_entities(document).entities


for entity in entities:
    # entity_type = enums.Entity.Type(entity.type)
    print('=' * 20)
    print("entity type: "+str(entity.type))
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))

    if entity.type == 1:
        new_person = Person.Person(entity.name)
        #Save image
        #Trigger model to train again


print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))