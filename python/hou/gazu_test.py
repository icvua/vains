import gazu
import os
import json

gazu.client.set_host("http://192.168.3.116/api")
gazu.log_in("pipeline@rapa.org", "netflixacademy")
hook = gazu.project.get_project_by_name("hook")
avata3 = gazu.project.get_project_by_name("Pizza")
chopsticks = gazu.project.get_project_by_name("chopsticks")
place = gazu.asset.get_asset_type_by_name("place")
# gazu.asset.new_asset(chopsticks, place, "daughters_room")
assets = (gazu.asset.all_assets_for_project(chopsticks))
shots = gazu.shot.all_shots_for_project(chopsticks)

# gazu.shot.new_sequence(chopsticks, "Scene_1")

# print(gazu.shot.get_sequence_by_name("Scene_1"))# projects = gazu.client.post("data/projects", {"name": "Chopsticks"})
# # print(projects)
# project = gazu.project.get_project_by_name("Chopsticks")
# seq = gazu.shot.get_sequence_by_name(project, 'S1')
# shot = gazu.shot.get_shot_by_name(seq, 'S1_01')

# tasks = gazu.task.all_task_types()
# task_type = gazu.task.get_task_type_by_name('Animation')
# print(tasks)
# statuses = gazu.task.all_task_statuses()
# print(statuses)
# status = gazu.task.get_task_status_by_name('Ready To Start')
#
# gazu.task.new_task(shot,
#     task_type,
#     name="main",
#     task_status=None,
#     assigner=None,
#     assignees=[],)


# # gazu.project.close_project(project)
# # gazu.client.delete(project)
#
#
# # a = gazu.client.get("data/projects")
# # for i in a:
# #     print(i)
#
# chopsticks = gazu.project.get_project_by_name("Chopsticks")
# # char = gazu.asset.get_asset_type_by_name("Characters")
# # father = gazu.asset.new_asset(chopsticks, char, "Father")
# # daughter = gazu.asset.new_asset(chopsticks, char, "Daughter")
#
# # testcam = gazu.asset.get_asset_by_name(chopsticks, "S1_01_CAM")
# # print(testcam['data']['path'])
# # print(testcam['data']['type'])
# # cam = gazu.asset.get_asset_type_by_name("Camera")
# # print(cam)
# # gazu.asset.new_asset(chopsticks, cam, "S1_03_CAM", description="S1_03_CAM",
#                      # extra_data={'path': '/home/rapa/S1_03_CAM.abc'})
#
# # test_import_cam = gazu.asset.get_asset_by_name("Chopsticks", "S1_03_CAM", cam)
# # print(test_import_cam)
# tree = {
#   "working": {
#     "mountpoint": "/mnt/pipeline/personal/jhLee",
#     "root": "productions",
#     "folder_path": {
#       "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>",
#       "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>",
#       "sequence": "<Project>/sequences/<Sequence>/<TaskType>",
#       "style": "lowercase"
#     },
#     "file_name": {
#       "shot": "<Project>_<Sequence>_<Shot>_<TaskType>",
#       "asset": "<Project>_<AssetType>_<Asset>_<TaskType>",
#       "sequence": "<Project>_<Sequence>_<TaskType>",
#       "style": "lowercase"
#     }
#   }
# }
# gazu.files.set_project_file_tree(chopsticks, tree)
# gazu.files.update_project_file_tree(chopsticks, tree)
# # for asset in gazu.asset.all_assets_for_project(chopsticks):
# #     for task in gazu.task.all_tasks_for_asset(asset):
# #         path = os.path.dirname(
# #             gazu.files.build_working_file_path(task)[1:]
# #         )
# #         os.makedirs(path)
#
#
# # gazu.files.update_project_file_tree(chopsticks, {
# #   "working": {
# #     "mountpoint": "/mnt/pipeline/personal/jhLee",
# #     "root": "productions",
# #     "folder_path": {
# #       "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>",
# #       "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>",
# #       "sequence": "<Project>/sequences/<Sequence>/<TaskType>",
# #       "style": "lowercase"
# #     },
# #     "file_name": {
# #       "shot": "<Project>_<Sequence>_<Shot>_<TaskType>",
# #       "asset": "<Project>_<AssetType>_<Asset>_<TaskType>",
# #       "sequence": "<Project>_<Sequence>_<TaskType>",
# #       "style": "lowercase"
# #     }
# #   }
# # })
#
#
# # shots = gazu.shot.all_shots_for_project(chopsticks)
# # print(shots)
# # print(chopsticks['id'])
#
# # gazu.shot.new_episode("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1")
# # gazu.shot.new_sequence("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1_01_06")
# # ptt = gazu.shot.get_sequence_by_name("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1")
# # print(ptt)
# # gazu.shot.new_shot("0249b2ef-5252-4db6-b22e-72082cfca24d", "43f0905c-e01c-4645-949d-11ecf32f4c71", "S1_01",
# #                    nb_frames=151, frame_in=1, frame_out=151)


