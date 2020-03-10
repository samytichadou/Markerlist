import bpy

class GoToMarker(bpy.types.Operator):
    """Go to specific Timeline Marker frame"""
    bl_idname = "marker.go_to"
    bl_label = "Go to Marker"
    bl_options = {'INTERNAL', 'UNDO'}
    
    frame : bpy.props.IntProperty()

    @classmethod
    def poll(cls, context):
        return context.scene.timeline_markers

    def execute(self, context):
        context.scene.frame_current = self.frame
        return {'FINISHED'}