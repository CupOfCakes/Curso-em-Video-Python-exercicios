print("=" * 6 + "CLASSE DE NATAÇÃO" + "=" * 6)
idade = int(input("qual e a sua idade? "))

if idade <= 9:
    print("vc e classe \33[36mMIRIM\33[m")
elif idade <= 14:
    print("vc e classe \33[36mINFANTIL\33[m")
elif idade <= 19:
    print("vc e classe \33[36mJUNIOR\33[m")
elif idade <= 25:
    print("vc e classe \33[36mSÊNIOR\33[m")
else:
    print("vc e classe \33[36mMESTRE\33[m")
