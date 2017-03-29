from setuptools import setup, find_packages


setup(name='DeepHelper',
        version='0.1alpha',
        description='Python Utilites for easy telegram notification and save files to dropbox',
        author='Antonov Dmitri',
        packages=find_packages(),
        install_requires=[
                    "PyTelegramBotAPI",
                    "dropbox"
                        ])
