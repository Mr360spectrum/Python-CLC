# Karter Ence
# 11/21/2019
# Reading and Writing to Files
import pickle, shelve
# variety = ["sweet", "bread and butter", "dill"]
# shape = ["whole", "spear", "chips"]
# brands = ["Claussen", "Heinz", "Vlassic"]

# f = open("pickles.dat", "wb")
# pickle.dump(variety, f)
# pickle.dump(shape, f)
# pickle.dump(brands, f)

# f = open("pickles.dat", "rb")
# variety = pickle.load(f)
# shape = pickle.load(f)
# brands = pickle.load(f)

# print(variety)
# print(shape)
# print(brands)

# f.close()

s = shelve.open("pickles.dat")
s["variety"] = ["sweet", "bread and butter", "dill"]
s["shape"] = ["whole", "spear", "chips"]
s["brands"] = ["claussen", "Heinz", "Vlassic"]
s.sync()