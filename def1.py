import bpy
import bmesh
import math
import numpy as np
import mathutils as mu


# region 全て削除
def all_clear():
    co = 0
    for x in bpy.data.objects:
        bpy.data.objects.remove(x)
    for x in bpy.data.meshes:
        bpy.data.meshes.remove(x)
    for x in bpy.data.materials:
        print(co)
        co += 1
        bpy.data.materials.remove(x)
    for x in bpy.data.armatures:
        bpy.data.armatures.remove(x)
    return


# endregion


# region メッシュオブジェクトの作成
def testfn1():
    verts = [[1, 1, 1.0], [2.0, 1.0, 1.0], [2.0, 2.0, 1.0]]
    faces = [[0, 1, 2]]

    verts = verts + [[1, 3, 1.0], [3.0, 1.0, 1.0], [2.0, 3.0, 1.0]]
    faces = faces + [[3, 4, 5]]
    msh = bpy.data.meshes.new(name="cubemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()

    obj = bpy.data.objects.new(name="cube", object_data=msh)

    print("success!!")
    bpy.context.scene.collection.objects.link(obj)
    return


# endregion


# region メッシュオブジェクトの作成
def testfn2():
    a = np.array([3, 3, 3])
    verts = [[1, 0, 0], [-1, 0, 0], [0, 1, 0]]
    for index in range(0, 3):
        verts[index] = 3 * np.array(verts[index])
    faces = [[0, 1, 2]]
    msh = bpy.data.meshes.new(name="trianglemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="triangle", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn3():
    rad = 3.14159 * 2
    points = 100
    verts = []
    faces = []
    verts.append([0, 0, 0])
    for i in range(0, points):
        verts.append([math.cos(rad * i / points), math.sin(rad * i / points), 0])
    for i in range(1, points):
        faces.append([0, i, i + 1])
    faces.append([0, points, 1])

    msh = bpy.data.meshes.new(name="trianglemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="triangle", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn4():
    rad = 3.14159 * 2
    rounds = 1000
    zlength = 10
    verts = []
    faces = []
    for z in range(0, zlength):
        for i in range(0, rounds):
            verts.append(
                [
                    math.cos(rad * i / rounds) * (1 + z / zlength),
                    math.sin(rad * i / rounds) * (1 + z / zlength),
                    z / zlength,
                ]
            )

    for z in range(0, zlength - 1):
        for i in range(0, rounds):
            if i == rounds - 1:
                faces.append(
                    [z * rounds + i, z * rounds, (z + 1) * rounds, (z + 1) * rounds + i]
                )
                continue
            faces.append(
                [
                    z * rounds + i,
                    z * rounds + i + 1,
                    (z + 1) * rounds + i + 1,
                    (z + 1) * rounds + i,
                ]
            )

    msh = bpy.data.meshes.new(name="trianglemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="triangle", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn5():
    rad = 3.14159 * 2
    rounds = 1000
    zlength = 10
    verts = []
    faces = []
    for z in range(0, zlength):
        for i in range(0, rounds):
            verts.append(
                [
                    math.cos(rad * i / rounds)
                    * ((1 + math.sin(rad * 25 * i / rounds) / 20) + z / (zlength * 2)),
                    math.sin(rad * i / rounds)
                    * ((1 + math.sin(rad * 25 * i / rounds) / 20) + z / (zlength * 2)),
                    z / zlength,
                ]
            )

    for z in range(0, zlength - 1):
        for i in range(0, rounds):
            if i == rounds - 1:
                faces.append(
                    [z * rounds + i, z * rounds, (z + 1) * rounds, (z + 1) * rounds + i]
                )
                continue
            faces.append(
                [
                    z * rounds + i,
                    z * rounds + i + 1,
                    (z + 1) * rounds + i + 1,
                    (z + 1) * rounds + i,
                ]
            )

    msh = bpy.data.meshes.new(name="trianglemesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="triangle", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn6():
    # 中心が0,0,0 で一辺が1の平面
    verts = [[-0.5, -0.5, 0], [0.5, -0.5, 0], [0.5, 0.5, 0], [-0.5, 0.5, 0]]
    faces = [[0, 1, 2, 3]]
    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], faces)
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square", object_data=msh)
    )
    print("tst")
    for vert in verts:
        vert[2] = 2
    msh2 = bpy.data.meshes.new(name="squaremesh2")
    msh2.from_pydata(verts, [], faces)
    msh2.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square2", object_data=msh2)
    )
    return


# endregion


# region メッシュの頂点追加テスト
def testfn7():
    r = -10
    a = mu.Euler((0, math.radians(r), 0), "XYZ")
    q = a.to_quaternion()
    # 中心が0,0,0 で一辺が1の平面
    verts = [[-0.5, -0.5, 0], [0.5, -0.5, 0], [0.5, 0.5, 0], [-0.5, 0.5, 0]]
    faces = [(0, 1, 2, 3)]
    faces2 = [[4, 5, 6, 7]]
    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], faces)
    msh.update()
    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square2", object_data=msh)
    )
    for vert in verts:
        vert[2] = 1
    bmsh = bmesh.new()
    bmsh.from_mesh(msh)
    appendverts = []
    for vert in verts:
        appendverts.append(bmsh.verts.new(vert))
    for face in faces:
        bmsh.faces.new(appendverts[i] for i in face)
    bmsh.to_mesh(msh)
    bmsh.free()

    return


# endregion


# region Quaternionのテスト
def testfn8():
    verts = []
    for r in range(0, 360):
        a = mu.Euler((0, math.radians(r), 0), "XYZ")
        q = a.to_quaternion()
        y = q @ mu.Vector((1, 1, 1))
        verts.append(y)

    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], [])
    msh.update()

    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square2", object_data=msh)
    )
    return


