import pickle
import face_variant_sample_generation as ftrain
def set_id(key,value):
    pickle_in= open("users.pickle","rb")
    usr = pickle.load(pickle_in)
    usr.update({int(key):str(value)})
    pickle_out = open("users.pickle","wb")
    pickle.dump(usr,pickle_out)
    pickle_out.close()
    print(usr)
    ftrain.f_train(key)

def get_id():
    pickle_in= open("users.pickle","rb")
    usr = pickle.load(pickle_in)
    return usr

