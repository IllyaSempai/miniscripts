import os
import requests

absFilePath = os.path.abspath(__file__)
os.chdir( os.path.dirname(absFilePath) )
filesep = "\\" if os.name == "nt" else "/"
if not os.path.isdir("files") or not os.path.isfile(f"files{filesep}imgs.txt"):
    print(
        'the "files" directory was not found or is incomplete, please move this file to the correct directory or run "hentaimini.py" again'
    )
    quit()
try:
    os.mkdir(os.path.join(os.path.dirname(absFilePath), "imgs"))
except OSError as error:
    print(error)
    path = os.path.join(os.path.dirname(absFilePath), "imgs")
    print(
        f'if the "{path}" directory already exists in this path please remove it or move the file'
    )
    quit()
with open(f"files{filesep}imgs.txt", "rt", encoding="utf-8") as f:
    content = f.readlines()
os.chdir(os.path.dirname(absFilePath) + filesep + "imgs")
indx = 0
for x in content:
    if str(x) == "0":
        continue
    if os.name != "nt":
        os.system(f"wget {x}")
    else:
        with open(f"pic{indx}.jpg", "wb") as handle:
            response = requests.get(x, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        indx += 1
