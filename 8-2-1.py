import pathlib
p = pathlib.path('.')
for pf in p.iterdir():
    if pf.is_file():
        print(str(pf))
        