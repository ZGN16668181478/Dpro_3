from django.contrib import admin
from .models import grades,students
# Register your models here.

class studentsInfo(admin.TabularInline):
    extra = 2
    model = students

@admin.register(grades)
class gradesAdmin(admin.ModelAdmin):
    # 设置关联
    inlines = [studentsInfo]
    # 修改显示页面
    list_display = ['gId','gName','gNum','gDate','gIsDelete']
    list_per_page = 2
    list_filter = ['gName']
    search_fields = ['gId']
    #修改添加页面内容
    fieldsets = [
        ('num',{'fields':['gId','gNum',]}),
        ('content',{'fields':['gName','gDate','gIsDelete']})
    ]
@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    # 更改False显示
    def notDelete(self):
        if self.sDelete:
            return '保存'
        else:
            return '删除'
    # 设置字段描述'
    notDelete.short_description = '是否删除'
    list_display = ['id','sGender', 'sName', 'sNum', 'sDate',notDelete,'sGrade_id']
    list_per_page = 2
    list_filter = ['sName']
    search_fields = ['id']
    # 设置动作位置
    actions_on_top = False
# 这里应该是默认在前面加了装饰器就会进行注册
admin.register(gradesAdmin,studentsAdmin)