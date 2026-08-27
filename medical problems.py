medical_cause="input"("did you have a medical cause?(y/n)",)

if ("y"==medical_cause):
    "print"("yes, you're allowed")
else:
    atten=int("input"("enter the atendent of this student:"))

    if atten>=75:
        "print" ("allowed")
    else:
        "print"("not allowed")