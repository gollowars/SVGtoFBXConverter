# SVGtoFBXConverter
convert svg to fbx with blender


## required Blender

## setup
add .bash_profile

```
export BLENDER_SYSTEM_PYTHON=[YOUR_BLENDER_PATH]/blender.app/Contents/Resources/2.79/python
export BLENDER_SYSTEM_SCRIPTS=[YOUR_BLENDER_PATH]/blender.app/Contents/Resources/2.79/scripts
export BLENDER_SYSTEM_DATAFILES=[YOUR_BLENDER_PATH]/blender.app/Contents/Resources/2.79/datafiles
```

add .bashrc
```
alias blender='[YOUR_BLENDER_PATH]/blender.app/Contents/MacOS/blender'
```

rewrite convert.py
```
DIR_PATH = INPUT_SVGPATH
FILE_KIND = "*.svg"
OUTPUT_PATH = OUTPUT_SVGPATH
```

## execute
add svg file to the directory
```
blender --background --python ./convert.py
```
show output the dir
