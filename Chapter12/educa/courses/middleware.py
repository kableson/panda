from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course


def subdomain_course_middleware(get_response):
    """
    为课程提供二级域名
    """

    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            # 通过指定的二级域名查询课程对象
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse('course_detail', args=[course.slug])
            # 将二级域名请求重定向至实际的URL
            url = '{}://{}{}'.format(request.scheme,
                                     '.'.join(host_parts[1:]), course_url)
            return redirect(url)
        response = get_response(request)
        return response
    return middleware
