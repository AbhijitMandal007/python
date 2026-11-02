import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'student': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'],
    'mathematics': [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    'physics': [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    'chemistry': [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    'english': [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)

print("Student Examination Data:")
print(df)

sns.set_style("whitegrid")

# Create one figure with 2 subplots
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)

sns.histplot(df['mathematics'], kde=True, label='Mathematics')
sns.histplot(df['physics'], kde=True, label='Physics')
sns.histplot(df['chemistry'], kde=True, label='Chemistry')
sns.histplot(df['english'], kde=True, label='English')

plt.title("Subject-Wise Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()

plt.subplot(1, 2, 2)

correlation = df[
    ['mathematics', 'physics', 'chemistry', 'english']
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")

# Adjust spacing
plt.tight_layout()

# Display figure
plt.show()