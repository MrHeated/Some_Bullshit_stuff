print()
print('Deedle-deedle, answer my riddle!')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
correct = 0
incorrect = 0
first = 'python'
print()
first_answer = input("Как называется язык, который мы учим?: ")
print()
first_answer = first_answer.lower()
if first_answer == first:
    print('Отлично, это правильный ответ!')
    correct = correct + 1
else:
    print('Ты шо индеец?')
    incorrect = incorrect + 1
print()    
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print()
second = 'сибас'
second_answer = input('Как порусски называется рыба, которая какбэ намекаэ шо надо уходить/уезжать/улетать отсюда?: ')
print()
second_answer = second_answer.lower()
if second_answer == second:
	print('Вы выиграли трактор, заводите мотор!')
	correct = correct + 1
else:
	print('Вы наверное из Индианаполиса?')
	incorrect = incorrect + 1
print()	
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print()
third = str(25)
third_answer = input('Сколько будет 2 + 2 * 5 + 3 + 72 : 6 - 2?: ')
print()
if third_answer == third:
	print('Правильно!')
	correct = correct + 1
else:
    print('Подсказка: столько же, сколько и перьев в головном уборе твоего вождя.')
    incorrect = incorrect + 1
print()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')    
print()
fourth = 'gothic'
fourth_answer = input('Правильное название игры латинскими буквами, в которой главный герой попал за барьер?: ')
fourth_answer = fourth_answer.lower()
print()
if fourth_answer == fourth:
	print('Играть в эту игру было офигенски, правда?')
    #correct = correct + 1
else:
    print('Подсказка: там еще были древние храмы индейцев.')
    incorrect = incorrect + 1
print()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print()
fifth = 'стражи мертвых'
fifth_answer = input('Куарходрон из Яркендара: "К какой касте ты принадлежишь?": ')
fifth_answer = fifth_answer.lower()
if fifth_answer == fifth:
	print('Это помоему самый крутой диалог в дополнении.')
    #correct = correct + 1
else:
	print('Такое невозможно непомнить, там же офигенский диалог!')
    #incorrect = incorrect + 1
print()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print()	
print('Правильных ответов: ', correct)
print('Неправильных ответов: ', incorrect)
print()
if correct == 5:
	print('Вы выиграли афтамабиииль!!!!!')
if incorrect == 5:
	print('Не ну ты француз')
