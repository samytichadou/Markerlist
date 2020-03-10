import bpy

class MarkerList(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "marker.list"
    bl_label = "Marker List"

    @classmethod
    def poll(cls, context):
        return context.scene.timeline_markers
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
 
    def draw(self, context):
        scn = context.scene
        tool_settings = scn.tool_settings
        marker_list = scn.timeline_markers
        layout = self.layout
        
        col = layout.column(align=True)
        if scn.tool_settings.lock_markers: col.enabled = False
        else: col.enabled = True
            
        for k, marker in sorted(marker_list.items(), key=lambda it:it[1].frame):
            row = col.row(align=True)
            # go to frame
            if scn.frame_current == marker.frame: icon='RADIOBUT_ON'
            else: icon='RADIOBUT_OFF'
            op = row.operator('marker.go_to', text='', icon=icon, emboss=False)
            op.frame = marker.frame
            # name
            row.prop(marker, "name", text="")
            # selection
            if marker.select: icon = 'RESTRICT_SELECT_OFF'
            else: icon = 'RESTRICT_SELECT_ON'
            row.prop(marker, "select", text="", icon=icon)
            # frame
            row.prop(marker, "frame", text="")
            
            # delete
            op = row.operator('marker.remove', text='', icon='X')
            op.frame = marker.frame
            # camera
            if marker.camera: icon = 'VIEW_CAMERA'
            else: icon = 'CAMERA_DATA'
            row.label(text="", icon=icon)
            
        row = layout.row(align=True)
        row.prop(scn, 'frame_current', text='Frame')
        row.separator()
        op = row.operator('screen.marker_jump', text='', icon='TRIA_LEFT')
        op.next = False
        op = row.operator('screen.marker_jump', text='', icon='TRIA_RIGHT')
        op.next = True
        row.separator()
        if tool_settings.lock_markers: icon='LOCKED'
        else: icon='UNLOCKED'
        row.prop(tool_settings, 'lock_markers', text='', icon=icon)
        row.separator()
        row.operator('marker.remove_selected', text='Selected', icon='X')
        
    def execute(self, context):
        return {'FINISHED'}

def marker_list_function(self, context):
    self.layout.operator('marker.list')