import pickle,os

model_folder_path= "model"
def pred_class(x,y,z):

    clf_model = pickle.load(open(f'model.pkl', 'rb'))
    pred=clf_model.predict([[x,y,z]])

    return pred[0]


# print(pred_class(70,80,90))
    