tree_sample = {
    "working": {
        "mountpoint": "/your_mount_directory",
        "root": "your_root_directory",
        "folder_path": {
            "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>",
            "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>",
            "style": "lowercase"
        },
        "file_name": {
            "shot": "<Project>_<Sequence>_<Shot>_<TaskType>",
            "asset": "<Project>_<AssetType>_<Asset>_<TaskType>",
            "style": "lowercase"
        }
    }
}
gazu.files.update_project_file_tree(your_project_name, tree_sample)

for shot in gazu.shot.all_shots_for_project(your_project_name):
    for task in gazu.task.all_tasks_for_shot(shot):
        path = os.path.dirname(
            gazu.files.build_working_file_path(task)[1:]
        )
        print(path)
        os.makedirs(os.sep + path)

for asset in gazu.asset.all_assets_for_project(your_project_name):
    for task in gazu.task.all_tasks_for_asset(asset):
        path = os.path.dirname(
            gazu.files.build_working_file_path(task)[1:]
        )
        print(path)
        os.makedirs(os.sep + path)


# a = gazu.shot.all_shots_for_project(hook)
# for i in a:
#     fff = gazu.task.all_task_types_for_shot(i)
#     if fff != "":
#         for n in fff:
#             pass
#             # print(n)
#         break
# s01 = gazu.shot.get_shot_by_name("SQ01", "0010")
# b = gazu.task.all_task__for_shot(s01)
# for i in b:
#     for c in i:
#         print(c)
#     break
# for shot in gazu.shot.all_shots_for_project(chopsticks):
#     gazu.files.build_working_file_path(shot)
# tasklist = ['Modeling', 'Texture', 'Rigging']
# gazu.task.new_task_type("happy")
# mod = gazu.task.get_task_type_by_name("happy")
# a = mod['id']
# print(mod)
# print(a)
# b = gazu.task.all_task_types()
# for i in b:
#     print(i)
# gazu.task.remove_task_type('b714d9cb-e139-41b8-b1a3-141b84317b82')
# gazu.task.remove_task_type(mod)
# gazu.task.remove_task_type('texture')
# gazu.task.remove_task_type('rigging')
# for n in tasklist:
# print(n, type(n))
# gazu.task.new_task_type(n)

# for asset in gazu.asset.all_assets_for_project(chopsticks):
#     dtt = asset['data']
#     print(dtt)
#     if dtt == {'Ready for': 'FX'}:
#         asset['data'] = {'oh': 'shit'}
#     gazu.asset.update_asset_data(asset, data={''})
    # print(gazu.task.all_task_types_for_asset(asset))
    # print(gazu.task.all_tasks_for_asset(asset))
    # print(gazu.asset.get_asset_type_from_asset(asset))

    # gazu.task.new_task(asset,)
    # gazu.asset.update_asset_data(asset, data={"task_types": "FX"})
    # for task in gazu.task.all_tasks_for_asset(asset):
    #     gazu.files.build_working_file_path(task)
