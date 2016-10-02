try:
    from setuptools import setup
except:
    from distutils import setup


setup(
    name='Amity',
    version='1.0.0',
    description='Room Allocation System',
    url='https://github.com/andela-kndegwa/CP1',
    author='Kimani Ndegwa',
    author_email='kimani.ndegwa@andela.com',
    packages=['Amity'],
    entry_points={
            'console_scripts': [
                'my_project = my_project.__main__:main'
            ]
    },




)
