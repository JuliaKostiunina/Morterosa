define l = Character(_("Lucy"), color="#ffcccc")
define s = Character(' ', kind=nvl, color="#c8ffc8")
define q = Character(' ', kind=nvl, color="#c8ffc8")
define e = Character(' ', kind=nvl, color="#c8ffc8")

image Elisa happy = "images/Elisa_happy.png"
image Elisa veryhappy = "images/Elisa_veryhappy.png"
image Elisa serious = "images/Elisa_serious.png"
image Queen happy  = "images/Queen_happy.png"
image Guardian  = "images/guardian.png"
image servant = "images/servant.png"
image servant_diss = "images/servant_diss.png"
image servant_diss_talk = "images/servant_diss_talk.png"
image Lucy_happy = "images/Lucy_happy.png"
image Lucy_happy_centre = "images/Lucy_happy_centre.png"
image Lucy_happy_centre_talk = "images/Lucy_happy_centre_talk.png"
image Lucy_minded = "images/Lucy_minded.png"
image Lucy_minded_talk = "images/Lucy_minded_talk.png"
image Lucy_minded_right = "images/Lucy_minded_right.png"
image Lucy_minded_right1 = "images/Lucy_minded_right1.png"
image Lucy_minded_right1_talk = "images/Lucy_minded_right1_talk.png"
image Lucy_grin = "images/Lucy_grin.png"
image Lucy_angry = "images/Lucy_angry.png"
image Lucy_amb_centre = "images/Lucy_amb_centre.png"
image Lucy_amb_centre_talk = "images/Lucy_amb_centre_talk.png"
image king = "images/king.png"
image kingfunnny = "images/kingfunnny.png"
image Queen_young_angry = "images/Queen_young_angry.png"
image MADAMA = "images/MADAMA.png"
image MADAMA2 = "images/MADAMA2.png"
image man = "images/man.png"
image man_talk = "images/man_talk.png"
image slujanka = "images/slujanka.png"
image slujanka_talk = "images/slujanka_talk.png"
image happyprincess1 = "images/happyprincess1.png"
image princess1 = "images/princess1.png"
image happyprincess2 = "images/happyprincess2.png"
image slugi = "images/slugi.png"
image Queen_young_shok = "images/Queen_young_shok.png"
image Queen_grin = "images/Queen_grin.png"
image Queen_young_shy= "images/Queen_young_shy.png"
image Queen_young_talk = "images/Queen_young_talk.png"
image Queen_young_right = "images/Queen_young_right.png"
image general  = "images/general.png"
image general1 = "images/general1.png"
image Queen_talk = "images/Queen_talk.png"
image roses = Movie(play="video/roses.webm", size=(config.screen_width, config.screen_height))

label start:
    play music "audio/music1.mp3" fadeout 1
    scene 1
    with Dissolve(.5) 

    pause .5 
    "{i}{cps=25}В нашем мире есть три Королевства. Первое и самое главное - это Мортероза. Мортероза - это благословенное королевство, жители которого по праву считаются самыми счастливыми.{/cps}{/i}"
    "{i}{cps=25}Мортероза утопает в розовых садах, которые не только придают королевству облик первозданной красоты, но и создают над ним облако сладкого аромата. Жители Мортерозы не знают, что такое голод, болезни и нищета и гордо называют свою родину раем.{/cps}{/i}"

    scene 2
    
    with Dissolve(.5)

    pause .5
    "{i}{cps=25}Также есть Королевство Солдерн, откуда родом наш главный герой. Солдерн - это королевство Солнца. Обычное средневековое государство ремесленников, художников, музыкантов, охотников и земледельцев.{/cps}{/i}"
    "{i}{cps=25}Это королевство славится своей культурой и плодородными землями. Жители строго следуют традициям Солдерна и почитают бога света-Феба.{/cps}{/i}"
   
    scene kek
   
    with Dissolve(.5)

    pause .5
    "{i}{cps=25}И последнее - Королевство синего неба - Рейенфорд. Жителям других королевств мало известно о нём, так как никто не решался посетить его или даже приблизиться к его границам. Ходят легенды, что оно охраняется драконами и магами Рейенфорда, умеющими управлять погодными условиями.{/cps}{/i}"

    scene 3

    with Dissolve(.5)

    pause .5
    "{i}{cps=25}Ну вот я и почти в Мортерозе. Предвкушаю знаменитый аромат цветов!..{/cps}{/i}"

    scene 4
    with Dissolve(.5) 

    pause .5 
    show Elisa veryhappy at right
    "Элиза" "{i}{cps=25}Привет! Это же ты посол из Солдерна?{/cps}{/i}"

    "Элиза" "{i}{cps=25}Отлично! Я тебя уже давно жду!{/cps}{/i}"

    "Элиза" "{i}{cps=25}У меня для тебя приветственный подарок от Королевы - букет наших знаменитых роз из Придворного Сада!{/cps}{/i}"

    "Элиза" "{i}{cps=25}Хочешь, я проведу тебе мини-экскурсию по городу до замка, или доберешься самостоятельно?{/cps}{/i}"


menu:
    "Да, было бы замечательно!":
        jump choice1_yes

    "Спасибо, но я думаю, что справлюсь сам.":
        jump choice1_no

