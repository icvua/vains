# -*- coding: utf-8 -*-

name = 'jaehyukLee'
version = '1.0.1'
authors = ['Jaehyuk Lee']
requires = [
    'python',
]
variants = [
    ['platform-linux', 'python'],
]


def commands():
    env.PYTHONPATH.prepend("{root}/python")


format_version = 2
