from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class Recommender:
    _dataset = None
    
    def __init__(self):
        pass
        
    @staticmethod
    def getDataset():
        if Recommender._dataset is None:
            Recommender._dataset =  refs = pd.read_csv("apps/detector/static/data/data.csv")
        return Recommender._dataset
    
    def getRecommendations(self,data):
        dataset = Recommender.getDataset()
        selected_cols = ['L4_SRC_PORT', 'L4_DST_PORT', 'PROTOCOL', 'L7_PROTO', 'IN_BYTES', 'OUT_BYTES', 'IN_PKTS', 'OUT_PKTS', 'TCP_FLAGS', 'FLOW_DURATION_MILLISECONDS']
        y = dataset['Encoded_Attack']
        dataset = dataset[selected_cols]
        data = data[selected_cols]
        cosine_similarities = cosine_similarity(data, dataset)
        most_similar_indices = cosine_similarities.argsort(axis=1)[:, ::-1]
        first_most_similar_indices = most_similar_indices[:, 0]
        second_most_similar_indices = most_similar_indices[:, 1]
        fst_pred = y.iloc[first_most_similar_indices]
        sec_pred = y.iloc[second_most_similar_indices]
        prediction = [fst_pred,sec_pred]
        return prediction