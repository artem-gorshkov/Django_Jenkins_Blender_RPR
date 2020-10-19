from jenkinsapi.jenkins import Jenkins
import os
import glob


def render_scene(path, rgb):
    url = 'http://localhost:8888'
    username = 'artem'
    password = 'qwerty25'
    pipeline = 'triger_from_django'
    params = {'RGB': rgb, 'FILE': path}
    # params = {'RGB': 'FF2233', 'FILE': r'C:\Users\HP\Desktop\blender_script\scene_1.blend'}
    jenkins = Jenkins(url, username=username, password=password, useCrumb=True)
    job = jenkins[pipeline]
    qi = job.invoke(build_params=params)
    if qi.is_queued() or qi.is_running():
        qi.block_until_complete()
    build = qi.get_build()
    # build = job.get_last_good_build()
    files = glob.glob('/home/artem/django/djangoProject/static/*g/*')
    for f in files:
        os.remove(f)
    img_path = '/home/artem/django/djangoProject/static/img/rendered.png'
    log_path = '/home/artem/django/djangoProject/static/log/log.txt'
    for i in build.get_artifacts():
        if 'img' in i.url:
            i.save(img_path)
        else:
            i.save(log_path)
    f = open(log_path, 'r')
    log = f.read()
    f.close()
    return log
