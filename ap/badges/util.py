""" BADGES util.py 
Utility functions for badges module
"""

from PIL import Image

def _image_upload_path(instance, filename):
  # To customise the path which the image saves to.
  return instance.get_upload_path(filename)

def resize_image(originimage, size=(120,100)):
  image = Image.open(originimage.path)
  final_path = str(originimage.path) + ".avatar"
  image.resize(size, Image.ANTIALIAS).save(final_path, 'JPEG', quality=100)
