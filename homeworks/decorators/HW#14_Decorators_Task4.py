print("TASK4:")
"""
4. Допишіть ще один декоратор, який загорне результат роботи з попереднього завдання в теги <body> </body>.
Щоб отримати ось такий код

<body>
<div class=*style_class*>
<h3> User names: </h3>
<p> Misha </p>
<p> Olia </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
</body>

ще один декоратор який приклеїть до існуючого куска html - head блок, де *title* це аргумент що отримується декоратором

<head>
<title>*title*</title>
</head>
<body>
<div class=*style_class*>
<h3> User names: </h3>
<p> Misha </p>
<p> Olia </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
</body>

Ще один декоратор який загорне все що є в <html> </html> теги

<html>
<head>
<title>*title*</title>
</head>
<body>
<div class=*style_class*>
<h3> User names: </h3>
<p> Misha </p>
<p> Olia </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
</body>
</html>

Зверніть увагу що у вас на одну функцію повинно назначатись 4 декоратори, тому потрібно не тільки їх написати, а й
вибрати правильний порядок декорування щоб після всіх декорацій отримати наприклад ось такий html
Також деякі декоратори доцільно буде робити через функції в "2 рівні", деякі в "3 рівні", деякі через функтори

<html>
<head>
<title>Users</title>
</head>
<body>
<div class=users_block>
<h3> User names: </h3>
<p> Misha </p>
<p> Olia </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
</body>
</html>
"""


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
