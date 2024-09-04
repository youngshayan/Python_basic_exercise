def name(fname, lname, *args, **kwargs):
    print(f"Hello {fname}{lname}")
    print("args:",args)
    print("kwargs:",kwargs)
name('shayan', 'mansornia', 'karaj', 'reza', age = 23, height = 170)
