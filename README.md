# https://discord.gg/DQsvSdR9kb
Russian HVH Cheat 1.8x-1.16.5
Fuck vega33 and djuniks  

# auto:  
- download the installer from -> https://raw.githubusercontent.com/jntdevelopment/vegaline/refs/heads/main/vlinstaller_0.1.1_x64-setup.exe
- ignore the shitty ui and use it 😭
- if auto downloading has failed use the local files option

# manual:  
- download archives from -> https://mega.nz/folder/joQijDjR#IRe06GayBsWmakp8_FALTg  
- unzip `gamepath`, paste into `%localappdata%` (should be `%localappdata%/gamepath`)  
- unzip `VEGA.NCO`, paste into `%appdata%` (should be `%appdata%/VEGA.NCO`)  
- launch via `run_client.bat` from `VEGA.NCO` folder  
  
![image](https://github.com/jntdevelopment/vegaline/blob/main/fun.gif?raw=true)

## if you wanna crack it yourself -> some info and the needed files are below

**decrypted build 93** -> https://mega.nz/file/S9ohnZbb#usQiGdh7nx4zUhOB3SS3vX0tf8l6iAQvlSsw97cQ_44  
**decrypted build 92** -> https://mega.nz/folder/3xonwCbQ#nRnVKrVFFNjTzwf-0wAOMw  
**encrypted build 92** -> https://mega.nz/file/HxRnHZ7A#lX2ceuJTj8zSbTrs67w53BxRDDOAUlNmABylNNRlVhg  
  
- **Auth and logging patching:** look at the info section for the classes location and patch them  

## Info:  
`vRes0.iso` (not encrypted) - minecraft and some client assets (jar)  
`vRes1.iso` (xored) - javax and client assets for the client (jar)  
`vRes2.iso` (encrypted) - main client (jar)  

`optifine/ResPipelineHandler` -> gist authorization class  
`optifine/SpriteTexturePipelined` -> discord logging class  
`ru/govno/client/utils/Managers/FOFO` -> discord logging helper class  


## Decrypting the client jars:  
- Download both `vres1decrypt.py` and `vres2decrypt.py`  
- `python vres1decrypt.py` (works on all builds of the client)  
- `python vres2decrypt.py` (keys change each build, latest works for build 92)  

## Updating the keys for decryption:  
- Look at `https://gist.github.com/DICKAFOTON/23aaeb6012dc7365c9bac85aa0f9036b`  
- If the gist is down -> grab the key you need from `KeyValue2_dumpgist.txt`  
- Put the raw contents into `KeyValue2.json`  
- Use the installer, go to `%appdata%\Roaming\VEGA.NCO`, copy the `data.bin`  
- Put both `KeyValue2.json` and `data.bin` into folder named `boiler`  
- From the root of that folder use `python update_meta.py` and replace the values you've got from the script in the `vres2decrypt.py`  
