import pandas as pd

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

print(canadian_youtube.head(5))
print(canadian_youtube.info() , british_youtube.info())
print(canadian_youtube.shape, british_youtube.shape)

concat_data0= pd.concat([canadian_youtube, british_youtube], axis=0)
print(canadian_youtube.shape, british_youtube.shape, concat_data0.shape)

concat_data1= pd.concat([canadian_youtube, british_youtube], axis=1)
print(canadian_youtube.shape, british_youtube.shape, concat_data1.shape)

join_data = canadian_youtube.join(british_youtube)

canadian_youtube = pd.read_csv("CAvideos.csv").reset_index()
british_youtube = pd.read_csv("GBvideos.csv").reset_index()

print(canadian_youtube.info(), british_youtube.info())
print(canadian_youtube.head(5), british_youtube.head(5))

join_data = canadian_youtube.join(british_youtube)

join_data = canadian_youtube.join(british_youtube, lsuffix='_CAN', rsuffix='_UK')
print(join_data.info())
print(concat_data1.shape,join_data.shape)


left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
print(left.shape, right.shape)
print(left.info(), right.info())

join_datalr = left.join(right, lsuffix='_CAN', rsuffix='_UK')
print(join_datalr.info())
print(join_datalr.head(5))

merged_data= pd.merge(left,right,on='video_id')
print(left.shape, right.shape, merged_data.shape)
print(join_data.shape, merged_data.shape)



#==================================================================
merged_data= pd.merge(left, right[['video_id','views','likes','dislikes']], on='video_id', how='left/right/outer')

#==================================================================


import pandas as pd






import requests
req1=requests.get('http://api.open-notify.org/iss-now.json')
print(req1.text)
req2=requests.get('http://api.open-notify.org/astros.json')
print(req2.text)
data=req2.json()
print(data['number'])
for p in data['people']:  print(p['name'])








import pandas as pd
Data = pd.read_csv(r"C:\Users\Bahman Honari\PycharmProjects\UCDMarketing\telco.csv")
print(Data)

from sklearn.svm import SVC
svm = SVC()
features = ['tenure','MonthlyCharges','TotalCharges']
X=Data[features]
y=Data['Churn']
svc.fit(Data[features], Data['Churn'])