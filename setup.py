from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['audio','core','entertainment','motion',
              'network','social','vision','apiai_service','utils'],
    package_dir={'': 'src'}
)

setup(**d)
