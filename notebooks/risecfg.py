#!/usr/bin/env python3
from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path
path = Path.home() / ".jupyter" / "nbconfig"
cm = BaseJSONConfigManager(config_dir=str(path))
cm.update(
        "rise",
        {
            "transition": "none",
            "auto_select": "none",
            "scroll": False,
            "enable_chalkboard": True,
            "width": 1024,
            "height": 768,
        }
        )

