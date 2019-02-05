from setuptools import setup

def readme():
   with open('README.md') as f:
       return f.read()

def license():
   with open('LICENSE') as f:
      return f.read()

setup(name='PassGen',
   version='1.0',
   description='Generate password',
   long_description=readme(),
   url='https://github.com/Natthapolmnc/PasswordGenerator.git',
   author='Fame',
   author_email='natthapolmnc@outlook.com',
   license=license(),
   keywords='PassGen',
   packages=['PassGen'],
   package_dir={'PassGen': 'src/PassGen'},
   package_data={'PassGen' :['CeasarCipher/*.py'] 
},
   
)