print("\nTask1")
print("\nTask2")
print("\nTask3")

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



print("\nTask4")
