
from setuptools import setup

setup(name="redditwallpapers",
      version="1.7",
      description="Automatically sets the top trending, good resolution images on reddit as your wallpaper.",
      url="https://github.com/yask123/redditwallpapers",
      author="Yask Srivastava",
      author_email="yask123@gmail.com",
      license='MIT',
      packages=["redditwallpapers"],
      install_requires=[
  	  'pillow',
          'requests',
          'praw'
      ],
      scripts=["bin/redditwallpapers"],
      zip_safe=False)
