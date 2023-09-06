from setuptools import setup

setup(name='custom_gym',
      version='0.0.1',
      install_requires=['gymnasium', 
			'shimmy',
			'imageio',
			'mujoco']  # And any other dependencies pepper env needs
)
