import os
import re
import sys
import time

from setuptools import find_packages, setup

setup(
    name="pyrequest",
    version="1.0",
    description="为 requests 的 response 添加 Selector 和 bs4.BeautifulSoup 功能，修复编码乱码问题",
    author="trent",
    author_email="fango6@qq.com",
    url="https://github.com/fango6/pyrequest",
    packages=find_packages(),

    install_requires=[
        'requests',
        'parsel',
        'bs4',
        'user-agent',
    ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
