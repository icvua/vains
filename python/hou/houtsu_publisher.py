import gazu
import os


class Houpub:
    _file_tree = None

    def __init__(self, project):
        gazu.client.set_host("http://192.168.3.116/api")
        gazu.log_in("pipeline@rapa.org", "netflixacademy")
        self.project = gazu.project.get_project_by_name(project)

    @property
    def file_tree(self):
        return self._file_tree

    @file_tree.setter
    def file_tree(self, path):
        mount_point = path[0]
        root = path[1]
        self._file_tree = {
            "working": {
                "mountpoint": mount_point,
                "root": root,
                "folder_path": {
                    "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/working",
                    "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/working",
                    "style": "lowercase"
                },
                "file_name": {
                    "shot": "<Project>_<Sequence>_<Shot>_<TaskType>_<Revision>",
                    "asset": "<Project>_<AssetType>_<Asset>_<TaskType>_<Revision>",
                    "style": "lowercase"
                }
            },
            "output": {
                "mountpoint": mount_point,
                "root": root,
                "folder_path": {
                    "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>/output/<OutputType>",
                    "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>/output/<OutputType>",
                    "style": "lowercase"
                },
                "file_name": {
                    "shot": "<Project>_<Sequence>_<Shot>_<OutputType>_v<Revision>",
                    "asset": "<Project>_<AssetType>_<Asset>_<OutputType>_v<Revision>",
                    "style": "lowercase"
                }
            }
        }

    def update_file_tree(self):
        if self.file_tree is None:
            return
        else:
            gazu.files.update_project_file_tree(self.project, self.file_tree)

    def publish_working_file(self, ent, task_type, task_name, work_name):
        task = self.get_task(ent, task_type, task_name)
        gazu.files.new_working_file(task, name=work_name)

    def upload_working_file(self, ent, task_type, task_name, work_name, path):
        task = self.get_task(ent, task_type, task_name)
        wkf = gazu.files.get_last_working_file_revision(task, name=work_name)
        gazu.files.upload_working_file(wkf, path)

    def download_working_file(self, ent, task_type, task_name, work_name, path):
        task = self.get_task(ent, task_type, task_name)
        wkf = gazu.files.get_last_working_file_revision(task, name=work_name)
        gazu.files.download_working_file(task, file_path=path)

    @staticmethod
    def get_task(ent, task_type, task_name):
        entity = gazu.entity.get_entity_by_name(ent)
        task_type_name = gazu.task.get_task_type_by_name(task_type)
        task = gazu.task.get_task_by_name(entity, task_type_name, name=task_name)
        return task

    @staticmethod
    def find_shot(dirs, inp):
        for arg in dirs:
            if arg['name'] == inp:
                return inp
            else:
                pass
        raise

    def make_working_dirs(self):
        """
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        여기서부터 미완성임
        """
        for shot in gazu.shot.all_shots_for_project(self.project):
            for task in gazu.task.all_tasks_for_shot(shot):
                working_file_path = os.path.dirname(
                    gazu.files.build_working_file_path(task)
                )
                rev = self.get_revision(task)
                for rev in range(1, rev + 1):
                    rev_path = os.path.join(working_file_path, f'v{rev:03}')
                    self.make_dirs(rev_path)

    def make_output_dirs(self, shot, task_type, output_type):
        task_type = gazu.task.get_task_type_by_name(task_type)
        output_type = gazu.files.get_output_type_by_name(output_type)
        gazu.entity.get_entity_by_name(shot)
        gazu.files.build_entity_output_file_path(shot, output_type, task_type)

    @staticmethod
    def get_revision(*args):
        if len(args) == 1:
            last_rev = gazu.files.get_last_working_file_revision(args)
        elif len(args) == 2:
            task = args[0]
            name = args[1]
            last_rev = gazu.files.get_last_working_file_revision(task, name)
        else:
            return
        rev = last_rev['revision']
        return rev

    @staticmethod
    def make_dirs(dir_path):
        if os.path.exists(dir_path):
            print("Path exists", dir_path)
            pass
        else:
            print("Path made", dir_path)
            os.makedirs(dir_path)

#
# a = Houpub('Chopsticks')
# a.publish_working_file('S1_01', 'FX', 'main', 'main')
