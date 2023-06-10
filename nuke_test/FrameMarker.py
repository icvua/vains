import nuke


class FrameMarker:
    def __init__(self):
        self.marker_node = nuke.createNode('NoOp')
        self.marker_node.addKnob(nuke.Int_Knob('marker'))
        self.marker_knob = self.marker_node.knob('marker')
        self.marker_knob.setVisible(False)

    def set_marker(self):
        self.marker_knob.setKeyAt(nuke.frame())

    def go_previous(self):
        pass

    def go_next(self):
        pass

    def clear_marker(self):
        pass
