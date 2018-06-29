
import re
import glob
import os

pics = glob.glob('*.jpg')

for name in pics:
  stripped = name.split('/')[-1].split('.')[0].split('_')[0]
  nameList = re.sub("([a-z])([A-Z])","\g<1> \g<2>", stripped).split(' ')

  nameList.reverse()

  nameList = ''.join(nameList)

  print(nameList)

  command_tokens = [
    'mv',
    name,
    nameList+'.jpg'
  ]

  command = ' '.join(command_tokens)

  os.system(command)

