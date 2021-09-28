print("Triple threat position")
print("Ты стоишь в тройной угрозе")
print("Выбери одно из действий:")
print("1. Пас на товарища\n2. Бросить самостоятельно\n3. Обыграть оппонента")
print()
step1=int(input("Вариант: "))
if step1==1:
    print("1. Пас на дугу\n2. Пас на кольцо")
    step2=int(input("\nВариант: "))
    if step2==1:
        print("\nТрех очковый бросок")
    elif step2==2:
        print("\nAlley-oop")
elif step1==2:
    print("1. Бросок с места\n2. Бросок с отклонением назад")
    step2=int(input("\nВариант: "))
    if step2==1:
        print("\nБросок заблокировали")
    elif step2==2:
        print("\nДвух очковый бросок от щита")
elif step1==3:
    print("1. Пройти с вращением\n2. Обманный бросок")
    step2=int(input("\nВариант: "))
    if step2==1:
        print("\nПерехват мяча")
    elif step2==2:
        print("\nПроход под кольцо и данк")