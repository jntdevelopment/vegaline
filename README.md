# https://discord.gg/DQsvSdR9kb
Russian HVH Cheat 1.8x-1.16.5
Fuck vega33 and djuniks

# full crack -> https://mega.nz/folder/joQijDjR#IRe06GayBsWmakp8_FALTg  
- unzip `gamepath`, paste into `%localappdata%` (should be `%localappdata%/gamepath`)  
- unzip `VEGA.NCO`, paste into `%appdata%` (should be `%appdata%/VEGA.NCO`)  
- launch via `run_client.bat` from `VEGA.NCO` folder  

# build 93 -> https://mega.nz/file/S9ohnZbb#usQiGdh7nx4zUhOB3SS3vX0tf8l6iAQvlSsw97cQ_44

# Decrypted client jars for build 92 -> https://mega.nz/folder/3xonwCbQ#nRnVKrVFFNjTzwf-0wAOMw
# Auth and logging patching: look at the info section for the classes location and patch them


Libs and the client jars (encrypted) for build 92 -> https://mega.nz/file/HxRnHZ7A#lX2ceuJTj8zSbTrs67w53BxRDDOAUlNmABylNNRlVhg  

## Info:  
`vRes0.iso` (not encrypted) - main assets for the client (jar)  
`vRes1.iso` (xored) - javax and assets for the client (jar)  
`vRes2.iso` (encrypted) - main client (jar)  

`optifine/ResPipelineHandler` -> gist authorization class  
`optifine/SpriteTexturePipelined` -> discord logging class  
`ru/govno/client/utils/Managers/FOFO` -> discord logging helper class  


## To decrypt the client jars:  
`python vres1decrypt.py` (works on all builds of the client)  
`python vres2decrypt.py` (keys change each build, latest works for build 92)  

## To update the keys for vres2:  
Look at `https://gist.github.com/DICKAFOTON/23aaeb6012dc7365c9bac85aa0f9036b`, put the raw contents into `KeyValue2.json` or grab the key you need from `KeyValue2_dumpgist.txt` (if the gist is down)  

Use the installer, go to `%appdata%\Roaming\VEGA.NCO`, copy the `data.bin`

Put both `KeyValue2.json` and `data.bin` into folder named `boiler`, from the root of that folder use `python update_meta.py` and replace the values you've got in the `vres2decrypt.py`  
