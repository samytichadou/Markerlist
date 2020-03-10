import bpy

class RemoveMarker(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "marker.remove"
    bl_label = "Remove Marker"
    bl_options = {'INTERNAL', 'UNDO'}
    
    frame : bpy.props.IntProperty()

    @classmethod
    def poll(cls, context):
        return context.scene.timeline_markers

    def execute(self, context):
        scn = context.scene
        for marker in scn.timeline_markers:
            if marker.frame == self.frame:
                scn.timeline_markers.remove(marker)
                break
        return {'FINISHED'}