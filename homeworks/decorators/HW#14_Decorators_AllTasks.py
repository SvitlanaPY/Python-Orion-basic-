print("\nTASK1:")
def check_types(*args_d):
    def decor_in(summa_):
        def inner(*args_f):
            if len(args_d) == len(args_f) + 1:
                for i in range(len(args_f)):
                    if type(args_f[i]) != args_d[i]:   # not isinstance((args_f[i]), args_d[i])
                        raise Exception("WRONG TYPE for function's argument!!!")
                result = summa_(*args_f)
                if isinstance(result, args_d[-1]):
                    return result
                else:
                    raise Exception("Function should return float")
            else:
                raise Exception("Function should get 1 parameter less than decorator!!!")
        return inner
    return decor_in


@check_types(int, float, int, float)
def summa(*args_f):
    return sum(args_f)


print(summa(1, 2.2, 4), "- function returns float")


print("\nTASK2 (Те ж саме що й в TASK1, але через функтор):")
class WrongType(Exception):
    pass


class CheckTypes:
    def __init__(self, *args_d):
        self.args_d = args_d

    def __call__(self, summa_):
        def inner(*args_f):
            if len(self.args_d) == len(args_f) + 1:
                for i in range(len(args_f)):
                    if type(args_f[i]) != self.args_d[i]:   # not isinstance((args_f[i]), self.args_d[i])
                        raise WrongType
                result = summa_(*args_f)
                if isinstance(result, self.args_d[-1]):
                    return result
                else:
                    raise Exception("Function should return float")
            else:
                raise Exception("Function should get 1 parameter less than decorator!!!")
        return inner


@CheckTypes(int, float, int, float)
def summa(*args_f):
    result = sum(args_f)
    return result


print(summa(1, 2.2, 4), "- function returns float")


print("\nTASK3:")
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
    string_ = ''
    for i in names_list_:
        template_string = "\n<p> {} </p>".format(i)
        string_ = string_ + template_string
    return template_head + string_


names_list = ["Misha", "Olia", "Vitaliy", "Vita"]
print(get_names_page(names_list))


print("\nTASK4:")
class DivBlock:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, get_names_page_):
        def inner1(*args):
            div_start = "<div class={}>\n".format(self.style_class)
            div_end = "\n</div>"
            return div_start + get_names_page_(*args) + div_end
        return inner1


def body_block(get_names_page_):
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
@body_block
@DivBlock("*style_class*")
def get_names_page(names_list_):
    template_head = "<h3> User names: </h3>"
    string_ = ''
    for i in names_list_:
        template_string = "\n<p> {} </p>".format(i)
        string_ = string_ + template_string
    return template_head + string_


names_list = ["Misha", "Olia", "Vitaliy", "Vita"]
print(get_names_page(names_list))
