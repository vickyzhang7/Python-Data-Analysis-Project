import pandas as pd
print("\n ********************     Question 1.1    ******************* ")

# Load the data into a pandas dataframe
data = pd.read_csv('data_banknote_authentication.txt', header=None)

# Add a "color" column based on the class label
data['color'] = ['green' if c == 0 else 'red' for c in data[4]]
print("\n Because it is a very large output so we only prints the first 5 rows of the data to verify")
print(data.head())
print("\n ********************     Question 1.2    ******************* ")

# Compute the mean and standard deviation for each feature and class
class0_mean = data[data[4] == 0].iloc[:,0:4].mean().round(2)
class0_std = data[data[4] == 0].iloc[:,0:4].std().round(2)
class1_mean = data[data[4] == 1].iloc[:,0:4].mean().round(2)
class1_std = data[data[4] == 1].iloc[:,0:4].std().round(2)
all_mean = data.iloc[:,0:4].mean().round(2)
all_std = data.iloc[:,0:4].std().round(2)

# Create a dataframe to summarize the mean and standard deviation
summary = pd.DataFrame({'µ(f1)': [class0_mean[0], class1_mean[0], all_mean[0]],
                        'σ(f1)': [class0_std[0], class1_std[0], all_std[0]],
                        'µ(f2)': [class0_mean[1], class1_mean[1], all_mean[1]],
                        'σ(f2)': [class0_std[1], class1_std[1], all_std[1]],
                        'µ(f3)': [class0_mean[2], class1_mean[2], all_mean[2]],
                        'σ(f3)': [class0_std[2], class1_std[2], all_std[2]],
                        'µ(f4)': [class0_mean[3], class1_mean[3], all_mean[3]],
                        'σ(f4)': [class0_std[3], class1_std[3], all_std[3]]},
                       index=['class 0', 'class 1', 'all'])

print(summary)
print("\n ********************     Question 1.3    ******************* ")
print("\n1.The mean of feature f1 is higher in class 0 than in class 1, and the standard deviation is also larger. "
      "\n  This may suggest that counterfeit banknotes exhibit greater variability in image variance than genuine banknotes, which may be more consistent."
      "\n2.The mean of feature f2 is higher in class 1 than in class 0, and the standard deviation is also larger. "
      "\n  This may suggest that there are more pixels with right-skewed distribution in the images of counterfeit banknotes, "
      "\n  whereas the images of genuine banknotes exhibit more left-skewed distribution."
      "\n3.The mean of feature f3 is higher in class 1 than in class 0, and the standard deviation is also larger. "
      "\n  This may suggest that the images of counterfeit banknotes exhibit greater variability in curvature, "
      "\n  whereas the images of genuine banknotes exhibit more consistent curvature."
      "\n4.The mean of feature f4 is lower in class 1 than in class 0, and the standard deviation is also smaller. "
      "\n  This may suggest that there are fewer pixels in the images of counterfeit banknotes, whereas there are more pixels in the images of genuine banknotes.")