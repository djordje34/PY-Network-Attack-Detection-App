import os
import pandas as pd
from django.core.wsgi import get_wsgi_application
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "net_attack_detection.settings")
application = get_wsgi_application()

from apps.detector.models import NetworkData

def load_and_populate_model(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    label_0_count = (df['Label'] == 0).sum()
    label_1_count = (df['Label'] == 1).sum()
    current_ratio = label_0_count / label_1_count
    
    desired_ratio = 3
    target_label_1_count = int(label_0_count / desired_ratio)

    rows_to_drop = df[df['Label'] == 1].index[:label_1_count - target_label_1_count]
    df = df.drop(rows_to_drop)
    df = df.sample(frac=1).reset_index(drop=True)
    
    df.drop(columns=['Label','Attack'],inplace=True)
    total_rows = len(df)
    
    for index, row in tqdm(df.iterrows(), total=total_rows, desc="Processing rows"):
        data_instance = NetworkData(**row.to_dict())
        data_instance.save()

if __name__ == "__main__":
    csv_file_path = "apps/detector/static/data/ton_iot.csv" 
    load_and_populate_model(csv_file_path)