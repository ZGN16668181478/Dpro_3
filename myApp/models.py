from django.db import models
from django.db.models import F,Q
# Create your models here.

class grades(models.Model):
    gObj = models.Manager()
    gId = models.IntegerField(primary_key=True)
    gNum = models.IntegerField()
    gName = models.CharField(max_length=30)
    gDate = models.DateTimeField()
    gIsDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'grades'
        ordering = ['gId']

# 定义一个管理类
class StudentsManager(models.Manager):
    # 通过管理类创建对象
    def createStudents(self,name,num,gender,date,grade,createtTime,alongTime,lastTime,delete=False):
        stu = self.model()
        stu.sName = name
        stu.sNum = num,
        stu.sGender = gender
        stu.sDate = date
        stu.sGrade = grade
        stu.sCreateTime = createtTime
        stu.sAlongTime = alongTime
        stu.sLastTime = lastTime
        stu.save()

    def get_queryset(self):
       return super(StudentsManager,self).get_queryset().filter(sName='linken')

class students(models.Model):
    stuObj = models.Manager()
    # 自定义管理器本来是models.Manager(),这里自定义管理类，直接实例化类就可以了
    stuObj2 = StudentsManager()
    sName = models.CharField(max_length=10)
    sNum = models.IntegerField()
    sGender = models.BooleanField()
    sDate = models.DateTimeField()
    sDelete = models.BooleanField(default=False)
    # 建立外键连接,这个连接就是修改的时候都会进行连接，然后通过连接对连接对象进行修改
    sGrade = models.ForeignKey(grades,on_delete=models.CASCADE)
    # 例如管理站点页面里调用时就会返回对象的sName，而不会是默认的对象名
    def __str__(self):
        return str(self.sName)
    sCreateTime = models.DateTimeField(auto_created=True)
    sAlongTime = models.DateTimeField(auto_now=True)
    sLastTime = models.DateTimeField(auto_now_add=True)
    # 创建元选项
    class Meta:
        db_table = 'students'
        ordering =['sDate']
    #创建一个类方法，通过调用这个类方法来进行对属性的添加，而不用通过shell命令来进行添加
    @classmethod         # 这里delete=False 只能放到最后才能使用:因为前面是元组，后面是字典
    def createStudents(cls,name,num,gender,date,grade,createtTime,alongTime,lastTime,delete=False):
        #这里是通过传入的参数，来和形参进行匹配，然后和数据库进行交互   所以是 sName = name
        stu = students(sName=name,sNum=num,sGender=gender,sDate=date,sGrade=grade,sCreateTime=createtTime,sAlongTime=alongTime,sLastTime=lastTime)
        return stu
    # 对于模型的简单小练习  copy
    def get(self,request,*args,**kwargs):
        filters =  request.GET
        # 找出符合customer的数据转成列表
        qs =  [Q(customer=request.user.customer)]
        try:
            if 'limit' in filters:
                limit = abs(int(filters['limit']))
                if limit > 49:
                    limit = 50
            else:
                limit = 10
            start_id = int(filters.get('start_id',0))
            # 添加符合start_id的对象
            qs.append(Q(id__gt=start_id))
            # 添加符合状态的state
            if 'state' in filters:
                qs.append(Q(state__in=filters['state']))
            else:
                qs.append(Q(state__in=[1,2,3,4]))
            # 添加符合title的数据
            if 'title' in filters:
              qs.append(Q(title__contains=filters['title']))
        except Exception:
            return "filters:过滤参数不合法！"
        # 通过*qs,对列表数据同时满足上述情况进行总的筛选，并设置限制集
        sets = Questionnaire.objects.filter(*qs)[:limit]