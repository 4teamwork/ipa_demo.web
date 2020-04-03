from setuptools import find_packages
from setuptools import setup


extras_require = {
    'tests': [
        'Products.DateRecurringIndex',
        'ftw.builder',
        'ftw.testbrowser',
        'ftw.testing',
        'isort',
        'pep8',
        'plone.app.testing',
    ],
}

setup(name='ipa_demo.web',
      version='1.0.0.dev0',
      author='4teamwork AG',
      url='https://github.com/4teamwork/ipa_demo.web',
      description="Package for the ipa_demo.",
      long_description=open("README.rst").read(),
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ipa_demo'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'collective.editmodeswitcher',
          'collective.quickupload',
          'ftw.chameleon',
          'ftw.file',
          'ftw.footer',
          'ftw.inflator [dexterity]',
          'ftw.lawgiver',
          'ftw.simplelayout [contenttypes, mapblock, plone4]',
          'ftw.upgrade',
          'plone.app.caching',
          'plonetheme.blueberry',
          'requests',
          'setuptools',
      ],

      tests_require=extras_require['tests'],
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
