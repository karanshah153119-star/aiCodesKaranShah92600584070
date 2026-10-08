print("==============================")
print("    CAREER GUIDENCE SYSTEM    ")
print("==============================")

print("Answer the following question with yes or no.")
print("\n")

coding = str(input("Do You Linke Coding (Y/N): "))
math = str(input("Do You Linke Mathematics (Y/N): "))
bio = str(input("Do You Linke Biology (Y/N): "))
drw = str(input("Do You Linke Drawing (Y/N): "))
print("\n")

print("==========Career Suggestion ==========")
print("\n")

if coding == "n" and math == "n" and bio == "n" and drw == "n":
    print("Suggestion Career : Explore your interst and career options further.")

elif coding == "n" and math == "n" and bio == "n" and drw == "y":
    print("Suggestion Career : Graphic Desiger / Animator.")

elif coding == "n" and math == "n" and bio == "y" and drw == "n":
    print("Suggestion Career : Pharmacist / Nurse.")

elif coding == "n" and math == "n" and bio == "y" and drw == "y":
    print("Suggestion Career : Medical illustrator / Healthcare Education.")

elif coding == "n" and math == "y" and bio == "n" and drw == "n":
    print("Suggestion Career : Engineer / Data Analyst.")

elif coding == "n" and math == "y" and bio == "n" and drw == "y":
    print("Suggestion Career : Architect.")

elif coding == "n" and math == "y" and bio == "y" and drw == "n":
    print("Suggestion Career : Doctor.")

elif coding == "n" and math == "y" and bio == "y" and drw == "y":
    print("Suggestion Career : Medical illustrator / Biomedical Designer.")

elif coding == "y" and math == "n" and bio == "n" and drw == "n":
    print("Suggestion Career : Programmer / Web Devloper.")

elif coding == "y" and math == "n" and bio == "n" and drw == "y":
    print("Suggestion Career : Web Designer / UI-UX Designer.")

elif coding == "y" and math == "n" and bio == "y" and drw == "n":
    print("Suggestion Career : Health App Devloper.")

elif coding == "y" and math == "n" and bio == "y" and drw == "y":
    print("Suggestion Career : Medical illustrator.")

elif coding == "y" and math == "y" and bio == "n" and drw == "n":
    print("Suggestion Career : Software Engineer / Computer Scients")

elif coding == "y" and math == "y" and bio == "n" and drw == "y":
    print("Suggestion Career : Game devloper / UI Engineer.")

elif coding == "y" and math == "y" and bio == "y" and drw == "n":
    print("Suggestion Career : Bioformatics Scientist.")

elif coding == "y" and math == "y" and bio == "y" and drw == "y":
    print("Suggestion Career : Biomedical Software Engineer / Medical Technology Specialist.")

else:
    print("Invalid Input.")

print("\n")
print("Thank you for using the career gudidance export system!")
