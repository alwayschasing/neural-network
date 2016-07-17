#!/usr/bin/env python
# coding=utf-8
"""
This ia a CNN network complete with Tensorflow
"""
###Libraries
#Standard library
import cPickle
import gzip
#Third-party Libraries
import numpy as np
import tensorflow as tf

def load_data(filename="./data/mnist.pkl.gz"):
    f = gzip.open(filename,'rb')
    training_data,validation_data,test_data = cPickle.load(f)
    f.close()

#place holder for the input x and output y
x = tf.placeholder("float",shape=[None,784])
y = tf.placeholder("float",shape=[None,10])

class Network(object):

    def __init__(self,layers,mini_batch_size):
        """
        The network include some layers that we defined
        """
        self.layers = layers
        self.mini_batch_size = mini_batch_size
        self.params = [param for layer in self.layers for param in layer.params]
        self.x = tf.placeholder()


