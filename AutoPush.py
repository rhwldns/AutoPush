from os import popen

popen("git add .")
popen('git commit -m "feat: some functions"')
popen("git push")