label choice1_yes:

    $ menu_flag = True
        
    scene ex1
    with Dissolve(.5) 

    pause .5 
    show Elisa serious at left
    with Dissolve(.5) 

    pause .5 

    "Элиза" "{i}{cps=25}Любимое место у местных жителей - это, конечно же, городская Ярмарка. На ней проходят все главные мероприятия нашего Королевства!{/cps}{/i}"

    scene ex2
    with Dissolve(.5) 

    pause .5 
    show Elisa happy at left
    with Dissolve(.5) 

    pause .5 
    "Элиза" "{i}{cps=25}Как ты знаешь, Мортероза славится множеством растущих здесь цветов. Наша Королева очень заботится о благоустройстве королевства и поддерживает его красоту на протяжении многих лет! Мы все обожаем эти цветы!{/cps}{/i}"

    scene ex3
    with Dissolve(.5) 

    pause .5 
    show Elisa happy at right
    with Dissolve(.5) 

    pause .5 
    "Элиза" "{i}{cps=25}Ну вот мы уже и подходим к замку. Приятно было провести время!{/cps}{/i}"

    jump choice1_done

label choice1_no:

    $ menu_flag = False

    jump choice1_done

label choice1_done:

    scene zamok
    with Dissolve(.5) 

    pause .5 
    "{i}{cps=25}Не думал что тут настолько красиво...{/cps}{/i}"

    show Guardian at right
    with Dissolve(.5) 

    pause .5 
    "Военачальник" "Какова цель прибытия к Королеве?"

menu:
    "Я прибыл с целью основать посольство нашего Королевства Солдерн.":
        jump choice2_yes
    "Просто так зашел...":
        jump choice2_no

label choice2_yes:

    $ menu_flag = True

    "Военачальник" "Можете пройти к Королеве."

    scene quenntron
    with Dissolve(.5) 

    pause .5 
    show Queen happy
    with Dissolve(.5) 

    pause .5 
    "{i}{cps=25}Ваше высочество, я, посол из Солдерна, прибыл сюда с целью основать посольство нашего Королевства. Это улучшит отношения наших Королевств и укрепит экономические связи.{/cps}{/i}"
    "Королева Констанция де Монфор" "{i}{cps=25}Да, я слышала о вашем прибытии. Думаю, что создание посольства это хорошая идея. Сегодня у меня назначена аудиенция, поэтому оставим обсуждение дел на завтра. Слуга отведет вас в ваши покои.{/cps}{/i}"

    scene zamok
    with Dissolve(.5) 

    pause .5 
    show servant
    with Dissolve(.5) 

    pause .5 

    "Элизабет" "{i}{cps=25}Пойдемте, я отведу вас в ваши покои.{/cps}{/i}"

    scene room
    with Dissolve(.5) 

    pause .5 
    show servant
    with Dissolve(.5) 

    pause .5 
    "Элизабет" "{i}{cps=25}Распологайся. Если будут какие-то вопросы - ты всегда можешь найти меня в моей комнате!{/cps}{/i}"

    hide servant

    jump choice2_done

label choice2_no:

    $ menu_flag = False

    "{i}{cps=25}Конец игры. Вы не выполнили свою цель.{/cps}{/i}"

    jump choice2_done

label choice2_done:

    scene diary
    with Dissolve(1.50)

    s "{i}{cps=25}Ну вот и закончился мой первый день в Мортерозе. Слухи, доходящие до Солдерна об этом королевстве совсем не преувеличены. Наоборот...{/cps}{/i}"
    s "{i}{cps=25}Мортероза превзошло все мои ожидания: уютные деревянные домики жителей, украшенные красочные городские площади, парки с прудами, дорожками и мостиками...{/cps}{/i}"
    s "{i}{cps=25}Королевский дворец необычайной красоты, расположенный среди водопадов и зелёных садов... Люди здесь живут среди захватывающих дух ландшафтов.{/cps}{/i}"
    s "{i}{cps=25}Однако, для посла я слишком мало знал о Мортерозе. Я не знал не только об архитектуре и природе этого королевства, но и не изучил культуру и традиции его жителей.{/cps}{/i}" 
    s "{i}{cps=25}Завтра обязательно нужно сходить в дворцовую библиотеку. Там должны быть книги по истории Мортерозы.{/cps}{/i}"   

    nvl clear

    scene roomnight
    with Dissolve(.5)

    "{i}{cps=25}Сквозь сон я почувствовал, что на меня кто-то смотрит...{/cps}{/i}"

    "{i}{cps=25}Посмотрев на стену перед кроватью, мне показалось, что Королева с картины смотрит прямо на меня...{/cps}{/i}"

menu:
    "Подойти к картине.":
        jump choice3_yes
    "Остаться в кровати и попытаться уснуть.":
        jump choice3_no

label choice3_yes:

    $ menu_flag = True

    scene kartinanight
    with Dissolve(1.00)

    "{i}{cps=25}Пронизывающий взгляд королевы, казалось, был направлен прямо на меня. Не хочется признавать, но от этого мне стало немного жутко...{/cps}{/i}"
    "{i}{cps=25}Я почувствовал, что в комнате резко стало холоднее, моя кожа покрылась мурашками.{/cps}{/i}"
    "{i}{cps=25}Черт.. Что происходит?...{/cps}{/i}"
    "{i}{cps=25}Голова налилась свинцом, ноги стали подкашиваться, перед глазами всё расплывалось... Через секунду я почувствовал, как ударился об пол.{/cps}{/i}"
    "{i}{cps=25}А в следующую - я потерял сознание...{/cps}{/i}"

    scene rkartinanight
    with Dissolve(3.00)

    scene black
    with Dissolve(2.00)

    jump choice3_done
    
