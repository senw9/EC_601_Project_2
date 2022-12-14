GOOGLE_APPLICATION_CREDENTIALS = "/Users/senwang/Desktop/EC 601/Project 2/client_secret_404201602489-88sjscsaka6m0hsjbucm6cq2iulru206.apps.googleusercontent.com.json"
# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Apple, headquartered in Cupertino, unveiled the new iPhone for $999 in the last three months. Cook said everybody love this new iPhone."
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))