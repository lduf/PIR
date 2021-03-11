from chefboost import Chefboost as chef
import pandas as pd

df = pd.read_csv("dataset/expanded")
decision=df.pop("Decision")

df.insert(22, "Decision", decision)
print(df.head())

config = {'algorithm': 'C4.5'}
#model = chef.fit(df, config = config)
#chef.Gain(df, config = config)

imp=chef.feature_importance("outputs/rules/rules.py")
print(imp)