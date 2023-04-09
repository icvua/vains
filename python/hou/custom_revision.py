import gazu
import os


gazu.client.set_host("http://192.168.3.116/api")
gazu.log_in("pipeline@rapa.org", "netflixacademy")
project = gazu.project.get_project_by_name("hook")
chopsticks = gazu.project.get_project_by_name("chopsticks")

tree_sample = {
    "working": {
        "mountpoint": "/mnt/pipeline/personal/jhLee",
        "root": "kitsu",
        "folder_path": {
            "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/working/v<Revision>",
            "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/working/v<Revision>",
            "style": "lowercase"
        },
        "file_name": {
            "shot": "<Project>_<Sequence>_<Shot>_<TaskType>_<Revision>",
            "asset": "<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>",
            "style": "lowercase"
        }
    },
    "output": {
        "mountpoint": "/mnt/pipeline/personal/jhLee",
        "root": "kitsu",
        "folder_path": {
            "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/output/<OutputType>/v<Revision>",
            "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>/v<Revision>",
            "style": "lowercase"
        },
        "file_name": {
            "shot": "<Project>_<Sequence>_<Shot>_<OutputType>_v<Revision>",
            "asset": "<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>",
            "style": "lowercase"
        }
    }
}
gazu.files.update_project_file_tree(chopsticks, tree_sample)
fx_ttp = gazu.task.get_task_type_by_name("FX")
ot_ttp = gazu.files.get_output_type_by_name("movie_file")

for shot in gazu.shot.all_shots_for_project(chopsticks):
    for task in gazu.task.all_tasks_for_shot(shot):
        working_file_path = os.path.dirname(
            gazu.files.build_working_file_path(task)
        )
        if os.path.exists(working_file_path):
            print("path exists", working_file_path)
            pass
        else:
            print(working_file_path)
            os.makedirs(working_file_path)
    output_file_path = os.path.dirname(
        gazu.files.build_entity_output_file_path(shot, ot_ttp, fx_ttp)
    )
    if os.path.exists(output_file_path):
        print("path exists", output_file_path)
        pass
    else:
        print(output_file_path)
        os.makedirs(output_file_path)

for asset in gazu.asset.all_assets_for_project(chopsticks):
    for task in gazu.task.all_tasks_for_asset(asset):
        working_file_path = os.path.dirname(
            gazu.files.build_working_file_path(task)
        )

        if os.path.exists(working_file_path):
            print("path exists", working_file_path)
            pass
        else:
            print(working_file_path)
            os.makedirs(working_file_path)
    output_file_path = os.path.dirname(
        gazu.files.build_entity_output_file_path(asset, ot_ttp, fx_ttp)
    )
    if os.path.exists(output_file_path):
        print("path exists", output_file_path)
        pass
    else:
        print(output_file_path)
        os.makedirs(output_file_path)
