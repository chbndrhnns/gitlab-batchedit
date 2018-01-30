from setuptools import setup, find_packages

setup(name='gitlab-batchedit',
      version='0.1',
      description='Some batch edit tools using python-gitlab',
      url='https://github.com/chbndrhnns/gitlab-batchedit',
      author='Johannes Rueschel',
      author_email='n@rueschel.de',
      license='MIT',
      entry_points = {
        'console_scripts': ['gitlab-batchedit=gitlabbatchedit.issues:main'],
      },
      packages=find_packages(),
      zip_safe=False)