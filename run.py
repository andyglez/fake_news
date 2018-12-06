import pandas as pd
from feature_extraction import manager

cols = ['ID', 'TITLE', 'TEXT', 'LABEL']
data = pd.read_csv("fake_or_real_news.csv", names=cols, header=0)
news = manager.manage(data, cols[1:len(cols)-1])

for n in news:
    print(n)
