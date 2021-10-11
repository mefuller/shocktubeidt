from setuptools import setup

setup(
    name='ShockTubeIDT',
    version='0.1.0',
    description='Shock tube ignition delay time calculator utilizing Cantera',
    url='https://gitlab.com/mefuller/shocktubeidt',
    author='Mark E. Fuller',
    author_email='fuller@stossrohr.net',
    license='Apache-2.0',
    packages=['ShockTubeIDT'],
    install_requires=['cantera>=2.4.0',
                      'matplotlib',
                      'numpy',
                      'pandas',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
