import bpy
import glob
from os.path import basename

###################
# CONST
DIR_PATH = "/Users/ashikawa/work/mitsufuji/03_material/image_svg_outline/01_r/"
FILE_KIND = "*.svg"


if __name__ == "__main__":
  # searchfiles = DIR_PATH + FILE_KIND
  # filelist = glob.glob(searchfiles)

  filePath = "/Users/ashikawa/work/mitsufuji/03_material/image_svg_outline/01_r/r1.svg"
  filterGlob = "INVOKE_DEFAULT"

  # import svg
  # bpy.ops.import_curve.svg(filepath="/Users/ashikawa/work/mitsufuji/03_material/image_svg_outline/01_r/r1.svg",filter_glob="INVOKE_DEFAULT")
  bpy.ops.import_curve.svg(filepath=filePath,filter_glob=filterGlob)

  # 選択
  bpy.data.objects['Curve'].select = True
  bpy.context.scene.objects.active = bpy.data.objects['Curve']

  # ピボットポイントをオブジェクトの重心にする。
  bpy.ops.object.origin_set(type="ORIGIN_CENTER_OF_VOLUME")

  # position変更
  # 直いじり
  # bpy.data.objects['Curve'].location[0] = 0
  # bpy.data.objects['Curve'].location[1] = 0
  # bpy.data.objects['Curve'].location[2] = 0

  bpy.data.objects['Curve'].rotation_euler[0] = 1.5708
  bpy.data.objects['Curve'].rotation_euler[1] = 0.0
  bpy.data.objects['Curve'].rotation_euler[2] = 0.0

  # scale
  bpy.data.objects['Curve'].scale[0] = 300
  bpy.data.objects['Curve'].scale[1] = 300
  bpy.data.objects['Curve'].scale[2] = 300


  # 押し出し
  bpy.data.objects['Curve'].data.extrude = 0.0001

  # meshに変換
  bpy.ops.object.convert(target="MESH")

  # 適応
  bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)

  # context change
  # bpy.context.space_data.context = "MATERIAL"
  # material delete
  bpy.ops.object.material_slot_remove()

  # export
  bpy.ops.export_scene.fbx(filepath="/Users/ashikawa/work/mitsufuji/03_material/models/exports/sample.fbx",apply_scale_options="FBX_SCALE_ALL")

  # delete
  bpy.ops.object.delete()

