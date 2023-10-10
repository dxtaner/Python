import matplotlib.pyplot as plt

# Data for the chart
activities = ['Work', 'Family', 'Homeworks',
              'Individual', 'Socializing', 'Spare Time', 'Sleep']
charles_data = [8.5, 0.5, 3.0, 1.0, 1.5, 3.0, 6.5]
henry_data = [9.5, 1.0, 2.0, 1.5, 0.5, 2.5, 7.0]
susan_data = [7.0, 1.5, 1.0, 2.5, 2.0, 2.0, 8.0]

# Plotting the unified bar chart
width = 0.2
x = range(len(activities))
plt.bar(x, charles_data, width=width, label='Charles')
plt.bar([i + width for i in x], henry_data, width=width, label='Henry')
plt.bar([i + 2 * width for i in x], susan_data, width=width, label='Susan')

# Customizing the chart
plt.xlabel('Area of Interest')
plt.ylabel('Time Spent (hours)')
plt.title('Time Spent on Daily Activities per Person')
plt.xticks([i + width for i in x], activities)
plt.legend()

# Display the chart
plt.tight_layout()
plt.show()
