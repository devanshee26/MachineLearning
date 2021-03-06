# -*- coding: utf-8 -*-
"""cifar10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q8RvMnlbbm9fI5FGiHEqbvrY7pHRX1mK
"""

from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical as tcg #convert to one-hot-encoded vector

(xtr,ytr),(xte,yte) = cifar10.load_data() #tupple--(xtr,ytr)<--training(60000imgs) (xte,yte)<--test(10000imgs)

type(ytr)

xtr.shape

xte.shape #10,000 imgs,32X32 heightXwidth(matrix <-r0wXcols),color channels rgb

from matplotlib import pyplot as plt #to view image

plt.imshow(xtr[0]) # use this to see the image frog

xtr=xtr.reshape(xtr.shape[0],-1).astype('float32')/255
xte=xte.reshape(xte.shape[0],-1).astype('float32')/255
ytr=tcg(ytr)
yte=tcg(yte) #convert to categorical neural network

ytr[0] #every element represents an object of class!Text->Number<--LabelEncoding ..Each number shows obj like frog ,etc

from sklearn.preprocessing import LabelEncoder #convert text to numbers

#creating a neural network
model = Sequential()
model.add(Dense(input_dim=3072,units=3072,activation='relu'))#dense->adding layer,input dimension,here every pixel has 3features(rgb) 32X32X3,relu activatonn function o/p-(0-1)
model.add(Dense(1024,activation='relu'))
model.add(Dense(512,activation='relu'))
model.add(Dense(10,activation='softmax'))#last 3 are hidden layers
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])#epoch tells the number of tym machine should learn
model.fit(xtr,ytr,validation_data=(xte,yte),epochs=10,batch_size=256)

