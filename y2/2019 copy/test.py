import urwid



def add_customer(button, choice):
    response = urwid.Text(['Add customer', '\n'])
    name = urwid.Edit("Customer name? >\n")
    address = urwid.Edit("Customer address? >\n")
    phone = urwid.Edit("Customer phone? >\n")
    
    done = urwid.Button('Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([
        response,
        name,
        address,
        phone,
        urwid.AttrMap(done, None, focus_map='reversed')
    ]))

def item_chosen(button, choice):
    response = urwid.Text(['You chose ', choice, '\n'])
    done = urwid.Button('Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

choices = [
    ["Add a customer", add_customer],
    ["View all customers", item_chosen],
    ["Add order", item_chosen],
    ["View all orders", item_chosen],
    ["Print Bill", item_chosen],
    ["Exit", item_chosen]
]

palette = [
    ('reversed', 'standout', ''),
    ('banner', 'black', 'light gray'),
    ('bg', 'black', 'dark blue'),
    ('text', 'white', 'black')
]


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c[0])
        urwid.connect_signal(button, 'click', c[1], c[0])
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))



def exit_program(button: urwid.Button):
    main.original_widget  = urwid.Padding(menu('Pizza Company', choices), left=2, right=2)

main = urwid.Padding(menu('Pizza Company', choices), left=2, right=2)
map1 = urwid.AttrMap(main, 'banner')
top = urwid.Overlay(map1, urwid.SolidFill(' '),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
map2 = urwid.AttrMap(top, 'bg')
urwid.MainLoop(map2, palette=palette).run()
