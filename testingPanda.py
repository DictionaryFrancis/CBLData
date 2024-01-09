import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['OPPONENT SHOT', 'OUR SHOT'],
        'Value': [13, 25]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting the data
ax = df.plot(kind='bar', x='Category', y='Value', legend=False, color=['red', 'blue'])

# Adding labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Comparison of OPPONENT SHOT and OUR SHOT')

# Display the plot
plt.show()
