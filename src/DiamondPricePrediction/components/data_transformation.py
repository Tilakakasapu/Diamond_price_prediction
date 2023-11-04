import os
from src.DiamondPricePrediction import logger
from sklearn.model_selection import train_test_split
from src.DiamondPricePrediction.config.configuration import DataTransformationConfig
import pandas as pd
from sklearn.impute import  SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.pipeline import  Pipeline
from sklearn.compose import ColumnTransformer
class Data_Transformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        data.drop(['id'],axis=1,inplace=True)
        x = data.drop(['price'],axis=1)
        y = data[['price']]
        categorical_cols = x.select_dtypes(include='object').columns
        numerical_cols = x.select_dtypes(exclude='object').columns
        cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
        color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
        clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
        num_pipeline = Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
        cat_pipeline = Pipeline(steps = [('imputer',SimpleImputer(strategy='most_frequent')),('OrdinalEncoder', OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),('scaler',StandardScaler())])
        preprocessor = ColumnTransformer([('num_pipeline',num_pipeline,numerical_cols),('cat_pipeline',cat_pipeline,categorical_cols)]) 
        x = pd.DataFrame(preprocessor.fit_transform(x),columns=preprocessor.get_feature_names_out())    
        X_train, X_test, y_train, y_test = train_test_split(x, y)
        train = pd.concat([X_train,y_train],axis=1)
        test=pd.concat([X_test,y_test],axis=1)
        train.reset_index(drop=True,inplace=True)
        test.reset_index(drop=True,inplace=True)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        logger.info("splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        print(train.shape)
        print(test.shape)