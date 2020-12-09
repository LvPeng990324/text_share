from django.shortcuts import render, redirect
from .models import Text


def index(request):
    """
    展示主页方法
    :param request:
    :return:
    """
    # 取出所有文本信息
    # 从新到旧排序，将置顶条目提到前边
    texts = Text.objects.all().filter(is_deleted=False).order_by("-to_top", "-create_time")
    # 打包到前端
    context = {
        'texts': texts,
    }
    return render(request, 'index.html', context=context)


def text_detail(request, text_id):
    """
    展示文本详情方法
    :param request:
    :param text_id: 文本id
    :return:
    """
    # 取出text_id的文本信息
    text = Text.objects.get(id=text_id)
    # 打包到前端
    context = {
        'text': text,
    }
    return render(request, 'text_detail.html', context=context)


def create_text(request):
    """
    创建文本方法
    :param request:
    :return:
    """
    # 判断访问方法，看是访问页面还是提交数据
    if request.method == 'GET':
        return render(request, 'create_text.html')
    else:
        # 获取提交的数据
        title = request.POST.get('title')
        text = request.POST.get('text')

        # 创建文本
        Text.objects.create(
            title=title,
            text=text,
        )

        # 重定向主页
        return redirect('index')


def delete_text(request):
    """
    删除文本方法
    :param request:
    :return:
    """
    # 获取要删除的text_id
    text_id = request.POST.get('text_id')

    # 删除对应的text
    # Text.objects.get(id=text_id).delete()

    # 将对应text的is_deleted设置为True
    text = Text.objects.get(id=text_id)
    text.is_deleted = True
    text.save()

    # 重定向主页
    return redirect('index')


def top_text(request):
    """
    置顶文本方法
    :param request:
    :return:
    """
    # 获取要置顶的text_id
    text_id = request.POST.get('text_id')

    # 将对应text的to_top设置为True
    text = Text.objects.get(id=text_id)
    text.to_top = True
    text.save()

    # 重定向主页
    return redirect('index')


def no_top_text(request):
    """
    取消置顶文本方法
    :param request:
    :return:
    """
    # 获取要取消置顶的text_id
    text_id = request.POST.get('text_id')

    # 将对应text的to_top设置为False
    text = Text.objects.get(id=text_id)
    text.to_top = False
    text.save()

    # 重定向主页
    return redirect('index')
