import bpy
import bmesh
import math
import numpy as np
import mathutils as mu
import random

# region ボーンの周りにメッシュを作成するテスト


def testmeth001():
    # ボーンの名称と座標のリストを作成する
    # ボーンの名称はbone00～bone03とする
    # ボーンの座標は設定する

    # ボーンの名称,　ヘッドの座標,　テールの座標の辞書を作成する
    # ボーンの名称はbone00～bone03とする
    # ボーンの座標はランダムに設定する
    # ボーンの座標はx,y,zの値を持つリストとする
    bone_locations = []
    for i in range(4):
        bone_locations.append(
            {
                "name": "bone" + str(i).zfill(2),
                "head": (0, 0, i * 0.2),
                "tail": (0, 0, i * 0.2 + 0.2),
            }
        )
    # アーマチュアを作成する
    armature = bpy.data.armatures.new("armature")
    armature_obj = bpy.data.objects.new("armature_obj", armature)
    bpy.context.scene.collection.objects.link(armature_obj)

    # アーマチュアを編集モードにする
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode="EDIT")

    # ボーンを作成
    tempbone = None
    for bone_location in bone_locations:
        bone = armature.edit_bones.new(bone_location["name"])
        bone.head = bone_location["head"]
        bone.tail = bone_location["tail"]
        # head と tail のベクトルを作成
        # ベクトルはノーマライズ

        if tempbone is not None:
            bone.parent = tempbone
            tempbone = bone
        else:
            tempbone = bone

    # アーマチュアをオブジェクトモードにする
    bpy.ops.object.mode_set(mode="OBJECT")

    verts = []
    for bone_location in bone_locations:
        v = (
            mu.Vector(bone_location["tail"]) - mu.Vector(bone_location["head"])
        ).normalized()
        # ベクトルを軸としたQuaternionを作成
        # 回転は60度とする
        q = mu.Quaternion(v, math.radians(60))
        q0 = mu.Quaternion(v, 0)
        for i in range(4):
            q0 = mu.Quaternion(v, 0)
            for j in range(6):
                verts.append(
                    q0 @ mu.Vector((0.5, 0, i * 0.05))
                    + mu.Vector(bone_location["head"])
                )
                q0 = q0 @ q
    faces = []
    print(verts.count)
    for r in range(15):
        for i in range(6):
            if i == 0:
                faces.append((r * 6, (r + 1) * 6, (r + 1) * 6 + 5, r * 6 + 5))
            else:
                faces.append(
                    (r * 6 + i, (r + 1) * 6 + i, (r + 1) * 6 + i - 1, r * 6 + i - 1)
                )

    msh = bpy.data.meshes.new(name="cubemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    obj = bpy.data.objects.new(name="cube", object_data=msh)

    bpy.context.scene.collection.objects.link(obj)


# endregion