# endregion


# region Quaternionのテスト
def testfn9():
    verts = []
    faces = []
    centerpointcount = 100
    radius = 0.05
    issurface = False
    for ctpointcount in range(0, centerpointcount):
        if ctpointcount % 2 == 0:
            issurface = False
        else:
            issurface = True
        if issurface:
            for r in range(180, 0, -6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, 1, 0)) + mu.Vector(
                    (ctpointcount * radius * 2, 0, 0)
                )
                verts.append(x)
        else:
            for r in range(180, 360, 6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, 1, 0)) + mu.Vector(
                    (ctpointcount * radius * 2, 0, 0)
                )
                verts.append(x)
    sidecount = verts.__len__()
    for ctpointcount in range(0, centerpointcount):
        if ctpointcount % 2 == 0:
            issurface = False
        else:
            issurface = True
        if issurface:
            for r in range(180, 0, -6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, -1, 0)) + mu.Vector(
                    (ctpointcount * radius * 2, 0, 0)
                )
                verts.append(x)
        else:
            for r in range(180, 360, 6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, -1, 0)) + mu.Vector(
                    (ctpointcount * radius * 2, 0, 0)
                )
                verts.append(x)
    for count in range(0, sidecount - 1):
        faces.append([count, count + 1, count + sidecount + 1, count + sidecount])
    for count in range(0, sidecount - 1):
        faces.append(
            [
                count,
                count + sidecount,
                count + sidecount + 1,
                count + 1,
            ]
        )
    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], faces)
    msh.update()

    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn10():
    verts = []
    faces = []
    xlength = 1000
    ylength = 1000

    epicenter = [(100, 40), (90, 34), (1000, 4000)]
    wavewidth = [1, 0.3, 0.1]
    waveheight = [0.3, 0.8, 3]
    for x in range(0, xlength):
        for y in range(0, ylength):
            z = 0
            for i in range(0, 3):
                z += (
                    math.sin(
                        (mu.Vector(epicenter[i]) - mu.Vector((x, y))).length
                        * wavewidth[i]
                    )
                    * waveheight[i]
                )
            verts.append([x, y, z])
    for x in range(0, xlength - 1):
        for y in range(0, ylength - 1):
            faces.append(
                [
                    x * ylength + y,
                    x * ylength + y + 1,
                    (x + 1) * ylength + y + 1,
                    (x + 1) * ylength + y,
                ]
            )
    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], faces)
    msh.update()

    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square", object_data=msh)
    )
    return


# endregion


# region メッシュオブジェクトの作成
def testfn11():
    verts = []
    faces = []
    centerpointcount = 100
    radius = 0.5
    sinradius = 0.5
    raddonw = 50
    issurface = False
    for ctpointcount in range(0, centerpointcount):
        if ctpointcount % 2 == 0:
            issurface = False
        else:
            issurface = True
        if issurface:
            for r in range(180 + raddonw, 0 - raddonw, -6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = (q @ mu.Vector((radius, 1, 0))) * mu.Vector(
                    (1, 1, sinradius)
                ) + mu.Vector(
                    (
                        ctpointcount * math.cos(math.radians(raddonw)) * radius * 2,
                        0,
                        -math.sin(math.radians(raddonw)) * radius * sinradius,
                    )
                )
                verts.append(x)
        else:
            for r in range(180 - raddonw, 360 + raddonw, 6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, 1, 0)) * mu.Vector(
                    (1, 1, sinradius)
                ) + mu.Vector(
                    (
                        ctpointcount * math.cos(math.radians(raddonw)) * radius * 2,
                        0,
                        math.sin(math.radians(raddonw)) * radius * sinradius,
                    )
                )
                verts.append(x)
    sidecount = verts.__len__()
    for ctpointcount in range(0, centerpointcount):
        if ctpointcount % 2 == 0:
            issurface = False
        else:
            issurface = True
        if issurface:
            for r in range(180 + raddonw, 0 - raddonw, -6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, -1, 0)) * mu.Vector(
                    (1, 1, sinradius)
                ) + mu.Vector(
                    (
                        ctpointcount * math.cos(math.radians(raddonw)) * radius * 2,
                        0,
                        -math.sin(math.radians(raddonw)) * radius * sinradius,
                    )
                )
                verts.append(x)
        else:
            for r in range(180 - raddonw, 360 + raddonw, 6):
                a = mu.Euler((0, math.radians(r), 0), "XYZ")
                q = a.to_quaternion()
                x = q @ mu.Vector((radius, -1, 0)) * mu.Vector(
                    (1, 1, sinradius)
                ) + mu.Vector(
                    (
                        ctpointcount * math.cos(math.radians(raddonw)) * radius * 2,
                        0,
                        math.sin(math.radians(raddonw)) * radius * sinradius,
                    )
                )
                verts.append(x)
    for count in range(0, sidecount - 1):
        faces.append([count, count + 1, count + sidecount + 1, count + sidecount])
    for count in range(0, sidecount - 1):
        faces.append(
            [
                count,
                count + sidecount,
                count + sidecount + 1,
                count + 1,
            ]
        )
    msh = bpy.data.meshes.new(name="squaremesh")
    msh.from_pydata(verts, [], faces)
    msh.update()

    bpy.context.scene.collection.objects.link(
        bpy.data.objects.new(name="square", object_data=msh)
    )
    return


# endregion


# region メッシュ編集モードで選択している頂点のインデックスを取得する
def testfn12():
    # メッシュの編集モードで、選択している頂点のインデックスを取得しprintする
    obj = bpy.context.active_object
    bmsh = bmesh.from_edit_mesh(obj.data)
    for v in bmsh.verts:
        if v.select:
            print(v.index)


# endregion
