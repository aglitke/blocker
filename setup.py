from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='blocker',
      version='0.1',
      description='Volume provisioning in Ansible with a cinder-like frontend',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Hardware :: Hardware Drivers',
      ],
      keywords='cinder ansible block storage drivers',
      url='https://github.com/aglitke/blocker',
      author='Adam Litke',
      author_email='alitke@redhat.com',
      license='GPLV2+',
      packages=['blocker'],
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={ },
      include_package_data=True,
      zip_safe=False)

