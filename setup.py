from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'Yogaraajan N E',
    author_email= 'yogaraajan.ne@gmail.com',
    packages= find_packages(),
    install_requires = []

)

#find_package() look for __init__.py file and make that folder as local package