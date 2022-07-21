from __future__ import unicode_literals

frames = []

series = {}


def clear():
    series.clear()
    frames.clear()


def draw(data):
    scene = data["Label"]
    frame = data["Frame"]
    overdraw = data["Overdraw"]
    particle = data["Particles"]
    frames.append(str(frame))
    if scene not in series.keys():
        newScene = {}
        newOver = []
        newPar = []
        for i in range(len(frames) - 1):
            newOver.append([frames[i], None])
            newPar.append([frames[i], None])
        newScene["overdraw"] = newOver
        newScene["particle"] = newPar
        series[scene] = newScene
    for aScene in series:
        if aScene != scene:
            series[aScene]["overdraw"].append([str(frame), None])
            series[aScene]["particle"].append([str(frame), None])
            continue
        series[aScene]["particle"].append([str(frame), particle])
        series[aScene]["overdraw"].append([str(frame), overdraw])


def get_data():
    response = {"series": series, "frame": frames}
    return response
