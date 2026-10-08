# Expert system
# Answer the follwing questionwith yes / no.
    #Do oyu have fever? : Yes / No
    #Do oyu have cough? : Yes / No
    #Do oyu have headach? : Yes / No


print("============== EXPERT SYSTEM ==============")
print("Answer the follwing questionwith yes / no.")
print("\n")

fever = input("Do oyu have fever? : ")
cough = input("Do oyu have cough? : ")
headach = input("Do oyu have headach? : ")

if fever == "no" and cough == "no" and headach == "no":
    print("You seem to be healthy.")

elif fever == "yes" and cough == "no" and headach == "no":
    print("You may have a mild infection.")

elif fever == "no" and cough == "yes" and headach == "no":
    print("You may have a Throat infection or mild cold.")

elif fever == "no" and cough == "no" and headach == "yes":
    print("You may have Stress, Migraine, or Fatigue.")

elif fever == "yes" and cough == "yes" and headach == "no":
    print("You may have Flu.")

elif fever == "yes" and cough == "no" and headach == "yes":
    print("You may have Viral Fever.")

elif fever == "no" and cough == "yes" and headach == "yes":
    print("You may have Commnon Cold.")

elif fever == "yes" and cough == "yes" and headach == "yes":
    print("You may have Flu or a Viral Infection.")

else:
    print("Invalid INPUT")
