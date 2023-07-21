import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import TweedieRegressor

from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
print("\n ********************     Question 2    ******************* ")

print("\n ********************     surviving  patients:    ******************* ")

# Surviving patients
survived = df[df['DEATH_EVENT'] == 0]
X = survived['serum_sodium'].values.reshape(-1, 1)
Y = survived['serum_creatinine'].values.reshape(-1, 1)

# Split into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

# Linear model
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)
Y_pred_lin = lin_reg.predict(X_test)

# Quadratic model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)
Y_pred_quad = lin_reg_2.predict(poly_reg.fit_transform(X_test))
# Cubic spline model

spline_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
spline_model.fit(X_train, Y_train)
Y_pred_spline = spline_model.predict(X_test)
# GLM model
glm = make_pipeline(PolynomialFeatures(1), LinearRegression())
glm.fit(np.log(X_train), Y_train)
Y_pred_glm = glm.predict(np.log(X_test))
# GLM with log(y) = a log(x) + b
glm2 = TweedieRegressor(power=0, alpha=0, link='log')
Y_train = Y_train.ravel()
glm2.fit(X_train, np.log(Y_train))
Y_pred_glm2 = np.exp(glm2.predict(X_test))






# Print the weights
print('*********** The weights ***********')
print('Linear model: a =', lin_reg.coef_[0][0], ', b =', lin_reg.intercept_[0])
print('Quadratic model: a =', lin_reg_2.coef_[0][1], ', b =', lin_reg_2.coef_[0][2], ', c =', lin_reg_2.intercept_[0])
print('Cubic spline model: a =', spline_model.named_steps['linearregression'].coef_[0][3], ', b =', spline_model.named_steps['linearregression'].coef_[0][2], ', c =', spline_model.named_steps['linearregression'].coef_[0][1], ', d =', spline_model.named_steps['linearregression'].intercept_[0])
print('GLM with y = a log(x) + b: a  =', glm.named_steps['linearregression'].coef_[0][0], ', b =', glm.named_steps['linearregression'].intercept_[0])
print('GLM with log(y) = a log(x) + b: a =', glm2.coef_[0], ', b =', glm2.intercept_)




# Plot the predicted and actual values
plt.scatter(X_test, Y_test, color='black')
plt.plot(X_test, Y_pred_lin, color='blue', linewidth=2)
plt.plot(X_test, Y_pred_quad, color='red', linewidth=2)
plt.plot(X_test, Y_pred_spline, color='green', linewidth=2)
plt.plot(X_test, Y_pred_glm, color='orange', linewidth=2)
plt.plot(X_test, Y_pred_glm2, color='purple', linewidth=2)
plt.title('Surviving patients')
plt.xlabel('Serum sodium')
plt.ylabel('Serum creatinine')
plt.show()

# Compute the SSE for each model
SSE_lin_0 = mean_squared_error(Y_test, Y_pred_lin) * len(Y_test)
SSE_quad_0 = mean_squared_error(Y_test, Y_pred_quad) * len(Y_test)
SSE_spline_0 = mean_squared_error(Y_test, Y_pred_spline) * len(Y_test)
SSE_glm_0 = mean_squared_error(Y_test, Y_pred_glm) * len(Y_test)
SSE_glm2_0 = mean_squared_error(Y_test, Y_pred_glm2) * len(Y_test)


print('\n *********** The SSE ***********')
print('Linear model SSE:', SSE_lin_0)
print('Quadratic model SSE:', SSE_quad_0)
print('Cubic spline model SSE:', SSE_spline_0)
print('GLM with y = a log(x) + b model SSE:', SSE_glm_0)
print('GLM with log(y) = a log(x) + b SSE:', SSE_glm2_0)
print("\n ********************     deceased patients:    ******************* ")
# Deceased patients
deceased = df[df['DEATH_EVENT'] == 1]
X = deceased['serum_sodium'].values.reshape(-1, 1)
Y = deceased['serum_creatinine'].values.reshape(-1, 1)

# Split into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

# Linear model
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)
Y_pred_lin = lin_reg.predict(X_test)

# Quadratic model
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, Y_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)
Y_pred_quad = lin_reg_2.predict(poly_reg.fit_transform(X_test))

