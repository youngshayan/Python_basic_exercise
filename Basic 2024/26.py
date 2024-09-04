try: #  if this part doesn't work python will execute the except part
    print('')
# except:
#     print("Error")
except:
    raise KeyError("We have an error")
else:
    print("I''m from else")
finally:
    print("I'm from finally")