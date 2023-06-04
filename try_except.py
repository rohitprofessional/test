#------------------------------------------------------------
a = 10

try:    # error occurs in this block
    y = a/0     # its zero in denominator
    print(y)    # this variable is not defined 
except ZeroDivisionError:   # error gets handled in this block
    print("zero error")

except NameError:
    print("variable is not defined")

# ------------------------------------------------------------

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# -------------------------------------------------------------

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# ----------------------------------------------------------------