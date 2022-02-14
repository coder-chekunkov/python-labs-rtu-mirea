### 👨‍🎓Практические задания по дисциплине: "Интерпретируемый язык программирования высокого уровня". РТУ МИРЭА.

Данные практические работы проводились в рамках дисципилны "Интерпретируемый язык программирования высокого уровня" в 2-ом семестре 2-ого курса. <br/>
Дисциплина была защищена на оценку: " ".

---

<a name="contents">**Оглавление.**</a>

- [Практика №1:](#practice1)
  - [1.1 "Бит или не бит?"](#1.1)
  - [1.2 "Регистрация почты"](#1.2)
  - [1.3 "Калькулятор"](#1.3)
  - [1.4 "Сколько строк?"](#1.4)
  - [1.5 "Среднее"](#1.5)
  - [1.6 "Остров невезения"](#1.6)
  - [1.7 "Обратный отсчет"](#1.7)
  - [1.8 "Найди кота"](#1.8)
  - [1.9 "Таблица деления"](#1.9)
- [Практика №2:](#practice2) 
  - [2.1 "Книги на лето"](#2.1)
  - [2.2 "Какая-то там бумага"](#2.2)
  - [2.3 "Розенкранц и Гильденстерн меняют профессию"](#2.3)
  - [2.4 "Белый список"](#2.4)
  - [2.5 "Напёрстки"](#2.5)
  - [2.6 "Маяковский"](#2.6)
  - [2.7 "Гэдсби"](#2.7)
  - [2.8 "CSV 2.0"](#2.8)
  - [2.9 "Транслитерация"](#2.9)
- [Практика №3:](#practice3) 
  - [3.1 "Скажи «пароль» и проходи"](#3.1)
  - [3.2 "Месяц/Month"](#3.2)
  - [3.3 "Счастливый пассажир"](#3.3)
  - [3.4 "Числа в строке"](#3.4)
  - [3.5 "Цезарь"](#3.5)
  - [3.6 "Мимикрия"](#3.6)
  - [3.7 "Есть ли 0"](#3.7)


    
---

<a name="practice1"></a>

<a name="1.1"> </a>

**1.1 "Бит или не бит?"**

:unlock: Выполнение: ✔️

Из разговора двух программистов: <br/>
– Ну вот представь, что у тебя есть 1000 рублей... <br/>
– Не-е-е, давай уж округлим... пусть у меня есть 1024 рубля.

Этот программистский анекдот шокирует людей, далеких от компьютерной тематики. Действительно, довольно сложно понять почему число 1024 круглое? Все дело в том, что компьютер работает с двоичной системой счисления, а 1024 в двоичном коде - это единица с десятью нулями: 10000000000, для компьютера оно круглое. Именно поэтому производные единицы измерения в информатике связаны не с 1000, как это принято (1 кг = 1000 гр, 1 км = 1000 м и т.д.), а с числом 1024.
Организуйте вывод памятки для начинающего программиста. Для вывода 5-ой строки выполните расчет и подставьте необходимое число вместо ХХХХ.

*Формат вывода* <br/>
Заполненная памятка из 5 строк.

| Ввод | Вывод |
|:----:|:----|
| - | 1 бит - минимальная единица количества информации. <br/> 1 байт = 8 бит. <br/> 1 Килобит = 1024 бита. <br/> 1 Килобайт = 1024 байта. <br/> 1 Килобайт = ХХХХ бит.|

:pushpin: [Оглавление.](#contents)

<a name="1.2"> </a>

**1.2 "Регистрация почты"**

:unlock: Выполнение: ✔️

При регистрации нового ящика электронной почты пользователя обычно просят ввести, помимо прочего, желаемый логин, а также резервный адрес электронной почты (на случай, если понадобится восстановить забытый пароль). Напишите программу, которая проверяет, что пользователь ничего не перепутал и ввёл корректный логин (не содержащий символ «@») и корректный резервный адрес (содержащий символ «@»). Иных проверок, кроме указанных здесь, выполнять не надо.

*Формат ввода* <br/>
Вводятся две строки: предлагаемые пользователем логин и резервный адрес. 

*Формат вывода* <br/>
Выводится одна строка: если все условия выполнены, то выводится «OK» (латиницей); если в логине присутствует «@», то выводится «Некорректный логин»; если логин корректный, но в адресе отсутствует «@», то выводится «Некорректный адрес».

*Пример* <br/>
| Ввод | Вывод |
|:----|:----:|
| S.L.Jackson <br/> MEGAKILLER@example,com | OK |

:pushpin: [Оглавление.](#contents)

<a name="1.3"> </a>

**1.3 Калькулятор**

:unlock: Выполнение: ✔️

Напишите программу, которая считывает с клавиатуры одно за другим два дробных числа, а затем строку. Если эта строка является обозначением одной из четырёх основных математических операций (+, -, * или /), то выведите результат применения этой операции к введенным ранее числам, в противном случае выведите «888888». Также «888888» следует вывести, если пользователь захочет поделить на ноль.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
|9 <br/> 4.2 <br/> - | 4.8 |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
|4 <br/> 6 <br/> minus | 888888 |

:pushpin: [Оглавление.](#contents)

<a name="1.4"> </a>

**1.4 Сколько строк?**

:unlock: Выполнение: ✔️

Программа-психотерапевт. Пользователь говорит, программа ничего не отвечает. Когда пользователь закончил говорить, он говорит "Спасибо.". После этого программа выводит общее количество введённых строк.

*Формат ввода* <br/>
Несколько строк, последняя из которых — "Спасибо."

*Формат вывода* <br/>
Одно целое число — общее количество введённых строк.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
|Здравствуйте. <br/> Мне в последнее время всё надоело. <br/> В школе учителя вредные, дети противные... <br/> Очень надоело. <br/> Я, кстати, директор. <br/> Уф. Выговорился. Полегчало. <br/> Спасибо. | 7 |

:pushpin: [Оглавление.](#contents)

<a name="1.5"> </a>

**1.5 Среднее**

:unlock: Выполнение: ✔️

Несколько дней подряд метеоролог измеряет температуру воздуха в своём городе. Ваша программа считывает измеренные им значения и выводит среднее значение температуры за время измерений. Чтобы обозначить конец ввода данных, вводится значение, меньшее -300 (реальная температура не может быть ниже -273.15).

При проведении вычислений с действительными числами ответ может незначительно отличаться от математически правильного из-за погрешностей округления; это не повлияет на проверку решения.

*Формат ввода* <br/>
Несколько (не меньше одного) действительных чисел на отдельных строках — температура воздуха в разные дни. <br/>
Действительное число, меньшее -300.

*Формат вывода* <br/>
Одно действительное число — средняя температура воздуха.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| 22.3 <br/> 24.1 <br/> 24.0 <br/> 24.4 <br/> -301 | 23.7 |

:pushpin: [Оглавление.](#contents)

<a name="1.6"> </a>

**1.6 Остров невезения**

:unlock: Выполнение: ✔️

Где-то по среди океана есть тихий и прекрасный остров Яшорты. Казалось бы, что может быть прекраснее южного солнца, белоснежных пляжей, экзотических цветов и птиц всех цветов радуги? Но вот дела у местных жителей идут не очень: крокодил не ловится, кокос не растет. Один из старейшин предположил: «Наверное, нас мама родила в понедельник!». Но проверить эту гипотезу оказалось непросто, потому что календаря на острове никто никогда не видал. Долго длились поиски решения, и вот местному шаману предки подсказли заветную формулу (которая на самом деле работает!):

`d + ((13*m - 1) / / 5 ) + y + (y / /4 + c / / 4 - 2*c + 777)`,

где d — число месяца, m — номер месяца, если начинать счет с марта, как это делали в Древнем Риме (март — 1, апрель — 2, ..., февраль — 12), y — номер года в столетии, c — количество столетий.

Если потом вычислить остаток от деления на 7, то мы получим день недели: 1 — понедельник, 2 — вторник, ..., 6 — суббота, 0 — воскресенье.

Помогите местным жителям написать программу, чтобы каждый из жителей мог прийти, ввести день, месяц и год своего рождения и узнать день недели чтобы проверить, действительно ли он невезучий.

*Формат ввода* <br/>
Три строки: день, месяц и год рождения аборигена.

*Формат вывода* <br/>
Число - день недели, в который родился абориген (1 — понедельник, 2 — вторник, ..., 6 — суббота, 0 — воскресенье).

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| 1 <br/> 9 <br/> 2000 | 5 |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| 12 <br/> 9 <br/> 2012 | 3 |

*Примечание*<br/>
Обратите внимание, что во входных данных номер месяца вводится так, как это принято у нас сейчас (январь - 1, февраль - 2 и т.д.)

:pushpin: [Оглавление.](#contents)

<a name="1.7"> </a>

**1.7 Обратный отсчет**

:unlock: Выполнение: ✔️

Любопытно, что впервые обратный отсчёт перед запуском ракеты был использован в немом научно-фантастическом фильме «Женщина на Луне». Драматический приём оказался настолько удачным, что прижился в реальной практике космонавтики.

Напишите программу, которая ведёт обратный отсчёт.

*Формат ввода* <br/>
Вводится одно целое число n — количество секунд, оставшееся до запуска.

*Формат вывода* <br/>
Для каждой секунды от n-й до нулевой последовательно выведите: «Осталось секунд: <количество оставшихся секунд>». После этого выведите: «Пуск». <br/>
Если n<0, то это значит, что с пуском мы опаздываем: в этом случае выводите «Пуск» немедленно, не тратя времени на обратный отсчёт.

*Пример* <br/>
| Ввод | Вывод |
|:----:|----|
| 5 | Осталось секунд: 5 <br/> Осталось секунд: 4 <br/> Осталось секунд: 3 <br/> Осталось секунд: 2 <br/> Осталось секунд: 1 <br/> Осталось секунд: 0 <br/> Пуск |

:pushpin: [Оглавление.](#contents)

<a name="1.8"> </a>

**1.8 Найди кота**

:unlock: Выполнение: ✔️

Напишите программу, которая находит кота. Пользователь вводит сначала количество строк, потом сами строки. Если хотя бы в одной введённой строке нашлось сочетание букв «Кот» или «кот», программа выводит «МЯУ», иначе программа выводит «НЕТ».

*Формат ввода* <br/>
В первой строке записано число n. <br/> 
Далее следует n строк.

*Формат вывода* <br/>
Напечатайте нужное сообщение в зависимости от того, есть во введенных строчках кот или нет.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| 4 <br/> Как устроен типичный фрукт: <br/> кожура; <br/> мякоть; <br/> косточки. | МЯУ |

:pushpin: [Оглавление.](#contents)

<a name="1.9"> </a>

**1.9 Таблица деления**

:unlock: Выполнение: ✔️

Почему столько внимания уделяется таблице умножения? Других арифметических операций не бывает, что ли? <br/>
Выведите таблицу деления заданных размеров.

*Формат ввода* <br/>
На первой строке вводится число колонок в таблице. <br/>
На второй строке вводится число строк в таблице.

*Формат вывода* <br/>
Выводится указанное число строк. В каждой строке выводятся разделённые символами пустого пространства частные: номер колонки, делённый на номер строки. Нумерация колонок и строк начинается с 1.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| 3 <br/> 2 | 1.0 2.0 3.0 <br/> 0.5 1.0 1.5 |

*Примечание* <br/>
При работе с вещественными числами может возникнуть проблема точности вычислений, хотя для этой задачи она и не столь важна. 

:pushpin: [Оглавление.](#contents)

---

<a name="practice2"></a>

<a name="2.1"> </a>

**2.1 "Книги на лето"**

:unlock: Выполнение: :x:

Алексей получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть, а каких нет. К счастью, у Алексея на компьютере есть текстовый документ, в котором записаны все книги из его домашней библиотеки в случайном порядке. Определите, какие книги из списка на лето есть у Алексея, а каких нет.

*Формат ввода* <br/>
В первой строке записано число M — число книг в домашней библиотеке. Во второй строке записано число N - число книг в списке на лето. В домашней библиотеке и списке книг есть хотя бы по одной книге (M ≥ 1 и N ≥ 1). Далее идут M строчек с названиями книг из домашней библиотеки и N строчек названий из списка на лето. Гарантируется, что все слова в названиях книг разделены одним пробелом, а после последнего слова сразу идёт перевод строки (т. е. нет «невидимых» пробелов).

*Формат вывода* <br/>
Выходные данные: N строчек, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| 4 <br/> 2 <br/> Хоббит <br/> Алиса в стране чудес <br/> Том Сойер <br/> Остров сокровищ <br/> Том Сойер <br/> Властелин Колец | YES <br/> NO |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| 4 <br/> 4 <br/> Хоббит <br/> Алиса в стране чудес <br/> Том Сойер <br/> Остров сокровищ <br/> Буратино <br/> Хоббит <br/>  Остров сокровищ <br/> Война и мир| NO <br/> YES <br/> YES <br/> NO |

:pushpin: [Оглавление.](#contents)

<a name="2.2"> </a>

**2.2 "Какая-то там книга"**

:unlock: Выполнение: :x:

Напишите программу, которая считывает сообщение, затем номер. После этого программа выводит букву из сообщения с таким номером, причём считается, что номера букв отсчитываются с единицы. <br/>
Если введённое число не является правильным номером буквы, вывести «ОШИБКА».

*Формат ввода* <br/>
В первой строке записано сообщение, во второй — номер буквы.

*Формат вывода* <br/>
Одна буква или сообщение «ОШИБКА».

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| привет <br/> 2 | р |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| привет <br/> -100 | Ошибка |

:pushpin: [Оглавление.](#contents)

<a name="2.3"> </a>

**2.3 "Розенкранц и Гильденстерн меняют профессию"**

:unlock: Выполнение: :x:

Второстепенные герои пьесы Шекспира «Гамлет» Розенкранц и Гильденстерн появляются и в пьесе Тома Стоппарда. <br/>
Они подбрасывают монетку, и Гильденстерна интересует, какое максимальное количество орлов подряд может выпасть. (Розенкранца это не интересует.)

Вводится одна строка, каждая буква которой представляет собой результат одного броска монетки — «о» обозначает орла, «р» обозначает решку. Программа должна вывести максимальное количество орлов, выпавших подряд.

*Формат ввода* <br/>
Одна строка, состоящая из букв «о» и «р» — результаты бросков.

*Формат вывода* <br/>
Одно целое число — максимальное число орлов, выпавших подряд.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| рооррооор | 3 |

:pushpin: [Оглавление.](#contents)

<a name="2.4"> </a>

**2.4 "Белый список"**

:unlock: Выполнение: :x:

Напишите жёсткий фильтр поисковых запросов для интернета в школе, который пропускает лишь те запросы, которые есть в «белом списке».

*Формат ввода* <br/>
На первой строке вводится количество пунктов «белого списка». <br/>
Затем — сами пункты «белого списка». <br/>
На отдельной строке — количество запросов, которые нужно проанализировать. <br/> 
Затем — сами запросы. <br/>

*Формат вывода* <br/>
Те запросы из введённых, которые есть в «белом списке».

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| 3 <br/> учебники <br/> котики <br/> почта <br/> 4 <br/> сериалы <br/> котики <br/> мемы <br/> учебники <br/>| котики <br/> учебники |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| 1 <br/> учебники <br/> 4 <br/> учебники <br/> скачать бесплатно реферат <br/> как обойти фильтр поисковых запросов <br/> учебники | учебники <br/> учебники |

:pushpin: [Оглавление.](#contents)

<a name="2.5"> </a>

**2.5 "Напёрстки"**

:unlock: Выполнение: :x:

Напёрсточник кладёт под каждый из напёрстков какую-нибудь мелочь, несколько раз переставляет напёрстки на столе, при этом некоторые напёрстки он убирает со стола. Определите, что под напёрстками, оставшимися в итоге на столе.

*Формат ввода* <br/>
На первой строке вводится натуральное число n0 — изначальное количество напёрстков. <br/>
Далее следуют n текстовых строк, описывающих, что положено под напёрстки с 1-го по n0-й. <br/>
На следующей строке вводится натуральное число k — количество перестановок напёрстков. <br/>

Далее следуют k групп строк, описывающих перестановки. Каждая группа устроена следующим образом. Пусть после предыдущей перестановки на столе осталось niнапёрстков в определённом порядке. Пронумеруем их с 1-го по ni-й (эта нумерация может не совпадать с исходной). Сначала на отдельной строке указывается количество напёрстков, которое останется на столе после данной перестановки — ni+1(гарантируется, что ni+1≤ ni). Затем следует ni+1 строк, содержащих различные номера напёрстков от 1 до ni; эти строки показывают, какие напёрстки и в каком порядке окажутся на столе после перестановки.

Например, в приведённом примере производится две перестановки: после первой на столе остаются все три исходных напёрстка, но в порядке 3, 2, 1, то есть: жук, монета, стеклянный шарик; после второй перестановки на столе остаются только два напёрстка, первый и второй.

*Формат вывода* <br/>
Выводится список предметов под напёрстками, оставшимися на столе, в том порядке, в каком лежат напёрстки.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| 3 <br/> стелкянный шарик <br/> монета <br/> жук <br/> 2 <br/> 3 <br/> 3 <br/> 2 <br/> 1 <br/> 2 <br/> 1 <br/> 2| жук <br/> монета |

:pushpin: [Оглавление.](#contents)

<a name="2.6"> </a>

**2.6 "Маяковский"**

:unlock: Выполнение: :x:

Напишите программу, которая выводит слова введённой строки (части, разделённые символами пустого пространства) в столбик. Нужно обойтись без явного использования циклов и списочных выражений, в программе должен быть всего один вызов print.

*Формат ввода* <br/>
Слова, каждое на отдельной строке.

*Формат вывода* <br/>
Слова, каждое на отдельной строке.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
|И волны клянутся всеводному Цику оружие бурь до победы не класть.| И <br/> волны <br/> клянутся <br/> всеводному <br/> Цику <br/> оружие <br/> бурь <br/> до <br/> победы <br/> не <br/>  класть. |

:pushpin: [Оглавление.](#contents)

<a name="2.7"> </a>

**2.7 "Гэтсби"**

:unlock: Выполнение: :x:

Предположим, вы — Эрнст Винсент Райт, и вы пишете очередной литературный эксперимент: роман, в котором вообще не используется какая-нибудь одна буква (как в вашем романе “Gadsby” ни разу не использовалась буква “e”, что, как говорят, осталось незамеченным редакторами). Будет полезно иметь программу, которая укажет, в каких словах вы, забывшись, всё-таки употребили эту букву.

*Формат ввода* <br/>
На первой строке вводится один символ — строчная буква. <br/> 
На второй строке вводится предложение.

*Формат вывода* <br/>
Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
|m <br/> Mary had a little lamb.| Mary <br/> lamb. |

:pushpin: [Оглавление.](#contents)

<a name="2.8"> </a>

**2.8 "CSV 2.0"**

:unlock: Выполнение: :x:

Один из простейших форматов таблиц — CSV, что значит Comma-Separated Values, т. е. «значения, разделённые запятыми». В самом деле, в этом текстовом формате каждому ряду таблицы соответствует строка текста, а значения в ячейках одного ряда разделяются запятыми.

Придумайте такую модификацию формата CSV, описанного выше, чтобы значения в ячейках таблицы могли содержать запятые и символы перехода на новую строку. Вспомните, как подобную проблему решили в Питоне. Решите задачу CSV и для своего улучшенного формата. Подробное описание своего формата изложите в комментариях.

Напишите программу, которая считывает таблицу в формате CSV, в том числе с запятыми и символами перехода на новую строку в вашем улучшенном формате, а затем выводит отдельные её элементы.

*Формат ввода* <br/>
На первой строке указано одно натуральное число R — число рядов таблицы. <br/>
Далее следуют R строк, представляющие ряды таблицы. <br/>
Далее следует одно натуральное число N — число элементов таблицы, которые нужно будет вывести. <br/>
Далее следует N строк, на которых приведены разделённые запятой координаты элементов таблицы (номер строки и номер столбца, нумерация с нуля). <br/>
(Запятые в примере расставлены не по правилам пунктуации.)

Запятые и символы перехода на новую строку (а также, возможно, какие-то ещё символы) кодируются предложенным вами способом.

*Формат вывода* <br/>
Выводятся N строк — соответствующие значения из таблицы. <br/>
Помните, что пользователь должен видеть запятые как запятые и переходы на новую строку как переходы на новую строку.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
|4 <br/> Дама,сдавала в багаж <br/> диван, чемодан, саквояж <br/> картину, корзину, картонку <br/> и маленькую собачонку,, <br/> 4 <br/> 0,0 <br/> 1,2 <br/> 3,1 <br/> 3,0 | Дама <br/> саквояж <br/> и маленькую собаченку |

:pushpin: [Оглавление.](#contents)

<a name="2.9"> </a>

**2.9 "Транслитерация"**

:unlock: Выполнение: :x:

Дан русский текст.

Вам необходимо транслитерировать его, то есть заменить все русские буквы на английские по правилам транслитерации для загранпаспортов 2010 года: http://mishka.travel/blog/index/node/id/1073-transliteraciya-v-zagranpasportah-rossiiskoi-federacii/.

Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь» (и их заглавные версии «Ъ» и «Ь») должны исчезнуть из текста. Строчные буквы заменяются на строчные, заглавные заменяются на заглавные. Если заглавная буква превращается при транслитерации в несколько букв, то заглавной должна остаться только первая из них (например, «Ц» → «Tc»).
Все некириллические символы должны остаться на месте.

*Формат ввода* <br/>
В единственной строке задан русский текст. Текст может состоять из любых символов, вам необходимо транслитерировать только русские буквы, а остальные оставить на месте. Гарантируется, что нет слов, состоящих только из букв «ъ» и «ь».

*Формат вывода* <br/>
Выведите одну строку — транслитерированный текст.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты. | Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, Kak mimoletnoe videne, Kak genii chistoi krasoty. |

:pushpin: [Оглавление.](#contents)

---

<a name="practice3"></a>

<a name="3.1"> </a>

**3.1 "Скажи «пароль» и проходи"**

:unlock: Выполнение: :x:

Напишите функцию ask_password(), которая запрашивает у пользователя пароль и сверяет его со строкой, в которой записано слово “password”. Пользователю дается три попытки. Как только пароль совпал с правильным значением, функция должна выводить «Пароль принят» и игнорировать дальнейший ввод. Если с трех попыток пользователь не смог угадать пароль, функция должна вывести на экран «В доступе отказано» и игнорировать ввод новых паролей. <br/>
Обратите внимание: в вашей программе должна быть функция ask_password, но она не должна вызываться. Следите за тем, чтобы имя функции было написано верно. <br/>
Тестирующая программа выглядит следующим образом: <br/>
ask_password()

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| qwerty <br/> 1234 <br/> password | Пароль принят |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| qwerty <br/> 1234 <br/> йцукен | В доступе отказано |

:pushpin: [Оглавление.](#contents)

<a name="3.2"> </a>

**3.2 "Месяц/Month"**

:unlock: Выполнение: :x:

Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| print(month_name(3, "en")) | march |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| print(month_name(3, "ru")) | март |

:pushpin: [Оглавление.](#contents)

<a name="3.3"> </a>

**3.3 "Счастливый пассажир"**

:unlock: Выполнение: :x:

Пассажир считается счастливым, если его текущий и предыдущий билеты на поездку в транспорте являются счастливыми. Напишите функцию lucky(ticket), которая проверяет этот факт и возвращает соответствующую строку.

Переменная ticket содержит в себе целое число. <br/>
В глобальной переменной lastTicket находится номер предыдущего билета пассажира.

Напомним, что билет является счастливым, если сумма первых трёх цифр совпадает с суммой трёх последних.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| lastTicket = 123456 <br/> print(lucky(100001)) | Несчастливый |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| lastTicket = 123321 <br/> print(lucky(100001)) | Счастливый |

*Примечание* <br/>
Если в переменной ticket находится не шестизначное число, то его следует дополнить нулями слева.

:pushpin: [Оглавление.](#contents)

<a name="3.4"> </a>

**3.4 "Числа в строке"**

:unlock: Выполнение: :x:

Напишите функцию from_string_to_list(string, container), которая принимает два аргумента: строку string, состоящую из целых чисел, написанных через пробел, и список container. Функция должна извлечь из строки числа и добавить их в конец списка.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| a = [1, 2, 3] <br/> from_string_to_list("1 3 99 52", a) <br/> print(* a) | 1 2 3 1 3 99 52 |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| a = [77, 'abc'] <br/> from_string_to_list("", a) <br/> print(* a) | 77 abc |

:pushpin: [Оглавление.](#contents)

<a name="3.5"> </a>

**3.5 "Цезарь"**

:unlock: Выполнение: :x:

Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций. <br/>
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции.

Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны превращаться в маленькие, большие — в большие.

Напишите также функцию декодирования decrypt_caesar(msg, shift), также использующую сдвиг по умолчанию. При написании функции декодирования используйте вашу функцию кодирования.

*Пример 1* <br/>
| Ввод | Вывод |
|----|----|
| msg = "Да здравствует салат Цезарь!" <br/> shift = 3 <br/> encrypted = encrypt_caesar(msg, shift) <br/> decrypted = decrypt_caesar(encrypted, shift) <br/> print(encrypted) <br/> print(decrypted) | Зг кзугефхецих фгогх Щикгуя! <br/> Да здравствует салат Цезарь! |

*Пример 2* <br/>
| Ввод | Вывод |
|----|----|
| msg = "Да здравствует салат Цезарь!" <br/> shift = 5 <br/> encrypted = encrypt_caesar(msg, shift) <br/> decrypted = decrypt_caesar(encrypted, shift) <br/> print(encrypted) <br/> print(decrypted) | Йе мйхезцчзшкч цереч Ыкмехб! <br/> Да здравствует салат Цезарь! |

*Примечание* <br/>
Символы русского алфавита расположены в стандартной для Python таблице кодировки подряд, то есть номера, выдаваемые функцией ord(symbol), идут подряд. <br/>
Буква «ё» идёт в таблице кодировки отдельно от основного алфавита. При решении задачи считайте, что буквы «ё» в русском алфавите нет.

:pushpin: [Оглавление.](#contents)

<a name="3.6"> </a>

**3.6 "Мимикрия"**

:unlock: Выполнение: :x:

У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>  <br/>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список <br/>
transformed_values = list(map(transformation, values)) <br/>
Единственный способ вашего взаимодействия с этим кодом – посредством задания функции transformation.

Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.

Напишите такое лямбда-выражение transformation, чтобы transformed_valuesполучился копией values.<br/>
Переменная transformation должна быть глобальной, чтобы проверяющая система смогла его найти. <br/>
Кроме transformation вам ничего писать не нужно. Печатать на экран – тоже.

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| values = [1, 23, 42, "asdfg"] <br/> transformed_values = list(map(transformation, values)) <br/> if values == transformed_values: print('ok') <br/> else: print('fail') | ok |

:pushpin: [Оглавление.](#contents)

<a name="3.7"> </a>

**3.7 "Есть ли 0"**

:unlock: Выполнение: :x:

Напишите программу, которая ищет нули в таблице чисел и печатает True, если нули нашлись. <br/>
В противном случае надо напечатать False.


Эту задачу надо постараться решить «в одну строчку». В этом вам помогут функции any и all.

*Формат ввода* <br/>
Текст c матрицей (таблицей) целых чисел в диапазоне от 0 до 99, разделённых пробелами и символами перевода строки (см. пример).

*Формат вывода* <br/>
True или False

*Пример* <br/>
| Ввод | Вывод |
|----|----|
| 64 33 79 56 78 70 45 71 82  3 <br/> 96 27  8 36 72 14 91 10 21 65 <br/> 95 28 91 23 78 38 21 50 64 37 <br/>  97 54 94  6 48 17 37 19 78 58 <br/> 69 58 35  1 70 24 60 17  3 11 <br/> 48  9 13 23 82 49 79 55 29 53 <br/>   9  2 67 90  0 17 34 55 49 63 <br/> 98 98 23 71 66 57 15 94 34 81 <br/> 58 37 32 29 10 19 53 46 95 19 <br/> 41 24 95 47 58 17 74 69 62  4 | True |

:pushpin: [Оглавление.](#contents)

---







