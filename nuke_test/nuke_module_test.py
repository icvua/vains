import os
os.environ["NUKE_INTERACTIVE"] = "1"

import nuke

nuke.scriptOpen(r"C:\Users\Elsholtzia\test.nk")
con = nuke.nodes.Constant()
con['color'].setValue(0.5)

nuke.scriptSaveAs(r"C:\Users\Elsholtzia\test5.nk")
