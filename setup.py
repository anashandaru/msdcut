from setuptools import setup

setup(
    name='cut',
    version='0.1.0',
    py_modules=['cut'],
    install_requires=[
        'Click',
        'obspy',
    ],
    entry_points={
        'console_scripts': [
            'cut = cut:main',
        ],
    },
)