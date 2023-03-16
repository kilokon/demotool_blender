# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "demo_tool",
    "author" : "aviik",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Object"
}

import bpy

class CubesOperator(bpy.types.Operator):
    """Creates cubes on cubes"""
    
    bl_label = "Cube Multiplier"
    bl_idname = "object.cubes_operator"

    def execute(self, context):
#        ctx = 
#        print(ctx)

        for i in context.selected_objects:
            for j in i.data.vertices:
#                print(j.co)
                    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(j.co.x, j.co.y, j.co.z), scale=(1, 1, 1))
        return {'FINISHED'}
    


class AartiPanel(bpy.types.Panel):
    """Creates Panel for multiplier on cubes"""
    
    bl_label = "Cube Multiplier"
    bl_idname = "OBJECT_PT_cubes"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Cube Multiplier")

#        row = layout.row()
#        row.label(text="Active object is: " + obj.name)
#        row = layout.row()
#        row.prop(obj, "name")

        row = layout.row()
        row.operator("object.cubes_operator")
    
#def menu_func(self, context):
#    self.layout.operator(AartiOperator.bl_idname, text=AartiOperator.bl_label)



def register():
    bpy.utils.register_class(CubesOperator)
    bpy.utils.register_class(CubesPanel)
#    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(CubesOperator)
    bpy.utils.unregister_class(CubesPanel)
#    bpy.types.VIEW3D_MT_object.append(menu_func)
    
if __name__ == "__main__":
    register()