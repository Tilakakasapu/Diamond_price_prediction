import os
from src.DiamondPricePrediction import logger
from src.DiamondPricePrediction.entity.config_entity import ModelTraining
import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from src.DiamondPricePrediction.utils.common import evaluate_model
import joblib
class Model_Training:
    def __init__(self,config: ModelTraining):
        self.config = config
    def train_model(self):
        df=pd.read_csv(self.config.train_data)
        df1= pd.read_csv(self.config.test_data)
        x_train = df.drop(['price'],axis=1)
        y_train = df[['price']]
        X_test = df1.drop(['price'],axis=1)
        y_test = df1[['price']]
        models={'LinearRegression':LinearRegression(),'Lasso':Lasso(),'Ridge':Ridge(),'Elasticnet':ElasticNet()}
        trained_model_list=[]
        model_list=[]
        r2_list=[]
        for i in range(len(list(models))):
            model=list(models.values())[i]
            model.fit(x_train,y_train)
            y_pred=model.predict(X_test)
            mae, rmse, r2_square=evaluate_model(y_test,y_pred)
            print(list(models.keys())[i])
            logger.info(list(models.keys())[i])
            model_list.append(list(models.keys())[i])
            logger.info('Model Training Performance')
            logger.info("RMSE:",rmse)
            logger.info("MAE:",mae)
            logger.info("R2 score",r2_square*100)
            r2_list.append(r2_square)
            logger.info('='*35)
            logger.info('\n')
        for i in range(len(r2_list)):
            if max(r2_list) == r2_list[i]:
                joblib.dump(model_list[i],os.path.join(self.config.root_dir,str(model_list[i])))
