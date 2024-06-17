import setuptools 

  

with open("README.md", "r") as fh: 

    description = fh.read() 

  
setuptools.setup( 

    name="encryptools", 

    version="1.2.0", 

    author="Dione Alfarisi", 

    author_email="ardionefarisi1322@gmail.com", 

    packages=["encryptools"], 

    description="Encrypt and Decrypt file python", 

    long_description=description, 

    long_description_content_type="text/markdown", 

    url="https://github.com/dioneal-farisi/encryptools", 

    license='MIT', 

    python_requires='>=3.8', 

    install_requires=['pycrytodome'] 
) 