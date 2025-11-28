

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


from google.colab import files


uploaded = files.upload()


insurance_dataset = pd.read_csv("insurance.csv")


insurance_dataset.head()


print("Shape:", insurance_dataset.shape)
insurance_dataset.info()


print(insurance_dataset.describe())


sns.set()
plt.figure(figsize=(6,6))
sns.histplot(insurance_dataset['age'], kde=True)
plt.title('Age Distribution')
plt.show()


plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=insurance_dataset)
plt.title('Sex Distribution')
plt.show()


plt.figure(figsize=(6,6))
sns.histplot(insurance_dataset['bmi'], kde=True)
plt.title('BMI Distribution')
plt.show()


plt.figure(figsize=(6,6))
sns.countplot(x='children', data=insurance_dataset)
plt.title('Children Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=insurance_dataset)
plt.title('Smoker Distribution')
plt.show()


plt.figure(figsize=(6,6))
sns.countplot(x='region', data=insurance_dataset)
plt.title('Region Distribution')
plt.show()


plt.figure(figsize=(6,6))
sns.histplot(insurance_dataset['charges'], kde=True)
plt.title('Charges Distribution')
plt.show()



insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)


X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)


regressor = LinearRegression()
regressor.fit(X_train, Y_train)


training_data_prediction = regressor.predict(X_train)
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared value (train):', r2_train)


test_data_prediction = regressor.predict(X_test)
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared value (test):', r2_test)


input_data = (31,1,25.74,0,1,0)

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


prediction = regressor.predict(input_data_reshaped)
print("The insurance cost is USD ", prediction[0])



age = int(input("Enter Age: "))
sex = input("Enter Sex (male/female): ").lower()
bmi = float(input("Enter BMI: "))
children = int(input("Enter Number of Children: "))
smoker = input("Smoker? (yes/no): ").lower()
region = input("Enter Region (southeast/southwest/northeast/northwest): ").lower()

sex = 0 if sex == 'male' else 1
smoker = 0 if smoker == 'yes' else 1
region_dict = {'southeast':0, 'southwest':1, 'northeast':2, 'northwest':3}
region = region_dict[region]


input_data = (age, sex, bmi, children, smoker, region)
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)


prediction = regressor.predict(input_data_as_numpy_array)
print("The insurance cost is USD", round(prediction[0], 2))