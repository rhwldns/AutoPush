from os import popen
from time import time

while True:
  time.sleep(60 * 5)
  popen("git add .")
  popen('git commit -m "feat: some functions ㅣ AutoPush"')
  popen("git push")
  print("Finished pushing to Github. ㅣ Made By 땅콩")
