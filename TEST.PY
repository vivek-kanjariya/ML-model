import pickle

path = "C:\\Users\\Administrator\\Desktop\\INtel-AI_MANU_COURSE\\Week 6 - Dependencies\Dependencies\\voting_model.pkl"
with open(path, "rb") as f:
    model = pickle.load(f)

print(model.__module__, model.__class__.__name__)
