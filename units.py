import pickle,os

model_folder_path= "model"
def pred_class(math_score,reading_score,writing_score):

    clf_model = pickle.load(open(f'{model_folder_path}/model.pkl', 'rb'))
    pred=clf_model.predict([[math_score,reading_score,writing_score]])

    return pred[0]


# print(pred_class(70,80,90))
    