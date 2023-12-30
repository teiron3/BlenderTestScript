# blender のスクリプト
# 正10面体のポリゴンを作成する
# 関数名は testmeth001
# マテリアルを10個作成し、正10面体の各面に割り当てる
# マテリアルの色をランダムに設定する

import bpy
import bmesh
import math
import numpy as np
import random


# メッシュを作成する


# region マテリアル作成テスト
def testmeth001():
    # マテリアルを8個作成する
    # マテリアルの変数はリストで名称はmat[0]～mat[7]とする
    # マテリアルの色はランダムに設定する
    mat = []
    for i in range(8):
        bpy.data.materials.new(name="mat" + str(i))
        bpy.data.materials[i].diffuse_color = (
            random.random(),
            random.random(),
            random.random(),
            1.0,
        )

    # 正10面体の頂点座標の入った配列を作成する
    vertices = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ]
    # 面を作成する
    faces = [
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 4],
        [0, 4, 1],
        [5, 1, 2],
        [5, 2, 3],
        [5, 3, 4],
        [5, 4, 1],
    ]

    # メッシュを作成する
    mesh = bpy.data.meshes.new(name="mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    # 各面にマテリアルを割り当てる

    for i in range(8):
        mesh.polygons[i].material_index = i

    # オブジェクトを作成する
    obj = bpy.data.objects.new(name="obj", object_data=mesh)
    for i in range(8):
        obj.data.materials.append(bpy.data.materials[i])
    bpy.context.scene.collection.objects.link(obj)

    return


# endregion


# region 8面体を作成して、BSDFでマテリアルを設定するテストメソッド
def testmeth002():
    # マテリアルを作成する
    mat = bpy.data.materials.new(name="mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["プリンシプルBSDF"]
    colornode = mat.node_tree.nodes.new("ShaderNodeBrightContrast")

    colornode.inputs[0].default_value = (0.70784, 0, 0, 1)
    mat.node_tree.links.new(colornode.outputs[0], bsdf.inputs[0])

    bsdf.inputs[9].default_value = 0
    bsdf.inputs[17].default_value = 1

    # 正10面体の頂点座標の入った配列を作成する
    vertices = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ]
    # 面を作成する
    faces = [
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 4],
        [0, 4, 1],
        [5, 1, 2],
        [5, 2, 3],
        [5, 3, 4],
        [5, 4, 1],
    ]

    # メッシュを作成する
    mesh = bpy.data.meshes.new(name="mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    # 各面にマテリアルを割り当てる

    # for i in range(8):
    #   mesh.polygons[i].material_index = i

    # オブジェクトを作成する
    obj = bpy.data.objects.new(name="obj", object_data=mesh)
    obj.data.materials.append(mat)
    bpy.context.scene.collection.objects.link(obj)

    return


# endregion


# region アーマチュアとボーンウェイトのテスト
def testmeth003():
    # region マテリアルを作成する
    mat = bpy.data.materials.new(name="mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["プリンシプルBSDF"]
    colornode = mat.node_tree.nodes.new("ShaderNodeBrightContrast")
    colornode.inputs[0].default_value = (0.70784, 0, 0, 1)
    mat.node_tree.links.new(colornode.outputs[0], bsdf.inputs[0])
    # endregion

    # 立方体を作成
    verts = (
        (1, 1, 0),
        (1, -1, 0),
        (-1, -1, 0),
        (-1, 1, 0),
        (1, 1, 2),
        (1, -1, 2),
        (-1, -1, 2),
        (-1, 1, 2),
    )
    faces = (
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (4, 0, 3, 7),
    )
    mesh = bpy.data.meshes.new(name="mesh")
    mesh.from_pydata(verts, [], [])
    mesh.update()

    # オブジェクトを作成する
    obj = bpy.data.objects.new(name="obj", object_data=mesh)
    obj.data.materials.append(mat)
    bpy.context.scene.collection.objects.link(obj)

    # アーマチュア
    armature = bpy.data.armatures.new("armature")
    armature_obj = bpy.data.objects.new("armature_obj", armature)
    bpy.context.scene.collection.objects.link(armature_obj)

    # アーマチュアを編集モードにする
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode="EDIT")
    # ボーンを作成
    bone = armature.edit_bones.new("bone")
    bone.head = (0, 0, 0)
    bone.tail = (0, 0, 1)
    bone2 = armature.edit_bones.new("bone2")
    bone2.parent = bone
    bone2.head = bone.tail
    bone2.tail = (0, 0, 2)

    # armature_obj.data.bones.append(bone)

    # アーマチュアをオブジェクトモードにする
    bpy.ops.object.mode_set(mode="OBJECT")

    # アーマチュアとメッシュを関連付ける
    obj.parent = armature_obj
    obj.modifiers.new("Armature", "ARMATURE").object = armature_obj

    # メッシュオブジェクトに頂点グループを追加
    v = obj.vertex_groups.new(name="bone")
    v.add((4, 5, 6, 7), 1.0, "REPLACE")

    return


# endregion


def testmeth004():
    # マテリアルを作成する
    mat = bpy.data.materials.new(name="mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["プリンシプルBSDF"]
    colornode = mat.node_tree.nodes.new("ShaderNodeBrightContrast")
    colornode.inputs[0].default_value = (0.70784, 0, 0, 1)
    mat.node_tree.links.new(colornode.outputs[0], bsdf.inputs[0])

    # 立方体を作成
    verts = []
    faces = []
    platelength = 20
    AddHeight = 0.1
    z = 0
    for i in range(0, 4 * platelength):
        w = 0.8
        s = 1
        x = w * s if (i + 1) % 4 == 1 or (i + 1) % 4 == 0 else 1
        y = w * s if (i + 1) % 4 == 1 or (i + 1) % 4 == 0 else 1
        verts += (
            (x, y, z),
            (x, -y, z),
            (-x, -y, z),
            (-x, y, z),
        )
        z += (i % 2) * 0.1
    for i in range(0, 4 * platelength - 1):
        faces += (
            (i * 4, i * 4 + 1, (i + 1) * 4 + 1, (i + 1) * 4),
            (i * 4 + 1, i * 4 + 2, (i + 1) * 4 + 2, (i + 1) * 4 + 1),
            (i * 4 + 2, i * 4 + 3, (i + 1) * 4 + 3, (i + 1) * 4 + 2),
            (i * 4 + 3, i * 4, (i + 1) * 4, (i + 1) * 4 + 3),
        )
    mesh = bpy.data.meshes.new(name="mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    # オブジェクトを作成する
    obj = bpy.data.objects.new(name="obj", object_data=mesh)
    obj.data.materials.append(mat)
    bpy.context.scene.collection.objects.link(obj)

    # アーマチュア
    armature = bpy.data.armatures.new("armature")
    armature_obj = bpy.data.objects.new("armature_obj", armature)
    bpy.context.scene.collection.objects.link(armature_obj)

    # アーマチュアを編集モードにする
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode="EDIT")
    # ボーンを作成
    bone = armature.edit_bones.new("bone")
    bone.head = (0, 0, 0)
    bone.tail = (0, 0, 0.01)
    bone2 = armature.edit_bones.new("bone2")
    bone2.parent = bone
    bone2.head = bone.tail
    bone2.tail = (0, 0, 2)

    # armature_obj.data.bones.append(bone)

    # アーマチュアをオブジェクトモードにする
    bpy.ops.object.mode_set(mode="OBJECT")

    # アーマチュアとメッシュを関連付ける
    obj.parent = armature_obj
    obj.modifiers.new("Armature", "ARMATURE").object = armature_obj

    # メッシュオブジェクトに頂点グループを追加
    v1 = obj.vertex_groups.new(name="bone")
    v2 = obj.vertex_groups.new(name="bone2")
    for i in range(1, platelength):
        j = i * 16
        k = i / platelength
        fverts = []
        for l in range(0, 16):
            fverts.append(j + l)
        v1.add(fverts, 1 - k, "REPLACE")
        v2.add(fverts, k, "REPLACE")

    return


def testmeth005():
    verts = ((1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0))
    mesh = bpy.data.meshes.new(name="mesh")
    mesh.from_pydata(verts, [], [])
    mesh.update()
    obj = bpy.data.objects.new(name="obj", object_data=mesh)
    bpy.context.scene.collection.objects.link(obj)

    bmsh = bmesh.new()
    bmsh.from_mesh(mesh)
    newverts = ((1, 1, 1), (0, 0, 1))
    for v in newverts:
        w = bmsh.verts.new(v)
        print(w.index)
    bmsh.to_mesh(mesh)
    mesh.update()
    return
