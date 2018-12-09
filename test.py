import pandas as pd
from tensorflow import keras
from feature_extraction import manager

cols = ['ID', 'TITLE', 'TEXT', 'LABEL']
data = pd.read_csv('fake_or_real_news.csv', names=cols, header=0)

k = len(data[cols[3]]) // 2

x = list(zip(data[cols[1]], data[cols[2]]))
y = data[cols[3]]

dim = 5

x_train, y_train = manager.flat_input(x[:k], y[:k], dim)
x_validate, y_validate = manager.flat_input(x[k:], y[k:], dim)

model = keras.Sequential()
model.add(keras.layers.Dense(units=500, activation='relu', input_dim=dim**2))
model.add(keras.layers.Dense(units=200, activation='relu'))
model.add(keras.layers.Dense(units=50, activation='relu'))
model.add(keras.layers.Dense(units=2, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=32)

model.evaluate(x_validate, y_validate, batch_size=32)

result = model.predict(x_validate, batch_size=32).tolist()

manager.calculate_metrics(result, y_validate.tolist())