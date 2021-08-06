print("\nTask1")
print("\nTask2")
print("\nTask3")


def decorator3(get_names_page_):
    def inner(names_list_):
        div_start = "<div class=*style_class*>\n"
        div_end = "\n</div>"
        return div_start + get_names_page_(names_list_) + div_end
    return inner


@decorator3
def get_names_page(names_list_):
    template_head = "<h3> User names: </h3>"
    string_ = template_head
    for i in names_list_:
        template = "\n<p> {} </p>".format(i)
        string_ = string_ + template
    return string_


names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
print(get_names_page(names_list))


print("\nTask4")
