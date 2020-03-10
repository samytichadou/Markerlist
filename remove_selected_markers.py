import bpy

class RemoveSelectedMarker(bpy.types.Operator):
    """Remove selected Timeline Markers"""
    bl_idname = "marker.remove_selected"
    bl_label = "Remove Selected Marker"
    bl_options = {'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        for marker in context.scene.timeline_markers:
            if marker.select:
                return True

    def execute(self, context):
        scn = context.scene
        for marker in scn.timeline_markers:
            if marker.select:
                scn.timeline_markers.remove(marker)
        return {'FINISHED'}