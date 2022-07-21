# -*- encoding: utf-8 -*-
"""
@File : series.py   
@Contact : 1175774748@qq.com
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/7/21 11:50 上午   yanou      1.0         None
"""
onesSeries = {
            "type": "line",
            "name": "Scene1/View1",
            "connectNulls": False,
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "symbolSize": 4,
            "showSymbol": True,
            "smooth": False,
            "clip": True,
            "step": False,
            "data": [
                [
                    "5",
                    200
                ]
            ],
            "hoverAnimation": True,
            "label": {
                "show": True,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "show": True,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "markPoint": {
                "label": {
                    "show": True,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                },
                "data": [
                    {
                        "name": "\u6700\u5927\u503c",
                        "type": "max"
                    },
                    {
                        "name": "\u6700\u5c0f\u503c",
                        "type": "min"
                    }
                ]
            },
            "markLine": {
                "silent": False,
                "precision": 2,
                "label": {
                    "show": True,
                    "position": "top",
                    "margin": 8
                },
                "data": [
                    {
                        "name": "\u5e73\u5747\u503c",
                        "type": "average"
                    }
                ]
            },
            "zlevel": 0,
            "z": 0
        }

