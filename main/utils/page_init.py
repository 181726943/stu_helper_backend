"""
自定义分页组件
"""
from django.utils.safestring import mark_safe


class Page_init(object):

    def __init__(self, request, queryset, page_size=10, page_param="page"):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据给他进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数，例如：/etty/list/?page=12
        """
        self.page_param = page_param

        from django.http.request import QueryDict
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        current_page = request.GET.get(page_param, '1')
        if current_page.isdecimal():
            current_page = int(current_page)
        else:
            current_page = 1

        total_count = queryset.count()
        total_page, reminder = divmod(total_count, page_size)
        if reminder:
            total_page += 1
        self.total_page = total_page
        # 检查目标页面是是否合法
        if current_page > self.total_page:
            self.current_page = self.total_page
        self.current_page = current_page

        self.page_size = page_size  # 每页显示的数据条数
        self.start = (current_page - 1) * page_size
        self.end = current_page * page_size

        # 每页显示的数据
        self.page_queryset = queryset[self.start: self.end]

    def html(self):
        # 页码
        page_list = []

        # 首页
        self.query_dict.setlist(self.page_param, [1])
        first_page = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(first_page)

        # 上一页
        if self.current_page > 1:
            self.query_dict.setlist(self.page_param, [self.current_page - 1])
            pre_page = '<li><a href="?{}">«</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            pre_page = '<li class="previous disabled"><a href="?{}">«</a></li>'.format(self.query_dict.urlencode())

        page_list.append(pre_page)

        for i in range(1, self.total_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.current_page:
                element = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                element = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_list.append(element)

        # 不分页
        # grade_list = models.Score.objects.filter(**data_dict)

        # 下一页
        if self.current_page < self.total_page:
            self.query_dict.setlist(self.page_param, [self.current_page + 1])
            next_page = '<li><a href="?{}">»</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page])
            next_page = '<li class="previous disabled"><a href="?{}">»</a></li>'.format(self.query_dict.urlencode())
        page_list.append(next_page)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page])
        last_page = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(last_page)

        # 页面直达
        # search_page = """
        #     <li>
        #         <form style="float: left;margin-left: -1px" method="get">
        #             <input name="page"
        #                    style="position: relative;float:left;display: inline-block;width: 80px;border-radius: 0;"
        #                    type="text" class="form-control" placeholder="页码" value={{ current_page }}>
        #                 <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
        #         </form>
        #     </li>
        #     """
        # page_list.append(search_page)

        grade_page = mark_safe("".join(page_list))
        return grade_page
