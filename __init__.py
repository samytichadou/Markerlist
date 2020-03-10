'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou (tonton)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {  
 "name": "Marker List",  
 "author": "Samy Tichadou (tonton)",  
 "version": (1, 0),  
 "blender": (2, 82, 0),  
 "location": "Timeline",  
 "description": "Utilities to help with Timeline Markers handling",  
  "wiki_url": "https://github.com/samytichadou/fcurve_helper",  
 "tracker_url": "https://github.com/samytichadou/fcurve_helper/issues/new",  
 "category": "Animation"}


import bpy


# IMPORT SPECIFICS
##################################

from .go_to_marker import *
from .marker_list import *
from .remove_marker import *
from .remove_selected_markers import *



# register
##################################

classes = (GoToMarker,
            MarkerList,
            RemoveMarker,
            RemoveSelectedMarker,
            )

def register():

    ### OPERATORS ###
    from bpy.utils import register_class
    for cls in classes :
        register_class(cls)

def unregister():
    
    ### OPERATORS ###
    from bpy.utils import unregister_class
    for cls in reversed(classes) :
        unregister_class(cls)