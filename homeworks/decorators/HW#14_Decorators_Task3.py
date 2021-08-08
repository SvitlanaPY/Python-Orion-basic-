print("TASK3")
"""
3. def get_names_page(names_list):
        template_head = "<h3> User names: </h3>"
        template = "<p> {} </p>"

Допишіть дану функцію так, щоб коли на вхід приходить names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
функція повертала таку строку

<h3> User names: </h3>
<p> Misha </p>
<p> Olya </p>
<p> Vitaliy </p>
<p> Vita </p>

До даної функції напишіть декоратор який загорне отриману строку в div блок. style_class - це аргумент який приймається
декоратором, тобто декоратор або в 3 рівні, або функтор (краще зробіть через функтор)

<div class=*style_class*>
<h3> User names: </h3>
<p> Misha </p>
<p> Olya </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
"""


# (1) using 3-level decorator:
def div_block(style_class):
    def decor_in(get_names_page_):
        def inner(*args):
            # div_start = "<div class=" + style_class + ">\n"
            div_start = "<div class={}>\n".format(style_class)
            div_end = "\n</div>"
            return div_start + get_names_page_(*args) + div_end
        return inner
    return decor_in


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


# (2) using class:
class DivDecorator:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, get_names_page_):
        def inner(*args):
            # div_start = "<div class=" + style_class + ">\n"
            div_start = "<div class={}>\n".format(self.style_class)
            div_end = "\n</div>"
            return div_start + get_names_page_(*args) + div_end
        return inner


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