label choice3_no:

    $ menu_flag = False

    scene black
    with Dissolve(2.00)

    jump choice3_done

label choice3_done:

    scene day2
    with Dissolve(3.00)

    scene room
    with Dissolve(1.50)

    "{i}{cps=25}Новый день - новые приключения! Надо будет обязательно посетить библиотеку.{/cps}{/i}"

    scene koridor1
    with Dissolve(1.50)

    show servant
    with Dissolve(1.00)

    "Элизабет" "{i}{cps=25}Доброе утро! Чего-нибудь хотите?{/cps}{/i}"

menu:
    "Доброе утро! Не подскажешь, как пройти к библиотеке?":
        jump choice4_yes
    "Ветер в харю, а я шпарю! Где тут библиотека?!":
        jump choice4_no

label choice4_yes:

    $ menu_flag = True

    "Элизабет" "{i}{cps=25}Конечно! Пройди налево до конца коридора, а потом опять поверни налево.{/cps}{/i}"

    jump choice4_done
    
label choice4_no:

    $ menu_flag = False 

    "Элизабет" "{i}{cps=25}Налево по коридору...{/cps}{/i}" 

    jump choice4_done

label choice4_done:

    scene library4
    with Dissolve(1.50)

    show Lucy_happy

    "Люси" "{i}{cps=25}Привет! Я тебя тут раньше не видела! Я - Люси, и я тут работаю.{/cps}{/i}"

    "{i}{cps=25}Приятно познакомиться! Не подскажешь, где можно прочитать про историю вашего королевства?{/cps}{/i}"

    hide Lucy_happy
    show Lucy_minded
    with Dissolve(.5)

    "Люси" "{i}{cps=25}Ничего себе! Редко кто интересуется историей Мортерозы. Рада что тебя это заинтересовало! Нужно пройти в левый отсек библиотеки.{/cps}{/i}"
    
    hide servant
    with Dissolve(1.00)

    scene library5
    with Dissolve(1.50)

    "{i}{cps=25}Я подошёл и дотронулся до полок. 'Сентенция', 'Энциклопедия животного мира', 'Одд и ледяные великаны', 'Основы зельеварения'...{/cps}{/i}"

    "{i}{cps=25}Я почувствовал, как шуршат книги под моими пальцами. Это было похоже на мелодию. Я ощутил себя маленьким ребёнком, попавшим в волшебный мир.{/cps}{/i}"

    play sound "audio/creak_door.mp3"

    "{i}{cps=25}Я побежал, быстрее играя мелодию на книжных позвоночниках, пока не услышал скрип открывающейся двери...{/cps}{/i}"


    scene openlibrary
    with Dissolve(2.00)

    "{i}{cps=25}Что это? Потайная комната?{/cps}{/i}"

    "{i}{cps=25}Мне, скорее всего, нельзя входить в неё, но никого ведь тут нет..{/cps}{/i}"

    "{i}{cps=25}Я только загляну...{/cps}{/i}"

    scene library2
    with Dissolve(1.00)

    "{i}{cps=25}Я зашёл в обширную круглую комнату, освещённую множеством свечей. По кругу здесь были расставлены широкие книжные шкафы и развешаны эмблемы Мортерозы. А в центре комнаты стоял стол.{/cps}{/i}"
    
    "{i}{cps=25}Меня привлекла книга, лежащая на нём. Она выглядела необычно: от неё исходило розовое свечение. Неведомая сила влекла меня к этому столу.{/cps}{/i}"

    scene library3
    with Dissolve(1.00)

    "{i}{cps=25}Я подошёл и посмотрел на открытые страницы книги...{/cps}{/i}"

    scene diary
    with Dissolve(1.00)

    s "{i}{cps=25}1032 год. 14 апреля.{/cps}{/i}"

    s "{i}{cps=25}Всё было подготовлено для коронации Элен. Митрополит прибыл в собор уже утром, а семнадцатилетняя принцесса была уже в королевской мантии, причёсана и прекрасна, как никогда.{/cps}{/i}"

    s " "

    s "{i}{cps=25}Наша Мудрая Королева и Великий Король стояли, счастливые, подле своей дочери, давая будущей правительнице напутствия и советы. Они были очень горды за свою маленькую птичку. {/cps}{/i}"

    s " "

    s "{i}{cps=25}Именно она с этого дня будет носить бриллиантовую корону, украшенную ориентальными перлами, и поведёт королевство к миру и благополучию.{/cps}{/i}"

    nvl clear

    scene white
    with Dissolve(2.00)

    scene koronation1
    with Dissolve(2.00)

    "{i}{cps=25}Я шла быстрым и твёрдым шагом через толпы гостей прямо к отцу.{/cps}{/i}"

    show kingfunnny
    with Dissolve(1.00)
    show MADAMA
    with Dissolve(1.00)

    "{i}{cps=25}Он давал поручения по поводу коронации Элен и заметил меня лишь тогда, когда я уже несколько минут простояла рядом с ним.{/cps}{/i}"

    "{i}{cps=25}Когда Король повернулся ко мне, я увидела на его лице досаду.{/cps}{/i}"

    hide MADAMA
    hide kingfunnny

    show king
    with Dissolve(1.00)

    "Король" "{i}{cps=25}А, это ты, Констанция... Ты уже была у сестры? Она готова?{/cps}{/i}"

    hide king

    scene koronation2

    show Queen_young_angry
    with Dissolve(1.00)

    "{i}{cps=25}В моих глазах вспыхнула зависть...{/cps}{/i}"

    hide Queen_young_angry
    with Dissolve(1.00)

    scene roomprincess
    with Dissolve(2.00)

    show happyprincess1
    with Dissolve(1.00)
    show slugi
    with Dissolve(1.00)

    "{i}{cps=25}Я вспомнила, как проходя мимо покоев Элен, я слышала её милое лепетанье и её служанок, поправляющих ей платье и причёску.{/cps}{/i}"

    "{i}{cps=25}Они поздравляли её с получением трона и мечтали о наступлении новой и ещё более благополучной жизни жителей Мортерозы с её воцарением.{/cps}{/i}"

    hide slugi
    with Dissolve(1.50)

    show roses
    with Dissolve(1.00)

    "{i}{cps=25}Все любили Элен за её доброту, наивность и дружелюбие.{/cps}{/i}"

    "{i}{cps=25}Только я понимала, что такие качества не помогут королеве создать мощное и богатое Королевство. Окружающие Элен были глупцами, считающими, что решение Короля было справедливым...{/cps}{/i}"

    "{i}{cps=25}Подумать только: на трон всегда возводились старшие дети, но моя семья, в частности отец, отняли у меня это право...{/cps}{/i}"

    "{i}{cps=25}Кстати, отец на протяжении нескольких месяцев хлопотливо готовился к этому дню, переложив половину своих обязанностей на меня и своего советника.{/cps}{/i}"

    scene koronation1
    with Dissolve(1.00)

    show king
    with Dissolve(1.00)

    "{i}{cps=25}И всё-таки сейчас он досадовал, увидев перед собой не любимую младшую дочь, а меня, свою верную помощницу.{/cps}{/i}"

    "{i}{cps=25}Нет, Король, я не видела сестру, я пришла к вам по другому вопросу... Дело в том, что мне за 2 года наконец-то удалось получить соглашение Рейенфорда на торговлю, и теперь требуется...{/cps}{/i}"

    "Король" "{i}{cps=25}Констанция, разве сейчас это важно? Давай обсудим это потом.{/cps}{/i}"

    "{i}{cps=25}Но...{/cps}{/i}"

    "Король" "{i}{cps=25}Лучше сходи в покои сестры, я думаю, там потребуется твоя помощь. У неё важный день сегодня. Всё должно быть на высшем уровне.{/cps}{/i}"

    scene koronation2

    show Queen_young_angry

    "{i}{cps=25}Элен, Элен, Элен! Мои руки сжались в кулаки... Ну почему всегда она? Почему? Мне так трудно было получить это соглашение, а я не заслужила даже каплю твоего внимания, отец.... Чем же я хуже Элен? Чем?!{/cps}{/i}"

    scene koronation1
    with Dissolve(1.00)

    show kingfunnny
    show MADAMA
    show MADAMA2

    "{i}{cps=25}Отец вновь разговорился с кем-то, перестав замечать моё присутствие.{/cps}{/i}"

    scene koridorv
    with Dissolve(1.00)

    "{i}{cps=25}Я вышла в тихий и безлюдный коридор.{/cps}{/i}"

    "{i}{cps=25}Свой гнев и разочарование сдерживать казалось мне невозможным.{/cps}{/i}"

    "{i}{cps=25}Среди праздника я чувствовала себя лишней, никому не было дела до моих чувств... Я хотела сбежать, покинуть дворец на своём чёрном коне.{/cps}{/i}"

    "{i}{cps=25}Однако, блуждая по коридору, я вдруг услышала чей-то разговор.{/cps}{/i}"

    scene koridorv1
    with Dissolve(0.50)

    show man
    show slujanka

    "{i}{cps=25}Эти люди находились за поворотом, поэтому не могли видеть, что за ними наблюдают.{/cps}{/i}"

    "{i}{cps=25}Я бы прошла мимо, если бы их слова не показались мне странными.{/cps}{/i}"

    show man_talk

    "Мужчина" "{i}{cps=25}Ты всё видела, да? Отвечай!{/cps}{/i}"

    show man
    show slujanka_talk

    "Служанка" "{i}{cps=25}Я... Я не хотела...{/cps}{/i}"

    show man_talk
    show slujanka

    "Мужчина" "{i}{cps=25}Что ты видела?!Смотри мне в глаза, когда отвечаешь!{/cps}{/i}"

    show man
    show slujanka_talk

    "Служанка" "{i}{cps=25}Я ничего не знаю!{/cps}{/i}"

    "{i}{cps=25}Мне показалось, что мужчина по какой-то причине угрожал девушке, и я хотела вмешаться, но как только я вышла из-за угла, в темноте я увидела холодный металлический блеск кинжала, занесённого над служанкой.{/cps}{/i}"

    scene knife
    with Dissolve(0.5)

    play sound "audio/scream_girl.mp3"

    "{i}{cps=25}В следующую секунду он вонзил его в тонкую шею. До меня донёсся приглушённый крик...{/cps}{/i}"

    scene koridorv2
    with Dissolve(1.00)

    show Queen_young_shok

    "{i}{cps=25}Меня оковал страх, я попятилась назад, ошарашенная увиденным.{/cps}{/i}"

    "{i}{cps=25}Нужно было бежать, пока меня не заметили.{/cps}{/i}"

    scene koridorv3
    with Dissolve(1.00)

    play sound "audio/run_girl.mp3"

    "{i}{cps=25}Я бесшумно, но быстро направилась в сторону покоев Элен.{/cps}{/i}"

    show general
    with Dissolve(2.00)

    "{i}{cps=25}Смятённая, я не заметила перед собой одного из генералов отца, и мы столкнулись.{/cps}{/i}"

    hide general

    show general1
    with Dissolve(1.00)

    show Queen_young_shy
    with Dissolve(1.00)

    "Генерал Аспид" "{i}{cps=25}Извините, принцесса Констанция. Я был невнимателен. Вы в порядке?{/cps}{/i}"

    show general
    hide general1
    show Queen_young_talk
    hide Queen_young_shy

    "{i}{cps=25}Всё нормально.{/cps}{/i}"

    show general1
    hide general
    show Queen_young_shy
    hide Queen_young_talk

    "Генерал Аспид" "{i}{cps=25}Не думаю, вы выглядите напуганной. Что-то случилось?{/cps}{/i}"

    show general
    hide general1
    show Queen_young_talk
    hide Queen_young_shy

    "{i}{cps=25}Я очень тороплюсь к Элен, генерал.{/cps}{/i}"

    show general1
    hide general
    show Queen_young_shy
    hide Queen_young_talk 

    "Генерал Аспид" "{i}{cps=25}Вы хотите поздравить её? Я думал, что вы против сегодняшней коронации. По-моему на роль королевы вы подходите лучше глупой, наивной девчонки...{/cps}{/i}"

    show general
    hide general1
    show Queen_young_talk
    hide Queen_young_shy

    "{i}{cps=25}Вы так считаете?{/cps}{/i}"

    show general1
    hide general
    show Queen_young_shy
    hide Queen_young_talk

    "Генерал Аспид" "{i}{cps=25}Конечно. Вы заключили множество важных для Мортерозы соглашений. В вас чувствуется сила и уверенность.{/cps}{/i}"

    show general
    hide general1
    show Queen_young_talk
    hide Queen_young_shy

    "{i}{cps=25}Спасибо, генерал. Не думала, что кто-то во дворце поддержит меня.{/cps}{/i}"

    show general1
    hide general
    show Queen_young_shy
    hide Queen_young_talk

    "Генерал Аспид" "{i}{cps=25}Вы всегда можете положиться на меня, принцесса Констанция. Я на вашей стороне.{/cps}{/i}"

    hide general1
    show Queen_young_shy

    "{i}{cps=25}Он низко поклонился и пошёл вперёд. Я посмотрела ему вслед, раздумывая над его словами.{/cps}{/i}"

    hide Queen_young_shy
    show Queen_young_right
    with Dissolve(1.00)

    "{i}{cps=25}После я поняла, что генерал направился в сторону убийцы. Что если на него тоже нападут?! Эта мысль сдвинула меня с места, я побежала назад к месту преступления.{/cps}{/i}"

    scene koridorv1

    show man

    show general at right
    with Dissolve(1.00)

    show man_talk

    "Мужчина" "{i}{cps=25}Всё готово, генерал. Я убил ту девушку, что узнала о наших планах.{/cps}{/i}"

    show man

    "{i}{cps=25}Я резко остановилась и притаила дыхание.{/cps}{/i}"

    show general1 at right

    "Генерал Аспид" "{i}{cps=25}Хорошо, Мартин. Теперь у нас нет преград. Сегодняшним вечером мы убьём королевскую семью. Наконец-то у Мортерозы будет сильный правитель!{/cps}{/i}"

    show man_talk
    show general at right

    "Мартин" "{i}{cps=25}О да! Этот день останется в истории нашего Королевства, как начало новой, великой эпохи!{/cps}{/i}"

    show general1 at right

    play sound "audio/laugh_man.mp3"

    "{i}{cps=25}Двое мужчин рассмеялись и направились по коридору вперёд. Я осталась незамеченной.{/cps}{/i}"

    scene white 
    with Dissolve(2.00)

    scene library3
    with Dissolve(2.00)

    "{i}{cps=25}Я увлечённо читал книгу, даже не замечая того, что меня уже несколько раз назвали по имени. У меня получилось оторваться только тогда, когда девушка, работающая в библиотеке, потрепала меня по плечу.{/cps}{/i}"

    scene library2
    with Dissolve(1.00)

    show Lucy_minded_talk
    hide Lucy_minded

    "Люси" "{i}{cps=25}Послушайте, тут опасно. Вам лучше сейчас же уйти.{/cps}{/i}"

    show Lucy_minded
    hide Lucy_minded_talk
    

    "{i}{cps=25}Что? Но в книге как раз начинается самое интересное.{/cps}{/i}"

    show Lucy_minded_talk
    hide Lucy_minded

    "Люси" "{i}{cps=25}Я знаю, но она спрятана в тайной комнате неслучайно. Эта книга принадлежит королеве, и если она узнает, что кто-то читал её, то вам и мне придётся отвечать за это.{/cps}{/i}"

    show Lucy_minded
    hide Lucy_minded_talk

    "{i}{cps=25}Но...{/cps}{/i}"

    "{i}{cps=25}За дверью послышался звук чьих-то шагов.{/cps}{/i}"

    show Lucy_minded_talk
    hide Lucy_minded

    "Люси" "{i}{cps=25}Чёрт, мы опоздали. Прячьтесь за колонну и не шумите.{/cps}{/i}"

    "Люси" "{i}{cps=25}Ну что вы стоите, как вкопанный? Быстрее!{/cps}{/i}"

    show Lucy_minded
    hide Lucy_minded_talk

    "{i}{cps=25}Я был испуган, но твёрдый тон девушки, не растерявшейся в этой ситуации, заставил меня действовать. Я шмыгнул за колонну и притаился.{/cps}{/i}"

    scene stolb
    with Dissolve(1.50)

    show Lucy_minded_right1
    show Queen_talk

    play sound "audio/creak_door.mp3"

    "{i}{cps=25}В следующий миг я услышал звук открывающейся потайной двери. Я почти ничего на видел, но хорошо слышал разговор вошедшей Королевы и Люси.{/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Добрый день, Ваше Величество, Королева Констанция.{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk

    "{i}{cps=25}Королева Констанция вошла, громко стуча каблуками своей обуви. Остановившись возле стола, она пристальным взглядом окинула комнату и девушку, стоявшую напротив.{/cps}{/i}"

    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Милая, что ты забыла в этой комнате?{/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Я давно уже не наводила здесь порядок. Посмотрите, сколько пыли и паутины вокруг!{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk
    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Ты убираешься?{/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Да, Королева.{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk
    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Ты здесь одна?{/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Как видите. За все 8 лет, которые я тут работаю, кроме вас, сюда никто не заходит, а помощников у меня никогда не было.{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk
    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Я хорошо плачу тебе, чтобы ты справлялась со всем одна. Не жалуйся.{/cps}{/i}"

    "Королева Констанция" "{i}{cps=25}Какие книги брал приходивший сюда консул?{/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Консул? О ком вы говорите, Королева? Я живу здесь, не выходя, уже несколько лет. Тут никого не было.{/cps}{/i}"

    show Lucy_minded_right1
    show Queen_grin

    "{i}{cps=25}В комнате на мгновение повисла тишина. Я обдумывал слова Королевы и Люси и никак на мог понять, почему вторая скрывает моё присутствие в библиотеке.{/cps}{/i}"

    "{i}{cps=25}И почему Королева, непроявившая ко мне особого интереса в день моего приезда, пытается выведать то, какие книги я прочёл здесь. Просто любопытство? А есть ли у Королевы время для того, чтобы заниматься такими мелочами?{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk
    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Сегодня я тебе поверила, Люси. Но знай, что несмотря на твоё примерное поведение и верную службу, моё к тебе доверие может иссякнуть, милая. {/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Не пойман - не вор, Ваше Величество.{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk
    show Queen_grin
    hide Queen_talk

    play sound "audio/laugh_queen.mp3"

    "{i}{cps=25}Внезапно раздался смех Королевы Констанции. Я так удивился, что вздрогнув, ударился о колонну. Удар был не сильным, а звук его - глухим. Но всё-таки... {/cps}{/i}"

    play sound "audio/door_knock.mp3"

    show Queen_talk
    hide Queen_grin

    "Королева Констанция" "{i}{cps=25}Мне пора к Мартину. Заканчивай уборку и иди спать. Завтра выходи к нам на обед. Я познакомлю тебя с тем Консулом. Он - красивый доброжелательный человек примерно твоего возраста. {/cps}{/i}"

    show Queen_grin
    hide Queen_talk

    "{i}{cps=25}Эти слова были произнесены Королевой таким тоном, что казалось, будто они сопровождались кокетливой улыбкой и подмигиванием... Кажется, она не услышала стука... {/cps}{/i}"

    show Lucy_minded_right1_talk
    hide Lucy_minded_right1
    show Queen_grin
    hide Queen_talk

    "Люси" "{i}{cps=25}Хорошего Вам вечера.{/cps}{/i}"

    show Lucy_minded_right1
    hide Lucy_minded_right1_talk

    play sound "audio/high_heels.mp3"

    "{i}{cps=25}За этой фразой девушки последовал скрип закрывающейся двери и затихающий звук стучащих каблуков. Я понял, что опасность миновала и выдохнул с облегчением. Можно выбираться из укрытия.{/cps}{/i}"

    play sound "audio/close_door.mp3"

    scene library2
    with Dissolve(1.00)

    "{i}{cps=25}Кажется, я могу продолжить чтение. Королева Констанция...{/cps}{/i}"

    show Lucy_angry
    with Dissolve(1.50)

    play sound "audio/poshechina.mp3"

    "{i}{cps=25}Вдруг девушка повернулась ко мне. Я увидел её разгневанное лицо и тут же, не успев отреагировать на занесённую надо мной руку, получил подзатыльник. Это было неожиданно{/cps}{/i}"

    "Люси" "{i}{cps=25}Когда я прошу сидеть тихо, то нужно сидеть тихо, как мышь. А ты там трясся и подпрыгивал от каждого звука, как трусливый заяц.{/cps}{/i}"

    "Люси" "{i}{cps=25}Никакого чтения. Выметайся отсюда.{/cps}{/i}"

    "{i}{cps=25}А на вид милая девушка...{/cps}{/i}"

    "Люси" "{i}{cps=25}Что ты сказал?!{/cps}{/i}"

menu:
    "Я сказал, что ты очень милая, особенно когда злишься.":
        jump choice5_yes
    "Хорошо, я уйду. Но завтра обязательно вернусь.":
        jump choice5_no

label choice5_yes:

    $ menu_flag = True

    hide Lucy_angry
    show Lucy_amb_centre_talk

    "Люси" "{i}{cps=25}Будет тебе.{/cps}{/i}"

    hide Lucy_amb_centre_talk
    show Lucy_amb_centre

    "{i}{cps=25}Девушка мгновенно залилась краской.{/cps}{/i}"

    show Lucy_amb_centre_talk
    hide Lucy_amb_centre

    "Люси" "{i}{cps=25}Я тебя сегодня, наверное, от смерти спасла. А ты как ни в чём не бывало комплиментами тут раскидываешься...{/cps}{/i}"

    hide Lucy_amb_centre_talk
    hide Lucy_amb_centre
    show Lucy_amb_centre

    "{i}{cps=25}Можно я зайду к тебе завтра ещё раз?{/cps}{/i}"

    jump choice5_done
    
label choice5_no:

    $ menu_flag = False 

    "{i}{cps=25}Хорошо, я уйду. Но завтра обязательно вернусь.{/cps}{/i}" 

    hide Lucy_angry
    hide Lucy_amb_centre_talk
    hide Lucy_amb_centre
    show Lucy_happy_centre_talk

    jump choice5_done

label choice5_done:

    show Lucy_happy_centre_talk

    "Люси" "{i}{cps=25}Книга зацепила, да? Оно и неудивительно. Ты находишь много сходств и для тебя это странно... {/cps}{/i}"

    hide Lucy_happy_centre_talk
    show Lucy_happy_centre

    "{i}{cps=25}Откуда ты...{/cps}{/i}"

    hide Lucy_happy_centre
    show Lucy_happy_centre_talk

    "Люси" "{i}{cps=25}Тсс...{/cps}{/i}"

    "Люси" "{i}{cps=25}Живое лицо скроет всё, что задумало коварное сердце, Норберт.{/cps}{/i}"

    hide Lucy_happy_centre_talk
    show Lucy_happy_centre

    "{i}{cps=25}Откуда ты знаешь моё настоящее имя?!{/cps}{/i}"

    hide Lucy_happy_centre
    show Lucy_happy_centre_talk

    "Люси" "{i}{cps=25}Значит, я права... Я знаю его из той книги. Приходи завтра с первыми лучами солнца, тогда она слаба и не сможет следить за нами, как сейчас. Эта книга - дневниковые записи Королевы Констанции. Они объяснят тебе всё.{/cps}{/i}"

    hide Lucy_happy_centre_talk
    show Lucy_happy_centre

    "{i}{cps=25}Но ведь записям уже столько лет... Как это может быть?{/cps}{/i}"

    hide Lucy_happy_centre
    show Lucy_happy_centre_talk

    "Люси" "{i}{cps=25}Всё завтра. Иди спать. И совет на будущее - никогда не смотри на картины Королевы.{/cps}{/i}"

    scene library4_night
    with Dissolve(1.00)

    "{i}{cps=25}Девушка явно больше не хотела продолжать разговор. У меня было много вопросов, а ответы на них находились в этой странной манящей книге... Я зачитался, и было уже поздно.{/cps}{/i}"

    scene koridorv1_night
    with Dissolve(1.00)

    "{i}{cps=25}Возможно, что предложение Люси было самым разумным. Я уже порядочно устал и перенервничал. Пора спать. Книга подождёт меня до завтра.{/cps}{/i}"

    "{i}{cps=25}С этой мыслью я прошёл коридор и зашёл в свою спальню.{/cps}{/i}"

    scene roomnight
    with Dissolve(1.00)

    "{i}{cps=25}Глаза слипались,я был без сил, но мне ужасно хотелось есть. Я пропустил обед и ужин, зачитавшись в библиотеке. В дорожной сумке, которую я взял с собой из Солдерна оставалось парочка яблок.{/cps}{/i}"

    "{i}{cps=25}Но с другой стороны, рядом была служанка, которая могла принести мне полноценный ужин.{/cps}{/i}"

    "{i}{cps=25}Живот забурчал при мысли о том, что мне могли бы принести жаркое или стейк с овощами...{/cps}{/i}"

menu:
    "Попросить принести служанку ужин.":
        jump choice6_yes

    "Съесть яблоки.":
        jump choice6_no

label choice6_yes:

    $ menu_flag = True

    show servant_diss
    with Dissolve(1.00)

    "{i}{cps=25}В комнату зашла заспанная и недовольная служанка.{/cps}{/i}"

    show servant_diss_talk
    hide servant_diss

    "Элизабет" "{i}{cps=25}Чего изволите, многоуважаемый Консул? Предупреждаю, что я придворная служанка и странные ночные прихоти господ не исполняю. В мои обязанности это не входит.{/cps}{/i}"

    show servant_diss
    hide servant_diss_talk

    "{i}{cps=25}Тон и слова девушки вызвали у меня внезапный приступ кашля...{/cps}{/i}"

    "{i}{cps=25}Какие же тут странные девушки: одни бьют, другие...{/cps}{/i}"

    "{i}{cps=25}Поздний ужин входит в число странных прихотей?{/cps}{/i}"

    show servant
    hide servant_diss

    "{i}{cps=25}Лицо служанки смягчилось.{/cps}{/i}"

    show servant_talk
    hide servant

    "Элизабет" "{i}{cps=25}Я принесу, господин. Подождите немного.{/cps}{/i}"

    hide servant_talk

    "{i}{cps=25}Сделав реверанс, девушка удалилась.{/cps}{/i}"

    show servant
    with Dissolve(1.00)

    "{i}{cps=25}Подождав пару минут, я вновь увидел служанку.{/cps}{/i}"

    scene dinner
    with Dissolve(1.00)

    "{i}{cps=25}Поставив передо мной тарелку с горячей едой, она поспешно ушла.{/cps}{/i}"

    "{i}{cps=25}Я взял ложку и уже хотел было приступить к трапезе, как...{/cps}{/i}"

    scene dinner_rotten
    with Dissolve(3.00)

    "{i}{cps=25}Что за чертовщина?!{/cps}{/i}"

    "{i}{cps=25}Перед моими глазами появилась такая отвратительная картина, что голод прошёл сам собой.{/cps}{/i}"

    "{i}{cps=25}Че...черви?!{/cps}{/i}"

    "{i}{cps=25}Я решил, что это какое-то помутнение и протёр свои глаза, не веря в увиденное.{/cps}{/i}"

    scene dinner
    with Dissolve(2.00)

    "{i}{cps=25}Когда я посмотрел вновь, то увидел аппетитную рисовую кашу с нежнейшим мясом. Но притронуться к этому блюду у меня уже не было никакого желания.{/cps}{/i}"

    scene roomnight
    with Dissolve(0.50)

    "{i}{cps=25}Оставив тарелку на столе, я решил, что ничего нет лучше здоровой полезной еды на ночь. Солдернские яблочки абсолютно точно подходили в качестве позднего перекуса.{/cps}{/i}"
    
    "{i}{cps=25}Закончив есть, я решил записать все сумасшедшие события, которые произошли сегодня со мной.{/cps}{/i}"

    scene diary
    with Dissolve(1.50)

    s "{i}{cps=25}Мортероза не перестаёт удивлять меня. Вчера-своими пейзажами, сегодня-своими загадками.{/cps}{/i}"

    s "{i}{cps=25}Из-за своего любопытства я чуть было не лишился головы, проникнув в тайную библиотеку Королевы Констанции. Там я нашёл дневник почти трёхсотлетней давности одной из принцесс Королевской семьи. Прочитав часть записей, я заметил несколько подозрительных совпадений.{/cps}{/i}"

    s "{i}{cps=25}1. Принцессу 1032 года зовут так же, как и ныне правящую королеву.{/cps}{/i}"

    s "{i}{cps=25}2. Генерал, утроивший заговор против королевской семьи, судя по разговору Люси и Королевы, это тот же генерал, встреча с которым была назначена во дворце сегодняшним вечером.{/cps}{/i}"

    s "{i}{cps=25}3. Люси утверждает, что моё имя она знает их этого дневника. И хотя я всё ещё не убедился в этом лично, почему-то я верю её словам.{/cps}{/i}"

    s "{i}{cps=25}Я думаю, что всему этому есть логическое объяснение. Однако, странные вещи происходят не только в книге, но и со мной. Я стал видеть странные мимолётные образы, но такие отвратительные и страшные, что они до сих пор всплывают в моей голове. Неужели смена климата и обстановки так влияет на меня?{/cps}{/i}"

    jump choice6_done
    
label choice6_no:

    $ menu_flag = False 

    "{i}{cps=25}На ночь лучше не нагружать желудок. Да и служанку будить не хочется. Поем полноценно утром.{/cps}{/i}" 

    "{i}{cps=25}Закончив есть, я решил записать все сумасшедшие события, которые произошли сегодня со мной.{/cps}{/i}"

    scene diary
    with Dissolve(1.50)

    s "{i}{cps=25}Мортероза не перестаёт удивлять меня. Вчера-своими пейзажами, сегодня-своими загадками.{/cps}{/i}"

    s "{i}{cps=25}Из-за своего любопытства я чуть было не лишился головы, проникнув в тайную библиотеку Королевы Констанции. Там я нашёл дневник почти трёхсотлетней давности одной из принцесс Королевской семьи. Прочитав часть записей, я заметил несколько подозрительных совпадений.{/cps}{/i}"

    s "{i}{cps=25}1. Принцессу 1032 года зовут так же, как и ныне правящую королеву.{/cps}{/i}"

    s "{i}{cps=25}2. Генерал, утроивший заговор против королевской семьи, судя по разговору Люси и Королевы, это тот же генерал, встреча с которым была назначена во дворце сегодняшним вечером.{/cps}{/i}"

    s "{i}{cps=25}3. Люси утверждает, что моё имя она знает их этого дневника. И хотя я всё ещё не убедился в этом лично, почему-то я верю её словам.{/cps}{/i}"

    jump choice6_done

label choice6_done:

    nvl clear

    scene day3
    with Dissolve(2.50)

    #"{i}{cps=25}{/cps}{/i}"