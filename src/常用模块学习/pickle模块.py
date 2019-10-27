import pickle


def foo():
    print("ok")


data = pickle.dumps(foo)

f = open("PICKLE_text", "wb")
f.write(data)
f.close()
