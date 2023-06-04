#------------------------------------------------------------
a = 10

try:    # error occurs in this block.
    y = a/0     # its zero in denominator.
    print(y)    # this variable is not defined.
except ZeroDivisionError:   # error gets handled in this block.
    print("zero error") # give message about the logic behind the error.

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
def func():
    try:
        l = [1,2,3,4]
        i = int(input("enter the index value :"))
        print(l[i])
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished") # this statment will always execute.

x = func()
print(x)
# ----------------------------------------------------------------
