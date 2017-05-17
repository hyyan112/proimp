# coding=utf-8
import random


class Edge(object):
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def to_json(self):
        return self.__dict__


class Module(object):
    def __init__(self, label, size):
        self.size = size + 10  # make cardinal number bigger to display
        self.label = label
        self.x = random.randint(-500, 1000)
        self.y = random.randint(-500, 1000)
        self.color = "#%06x" % random.randint(0, 0xFFFFFF)

    def accumulate(self, size=1):
        self.size += size

    def to_json(self):
        return self.__dict__
