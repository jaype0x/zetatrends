import setuptools


setuptools.setup(
    name="zetatrends",
    version="0.0.1",
    url="https://github.com/jaype0x/zetatrends",

    author="JAY SPARK",
    author_email="cozeetaa.io@gmail.com",

    description="Python package to plot tickers trends with charts like renko, line break, pnf etc and ZETA X will add more stuff",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
