from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

prompt = input("enter the prompt:  ").lower()


# functions are needed for the further work
def play_greetings():
    print("This is a greeting")


def increase_speed():
    print("The speed is increased")


commands = {
    "intents": {
        "greeting": {
            "examples": ["hi", "hey", "hello", "heyo", "good morning", "good afternoon",
                         "good evening", "good night", "morning", "evening", "night",
                         "ey up", "hey there", "hello there", "welcome"],
            "responses": play_greetings
        },
        "speed_increase": {
            "examples": ["speed up", "go faster", "faster", "increase speed", "accelerate",
                         "run", "forward", "you go faster", "exceed lightspeed", "accelerate vehicle",
                         "onwards", "to infinity and beyond", "speedy", "make like the wind", "fly on",
                         "fly up"],
            "responses": increase_speed
        }
    }
}

corpus = []
target_vector = []
# tokenization is pre-installed in vectorizer
tfid = TfidfVectorizer(analyzer="char")
classifier_probability = LogisticRegression()
classifier = LogisticRegression()

# getting intent
for intent_name, intent_data in commands["intents"].items():
    for example in intent_data["examples"]:
        corpus.append(example)
        target_vector.append(intent_name)

training_vector = tfid.fit_transform(corpus)
classifier_probability.fit(training_vector, target_vector)
classifier.fit(training_vector, target_vector)

best_intent = classifier.predict(tfid.transform([prompt]))[0]
index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
probabilities = classifier_probability.predict_proba(tfid.transform([prompt]))[0]
# probability of the best intent
best_intent_probability = probabilities[index_of_best_intent]
# When adding new intentions, this value should be decreased
print("probabilities of belonging to the greetings and speed_increase: ", probabilities)

# TODO ASK IF THE RESULT IS RIGHT? ADD TO LIST IF CORRECT, MAKE ANOTHER LIST FOR WRONG INTERPRETATION
### hhhh - false result for hello
### "go faster big boy", "zroom", "enter lightspeed" - false result for hello