# -*- coding: utf-8 -*-
"""neural_nets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BMbo1BLvpkwP1ufcNsaoNH97tCw9RwF1
"""

from keras.datasets import mnist

(xtr, ytr),(xte,yte) = mnist.load_data() # training, testing

xtr.shape  # each image has 28X28

from matplotlib import pyplot as plt

plt.imshow(xtr[0],cmap='gray')

ytr[0]

plt.imshow(xtr[99],cmap='gray')

ytr[99]

xte.shape

# lets start
from keras.utils.np_utils import to_categorical as tcg

ytr = tcg(ytr)

ytr[0]

yte = tcg(yte)

xtr[0]

xtr=xtr.reshape(xtr.shape[0], xtr.shape[1]*xtr.shape[2]) #simply 28*28

xtr.shape

xtr #converted to single array

#divide every number by 255 to get every number in same state or number of digits!-->Standardisation
#but first convert to float
xtr = xtr.astype('float32')/255

xtr[0]

#convert xte too... processs all together!i
xte=xte.reshape(xte.shape[0],-1).astype('float32')/255

xte[0]

from keras.models import Sequential
from keras.layers import Dense

#create neural network :)
model = Sequential()
model.add(Dense(input_dim=784,units=784,activation='relu')) #add layerinput layer contains no. of features
model.add(Dense(512,activation='relu')) #relu rectified linear...activation function
model.add(Dense(10,activation='softmax')) #softmax fun gives output frm 0-1
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']) #gradient types! explore vanila type
model.fit(xtr,ytr,validation_data=(xte,yte),epochs=10,batch_size=256)

