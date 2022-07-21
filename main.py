from __future__ import unicode_literals
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Grid
from pyecharts.globals import ThemeType

overdraws = {}
particles = {}
frames = []


def clear():
    overdraws.clear()
    particles.clear()
    frames.clear()
    line = Line()
    line.add_xaxis(frames)


def draw(data):
    scene = data["Label"]
    frame = data["Frame"]
    overdraw = data["Overdraw"]
    particle = data["Particles"]
    frames.append(str(frame))
    if scene not in overdraws.keys():
        o = []
        for i in range(len(frames) - 1):
            o.append(None)
        overdraws[scene] = o
    if scene not in particles.keys():
        p = []
        for i in range(len(frames) - 1):
            p.append(None)
        particles[scene] = p
    for aScene in overdraws:
        if aScene != scene:
            overdraws[aScene].append(None)
            continue
        overdraws[aScene].append(overdraw)
    for aScene in particles:
        if aScene != scene:
            particles[aScene].append(None)
            continue
        particles[aScene].append(particle)

    line = getLine('overdraw')
    line.add_xaxis(frames)
    for aScene, data1 in overdraws.items():
        line.add_yaxis(aScene, data1, is_connect_nones=False, markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")]))
    line2 = getLine('particles')
    line2.add_xaxis(frames)
    for aScene, data1 in particles.items():
        line2.add_yaxis(aScene, data1, is_connect_nones=False, markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")]))
    grid = Grid(init_opts=opts.InitOpts(width="1700px",
                                        height="800px"))
    grid.add(line, grid_opts=opts.GridOpts(pos_bottom="60%", pos_left="20%", pos_right="80"))
    grid.add(line2, grid_opts=opts.GridOpts(pos_top="60%", pos_left="20%", pos_right="80"))
    grid.render()


def getLine(name):
    return Line(init_opts=opts.InitOpts(width="1700px",
                                        height="350px",
                                        page_title="Overdraw",
                                        theme=ThemeType.DARK)) \
        .set_global_opts(xaxis_opts=opts.AxisOpts(name='frame', type_="value",
                                                  name_location='middle',
                                                  # 坐标轴名字所在的位置
                                                  name_gap=5,
                                                  # 坐标轴名字与坐标轴之间的距离
                                                  offset=5,
                                                  # 坐标轴X的值距离X轴的距离
                                                  axistick_opts=opts.AxisTickOpts(
                                                      is_inside=False
                                                      # 刻度线是否在内侧
                                                  ),
                                                  # 坐标轴刻度配置项
                                                  axisline_opts=opts.AxisLineOpts(
                                                      linestyle_opts=opts.LineStyleOpts(
                                                          width=3
                                                          ##设置宽度
                                                          ,
                                                          opacity=100
                                                          # 设置透明度
                                                          ,
                                                          type_='solid'
                                                          # 'solid', 'dashed', 'dotted'
                                                          ,
                                                          color='black')
                                                  )  # 坐标轴线的配置项
                                                  ,
                                                  axislabel_opts=opts.LabelOpts(
                                                      font_size=13
                                                      # 字的大小
                                                  )
                                                  ##坐标轴标签的格式配置
                                                  )
                         , yaxis_opts=opts.AxisOpts(
            name=name,
            name_location='middle',
            name_gap=30,
            name_textstyle_opts=opts.TextStyleOpts(
                font_family='Times New Roman',
                font_size=14,
                color='black',
                #                     font_weight='bolder',
            ),
            axistick_opts=opts.AxisTickOpts(
                #                     is_show=False,  # 是否显示
                is_inside=True,  # 刻度线是否在内侧
            ),
            axislabel_opts=opts.LabelOpts(
                font_size=12,
                font_family='Times New Roman',
            ),
        ))


def get_data():
    
    return {'Frame': frames, 'Overdraw': overdraws, 'Particles': particles}
