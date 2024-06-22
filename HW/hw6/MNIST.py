# 使用chatGPT生成

import numpy as np
import gzip
from urllib.request import urlretrieve
from pathlib import Path
from micrograd.engine import Value, cross_entropy_loss
from micrograd.nn import MLP

# Download MNIST dataset
def fetch(url, path):
    if not Path(path).exists():
        urlretrieve(url, path)

def load_mnist_images(path):
    with gzip.open(path, 'r') as f:
        f.read(16)
        buffer = f.read()
        data = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)
        return data.reshape(-1, 28 * 28) / 255.0

def load_mnist_labels(path):
    with gzip.open(path, 'r') as f:
        f.read(8)
        buffer = f.read()
        labels = np.frombuffer(buffer, dtype=np.uint8)
        return labels

fetch('http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz', 'train-images-idx3-ubyte.gz')
fetch('http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz', 'train-labels-idx1-ubyte.gz')

X_train = load_mnist_images('train-images-idx3-ubyte.gz')
y_train = load_mnist_labels('train-labels-idx1-ubyte.gz')

# Create neural network
model = MLP(784, [128, 64, 10])

# Training
learning_rate = 0.01
for epoch in range(1, 11):
    total_loss = 0
    for i in range(len(X_train)):
        x = [Value(val) for val in X_train[i]]
        logits = model(x)
        label = [0] * 10
        label[y_train[i]] = 1
        label = [Value(val) for val in label]

        loss = cross_entropy_loss(logits, label)
        total_loss += loss.data

        model.zero_grad()
        loss.backward()

        for p in model.parameters():
            p.data -= learning_rate * p.grad

    print(f'Epoch {epoch}, Loss: {total_loss / len(X_train)}')
