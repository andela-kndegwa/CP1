try:
    from setuptools import setup
except:
    from distutils import setup


dependencies = []
file = open('requirements.txt', 'r')
for dep in file.readlines():
    dependencies.append(dep)

setup(
    name='Amity',
    version='1.0.0',
    description='Room Allocation System',
    url='https://github.com/andela-kndegwa/CP1',
    author='Kimani Ndegwa',
    author_email='kimani.ndegwa@andela.com',
    install_requires=dependencies,
    packages=['Amity'],
    entry_points={
            'console_scripts': [
                'amity=Amity.ui:enter_amity'
            ]
    },
)
