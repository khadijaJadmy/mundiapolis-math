#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
width = 0.5
fig, ax = plt.subplots()
labels = ['Farrah', 'Fred', 'Felicia']

app_means = fruit[0]
bana_means = fruit[1]
oran_means = fruit[2]
pea_means = fruit[3]
bar_padding1 = np.add(app_means, bana_means).tolist()
bar_padding2 = np.add(bar_padding1, oran_means).tolist()


ax.bar(labels, app_means, width,  label='apples', color='r')
ax.bar(labels, bana_means, width,  bottom=app_means,
       label='bananas', color='yellow')
ax.bar(labels, oran_means, width,  bottom=bar_padding1,
       label='oranges', color='#ff8000')
ax.bar(labels, pea_means, width,  bottom=bar_padding2,
       label='peaches', color='#ffe5b4')

ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.legend()
ax.set_yticks(np.arange(0, 90, 10))
plt.show()
