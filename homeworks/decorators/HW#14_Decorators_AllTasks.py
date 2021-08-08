print("\nTask1:")
print("\nTask2:")


print("\nTask3:")
def div_block(style_class):
    def decor(get_names_page_):
        def inner(*args):
            div_start = "<div class={}>\n".format(style_class)
            div_end = "\n</div>"
            return div_start + get_names_page_(*args) + div_end
        return inner
    return decor


@div_block("*style_class*")
def get_names_page(names_list_):
    template_head = "<h3> User names: </h3>"
    string_ = template_head
    for i in names_list_:
        template = "\n<p> {} </p>".format(i)
        string_ = string_ + template
    return string_


names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
print(get_names_page(names_list))


print("\nTask4:")
class DivDecorator:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, get_names_page_):
        def inner1(*args):
            div_start = "<div class={}>\n".format(self.style_class)
            div_end = "\n</div>"
            return div_start + get_names_page_(*args) + div_end
        return inner1


def body_decorator(get_names_page_):
    def inner2(*args):
        body_start = "<body>\n"
        body_end = "\n</body>"
        return body_start + get_names_page_(*args) + body_end
    return inner2


class HeadBlock:
    def __init__(self, title):
        self.title = title

    def __call__(self, get_names_page_):
        def inner3(*args):
            head_start = "<head>\n"
            title = "<title>{}</title>".format(self.title)
            head_end = "\n</head>\n"
            return head_start + title + head_end + get_names_page_(*args)
        return inner3


def html_block(get_names_page_):
    def inner4(*args):
        html_start = "<html>\n"
        html_end = "\n</html>"
        return html_start + get_names_page_(*args) + html_end
    return inner4


@html_block
@HeadBlock("*title*")
@body_decorator
@DivDecorator("*style_class*")
def get_names_page(names_list_):
    template_head = "<h3> User names: </h3>"
    string_ = template_head
    for i in names_list_:
        template = "\n<p> {} </p>".format(i)
        string_ = string_ + template
    return string_


names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
print(get_names_page(names_list))
