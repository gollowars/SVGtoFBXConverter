import bpy
import glob
from os.path import basename

###################
# CONST
DIR_PATH = INPUT_SVGPATH
FILE_KIND = "*.svg"
OUTPUT_PATH = OUTPUT_SVGPATH


def convertSVGtoFBX(filePath, name):
  filterGlob = "INVOKE_DEFAULT"
  bpy.ops.import_curve.svg(filepath=filePath,filter_glob=filterGlob)
  target = bpy.data.objects['Curve']
  # 選択
  target.select = True
  bpy.context.scene.objects.active = target
  bpy.ops.object.origin_set(type="ORIGIN_CENTER_OF_VOLUME")
  target.rotation_euler[0] = 1.5708
  target.rotation_euler[1] = 0.0
  target.rotation_euler[2] = 0.0
  target.scale[0] = 300
  target.scale[1] = 300
  target.scale[2] = 300
  target.data.extrude = 0.0001
  bpy.ops.object.convert(target="MESH")
  bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
  bpy.ops.object.material_slot_remove()
  outputpath = OUTPUT_PATH + name + ".fbx"
  bpy.ops.export_scene.fbx(filepath=outputpath,apply_scale_options="FBX_SCALE_ALL")
  bpy.ops.object.delete()


if __name__ == "__main__":
  searchfiles = DIR_PATH + FILE_KIND
  filelist = glob.glob(searchfiles)

  for filepath in filelist:
    filename = basename(filepath)
    name = filename.split('.')[0]
    convertSVGtoFBX(filepath, name)
