from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='sss@t.com',
            profession='程序员',
            qq='333',
            phone='1333',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex = 1,
            email = 'nobody@dd.com',
            profession='程序员',
            qq = '333',
            phone='2323',
        )
        self.assertEqual(student.get_sex_display(),'男','性别字段内容与展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='333',
            phone='2323',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应只存在一个名称为{}记录'.format(name))

    def test_get_index(self):
        #测试首页可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200,'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='3333@dd.com',
            profession='程序员',
            qq='333',
            phone='2323',
            status=0,
        )
        response = client.post('/',data)
        obj = Student.objects.all()
        print(obj)
        print(response.status_code)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response = client.get('/')
        # print(response.content)
        self.assertTrue(b'test_for_post' in response.content,'response content must contain `test_for_post`')