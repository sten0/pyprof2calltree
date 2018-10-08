from setuptools import setup

version = '1.4.3'

setup(
    name='pyprof2calltree',
    version=version,
    description="Help visualize profiling data from cProfile with kcachegrind and qcachegrind",
    long_description=open('README.rst').read(),
    keywords='profiler visualization programming tool kde kcachegrind qcachegrind',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: X11 Applications :: KDE",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Desktop Environment :: K Desktop Environment (KDE)",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: System :: System Shells",
        "Topic :: Utilities",
    ],
    author='Olivier Grisel',
    author_email='olivier.grisel@ensta.org',
    maintainer='Peter Waller',
    maintainer_email='p@pwaller.net',
    url='https://github.com/pwaller/pyprof2calltree/',
    license='MIT',
    py_modules = ['pyprof2calltree'],
    zip_safe=True,
    test_suite='test',
    entry_points = {
        'setuptools.installation': [
            'eggsecutable = pyprof2calltree:main',
        ],
        'console_scripts': [
            'pyprof2calltree = pyprof2calltree:main',
        ],
    }
)
