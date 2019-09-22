#!/usr/bin/env python3
from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path
path = Path.home() / ".jupyter" / "nbconfig"
rise = BaseJSONConfigManager(config_dir=str(path))
rise.update(
        "rise",
        {
            "transition": "none",
            "auto_select": "none",
            "scroll": False,
            "enable_chalkboard": True,
            "width": 1024,
            "height": 768,
            "chalkboard" : {
                "readOnly": False,
                "smallDefaultCursors": True,
                "rememberColor": [True, False],
                "theme": "chalkboard",
                "penWidth": 8,
                "chalkWidth": 9,
                "chalkEffect": 0.2,
                "eraserDiameter": 25,
            },
        }
        )

