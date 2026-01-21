# https://discord.gg/DQsvSdR9kb
Russian HVH Cheat 1.8x-1.16.5

Libs and the client jars (encrypted) for build 92 -> https://mega.nz/file/HxRnHZ7A#lX2ceuJTj8zSbTrs67w53BxRDDOAUlNmABylNNRlVhg

vRes0.iso (not encrypted) - main assets for the client (jar)
vRes1.iso (xored) - javax and assets for the client (jar)
vRes2.iso (encrypted) - main client (jar)

To decrypt the client jars:
`python vres1decrypt.py` (works on all builds of the client)
`python vres2decrypt.py` (keys change each build, latest works for build 92)

To update the keys for vres2:
Look at `https://gist.github.com/DICKAFOTON/23aaeb6012dc7365c9bac85aa0f9036b`, put the raw contents into `KeyValue2.json` or grab the key you need from `KeyValue2_dumpgist.txt` (if the gist is down)
Use the installer, go to `%appdata%\Roaming\VEGA.NCO`, copy the `data.bin`
Put both `KeyValue2.json` and `data.bin` into folder named `boiler`, from the root of that folder use `python update_meta.py` and replace the values you've got in the `vres2decrypt.py`
