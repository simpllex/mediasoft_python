def ask_question():
    fullname = input("Введите ФИО: ").lower()
    lang = input("Введите желаемую технологию: ").lower()
    sorry = "{}, к сожалению вы не подходите на вакансию {} в компанию Медиасофт".format(fullname, lang)
    congrats = "«{}, вы подходите на вакансию {} в компанию Медиасофт!»".format(fullname, lang)
    if lang == "python" or lang == "java":
        framework = input("Введите фреймворк: ").lower()
        if framework in db[lang]["framework"]:
            subd = input("Введите СУБД:").lower()
            if subd in db[lang]["subd"]:
                expirience = int(input("Введите свой опыт работы: "))
                if expirience >= db["expirience"]:
                    print(congrats)
                else:
                    print(sorry)
            else:
                print(sorry)
        else:
            print(sorry)
    else:
        print(sorry)          
    
db = dict(python = dict(subd =["postgres", "mysql"], framework = ["django", "flask"]), 
          java = dict(subd =["oracle", "mssql"], framework = ["spring", "spark"]),
          expirience = 5)
ask_question()

