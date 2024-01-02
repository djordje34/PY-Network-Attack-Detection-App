import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, FunctionTransformer

class PreprocessPipeline:
    _scaler_instance = None
    _encoder_instance = None
    
    @staticmethod
    def transformIP(ip_address):
        octets = str(ip_address).split('.')
        formatted_octets = [f'{int(octet):03d}' for octet in octets]
        return ''.join(formatted_octets)
    
    @staticmethod
    def getScaler():
        if PreprocessPipeline._scaler_instance is None:
            PreprocessPipeline._scaler_instance = joblib.load("apps/detector/static/models/scaler.save")  #need to load scaler for outside
        return PreprocessPipeline._scaler_instance
    
    def getEncoder():
        if PreprocessPipeline._encoder_instance is None:
            PreprocessPipeline._encoder_instance = joblib.load("apps/detector/static/models/encoder.save")  #need to load scaler for outside
        return PreprocessPipeline._encoder_instance
    
    @classmethod
    def preprocessData(cls, data):
        
        if isinstance(data, dict):
            data = pd.DataFrame([data])
            
        scaler = cls.getScaler()
        data['IPV4_SRC_ADDR'] = data['IPV4_SRC_ADDR'].apply(cls.transformIP)
        data['IPV4_DST_ADDR'] = data['IPV4_DST_ADDR'].apply(cls.transformIP)
        data = data.to_numpy()
        data_transformed = scaler.transform(data)
        return data_transformed
        
    @classmethod
    def preprocessDataDiag(cls, data):
        if isinstance(data, dict):
            data = pd.DataFrame([data])
        scaler = cls.getScaler()
        print(data)
        data_transformed = pd.DataFrame(scaler.inverse_transform(data), columns=data.columns, index=data.index)
        return data_transformed
        
    @classmethod 
    def inverseLabelEncoding(cls,target):
        encoder = cls.getEncoder()
        return encoder.inverse_transform(target)
        
"""     TESTING THE PIPELINE :
test_data = {
    'IPV4_SRC_ADDR': '192.168.1.180',
    'L4_SRC_PORT': 40549,
    'IPV4_DST_ADDR': '192.168.1.190',
    'L4_DST_PORT': 53,
    'PROTOCOL': 17,
    'L7_PROTO': 5.000,
    'IN_BYTES': 302,
    'OUT_BYTES': 755,
    'IN_PKTS': 3,
    'OUT_PKTS': 3,
    'TCP_FLAGS': 0,
    'FLOW_DURATION_MILLISECONDS': 0
}
preprocessed_test_data = PreprocessPipeline.preprocessData(test_data)

print(preprocessed_test_data)
"""