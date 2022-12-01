  def menu1():
  print('')
  def f():
    ball=0
    question=["Столица Бургундии?","Кто победил в Столетней войне?","Когда ДР у Елены Леонидовны Архиповой?","Сколько ИСтрибителей ТИпА ЗИИИро?","Сколько букв в русском языке?"]
    answer=["Дижон","Франция","30 ноября","Тигр","33"]
    for i in range(len(question)):
      print(question[i])
      answer1=input('Ответ:')
      if answer1==answer[i]:
        print("ПРАВИЛЬНА")
        ball=ball+100
      else:
        print("НЕПРАВИЛЬНА")
    print("Вы набрали: "+str(ball)+" баллов.")
    povtor=str(input("Желаете повторить:да/нет"))
    if povtor=="да":
      menu1()
  f()
