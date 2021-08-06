print("\nTask1")
"""
1. Дану задачу робити через декоратор як функції!
Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
Приклад:
@decor(int, float, int, float)
def func(1, 1.2, 4)
Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
функція повертає
можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується
"""


print("\nTask2")
"""
2. Те ж саме що й в завданні 1, але зробити через функтор
"""



print("\nTask3")
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
def decor(get_names_page_):
    def inner(names_list_):
        div_start = "<div class=*style_class*>\n"
        div_end = "\n</div>"
        return div_start + get_names_page_(names_list_) + div_end
    return inner

@decor
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
"""
4. Допишіть ще один декоратор, який загорне результат роботи з попереднього завдання в теги <body> </body>.
Щоб отримати ось такий код

<body>
<div class=*style_class*>
<h3> User names: </h3>
<p> Misha </p>
<p> Olya </p>
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
<p> Olya </p>
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
<p> Olya </p>
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
<p> Olya </p>
<p> Vitaliy </p>
<p> Vita </p>
</div>
</body>
</html>
"""