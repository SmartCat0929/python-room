import pickle
def foo():
    print("ok")
f = open("PICKLE_text", "rb")

data = f.read()
data = pickle.loads(data)

data()
