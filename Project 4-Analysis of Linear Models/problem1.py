import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data into pandas dataframe
df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# extract two dataframes based on DEATH EVENT
df_0 = df[df['DEATH_EVENT'] == 0][['creatinine_phosphokinase', 'serum_creatinine', 'serum_sodium','platelets']]
df_1 = df[df['DEATH_EVENT'] == 1][['creatinine_phosphokinase', 'serum_creatinine', 'serum_sodium','platelets']]
# construct correlation matrix for df_0
print("\n ********************     Question 1.1    ******************* ")
print("plot correlation matrix for df_0")
corr_0 = df_0.corr()
sns.set(font_scale=1.2)
sns.heatmap(corr_0, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix for Surviving Patients')
plt.savefig('corr_matrix_0.png', dpi=300)
plt.show()

# construct correlation matrix for df_1
print("\n ********************     Question 1.2    ******************* ")
print("plot correlation matrix for df_1")
corr_1 = df_1.corr()
sns.set(font_scale=1.2)
sns.heatmap(corr_1, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix for Deceased Patients')
plt.savefig('corr_matrix_1.png', dpi=300)
plt.show()

# Examine correlation matrix plots and answer questions

print("\n ********************     Question 1.3    ******************* ")
print(" (a) The features with the highest correlation for surviving patients (df_0) are age and ejection fraction."
      "\n (b) The features with the lowest correlation for surviving patients (df_0) are serum creatinine and serum sodium."
      "\n (c) The features with the highest correlation for deceased patients (df_1) are serum creatinine and age."
      "\n (d) The features with the lowest correlation for deceased patients (df_1) are serum sodium and ejection fraction."
      "\n (e) The results are not the same for both cases. There are differences in the highest and lowest correlated features between the two datasets.")
