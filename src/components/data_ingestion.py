import os
import sys
from exception import CustomException
from logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestuinConfig:
    train_data_parth: str= os.path.join("artifacts","train.csv")
    test_data_parth: str= os.path.join("artifacts","test.csv")
    raw_data_parth: str= os.path.join("artifacts","data.csv")

class DataIngestionConfig:
    
    def __init__(self):
        self.ingestion_congif =DataIngestuinConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion or component")
        try:
            df = pd.read_csv(r"D:/mlprojects/project1/notebook/data/stud.csv")
            logging.info("read dataset as data frame")
            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_parth),exist_ok=True)
            df.to_csv(self.ingestion_congif.raw_data_parth,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_congif.train_data_parth,index=False,header=True)

            test_set.to_csv(self.ingestion_congif.test_data_parth,index=False,header=True)
            
            logging.info("Ingection of the data is completed")
            
            return (self.ingestion_congif.train_data_parth,
                    self.ingestion_congif.test_data_parth)
            
            
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__ == "__main__":
    obj = DataIngestionConfig()
    obj.initiate_data_ingestion()
    