# Fit cubic spline model
spline_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
spline_model.fit(X_train, Y_train)
Y_pred_spline = spline_model.predict(X_test)

# Fit generalized linear model
glm_model = make_pipeline(PolynomialFeatures(1), LinearRegression())
glm_model.fit(np.log(X_train), Y_train)
Y_pred_glm = glm_model.predict(np.log(X_test))

# Generalized linear model
glm2 = TweedieRegressor(power=0, alpha=0, link='log')
Y_train = Y_train.ravel()
glm2.fit(X_train, np.log(Y_train))
Y_pred_glm2 = np.exp(glm2.predict(X_test))

# Print the weights
print(' *********** The weights ***********')
print('Linear model: a =', lin_reg.coef_[0][0], ', b =', lin_reg.intercept_[0])
print('Quadratic model: a =', lin_reg_2.coef_[0][1], ', b =', lin_reg_2.coef_[0][2], ', c =', lin_reg_2.intercept_[0])
print('Cubic spline model: a =', spline_model.named_steps['linearregression'].coef_[0][3], ', b =', spline_model.named_steps['linearregression'].coef_[0][2], ', c =', spline_model.named_steps['linearregression'].coef_[0][1], ', d =', spline_model.named_steps['linearregression'].intercept_[0])
print('GLM with y = a log(x) + b: a  =', glm.named_steps['linearregression'].coef_[0][0], ', b =', glm.named_steps['linearregression'].intercept_[0])
print('GLM with log(y) = a log(x) + b: a =', glm2.coef_[0], ', b =', glm2.intercept_)



# Plot the predicted and actual values
plt.scatter(X_test, Y_test, color='black')
plt.plot(X_test, Y_pred_lin, color='blue', linewidth=2)
plt.plot(X_test, Y_pred_quad, color='red', linewidth=2)
plt.plot(X_test, Y_pred_spline, color='green', linewidth=2)
plt.plot(X_test, Y_pred_glm, color='orange', linewidth=2)
plt.plot(X_test, Y_pred_glm2, color='purple', linewidth=2)

plt.title('Deceased patients')
plt.xlabel('Serum sodium')
plt.ylabel('Serum creatinine')
plt.show()

# Compute the SSE for each model
SSE_lin_1 = mean_squared_error(Y_test, Y_pred_lin) * len(Y_test)
SSE_quad_1 = mean_squared_error(Y_test, Y_pred_quad) * len(Y_test)
SSE_spline_1 = mean_squared_error(Y_test, Y_pred_spline) * len(Y_test)
SSE_glm_1 = mean_squared_error(Y_test, Y_pred_glm) * len(Y_test)
SSE_glm2_1 = mean_squared_error(Y_test, Y_pred_glm2) * len(Y_test)
print('\n *********** The SSE ***********')
print('Linear model SSE:', SSE_lin_1)
print('Quadratic model SSE:', SSE_quad_1)
print('Cubic spline model SSE:', SSE_spline_1)
print('GLM with y = a log(x) + b model SSE:', SSE_glm_1)
print('GLM with log(y) = a log(x) + b SSE:', SSE_glm2_1)


print("\n ********************     Question 3.1    ******************* ")

# create a dictionary to store the SSE values for each model
data = {
    'Model': ['y = ax + b', 'y = ax^2 + bx + c', 'y = ax^3 + bx^2 + cx + d', 'y = a log(x) + b', 'log(y) = a log(x) + b'],
    'SSE (death event=0)': [SSE_lin_0, SSE_quad_0, SSE_spline_0, SSE_glm_0, SSE_glm2_0],
    'SSE (death event=1)': [SSE_lin_1, SSE_quad_1, SSE_spline_1, SSE_glm_1, SSE_glm2_1]
}

# create a pandas dataframe from the dictionary
df = pd.DataFrame(data)

# display the dataframe
print(df)
print("\n ********************     Question 3.2    ******************* ")
print(" The smallest SSE: for surviving patients is log(y) = a log(x) + b, for deceased patients is y = a log(x) + b")
print(" The largest SSE: for surviving patients is y = ax^3 + bx^2 + cx + d , for deceased patients is y = ax^3 + bx^2 + cx + d   ")


