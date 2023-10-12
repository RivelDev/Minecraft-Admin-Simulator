import time, random, sys
#simulator of server's admin
#Author's discrod: r1velsky
print('Welcome to ADMIN simulator!')
print('[GAME BY (Discord) r1velsky]')
start  = int(input('[1 - Да] [2 - Выход] Начать игру?: '))

if start == 1:
    #1. Email
    print('GMAIL | Google Почта')
    time.sleep(0.9)
    print('От кого: Owner')
    time.sleep(0.9)
    print('Кому: Вам')
    time.sleep(0.9)
    print('Добрый день!')
    print('Ваша заявка на вступление в должность модератора была рассмотрена и принята!')
    print('Вы уже можете идти работать! Не забудьте свой пароль! (пароль: пароль, логин: ixcUwu_)')
    
    time.sleep(4)
    
    #2. Login
    print('-------------------------------------------------')
    print('[MINETODAY.ORG]')
    l_login = input('Введите ваш никнейм: ')
    l_passw = input('Введите ваш пароль: ')
    if l_login == 'ixcUwu_':
        if l_passw == 'пароль':
            l_login = True
            l_passw = True
        else:
            print('ERROR')
    else:
        print('ERROR')
    
    if l_login and l_passw == True:
        print('Вы успешно вошли. Подождите...')
        time.sleep(5)
        
        #3.Main
        xp = 0
        #
        print('---------------------------------------------')
        print('Ожидайте, пока вам поступят жалобы для их рассмотрения.')
        #
        time.sleep(11.4) 
        #
        reports_list = ['сломали дом', 'аскоробляет', 'постаел песюн', 'Читы', 'Оскорбления', 'Спамит', 'Построил писю', 'Флуд', 'тим на бв', 'оскр мамы', 'лох', 'оскр сервера', 'неприличный ник', 'Неприличный префикс', 'Неприличный суффикс', 'Неприличный скин']
        nicknames_list = ['zuzya123', 'Boomforce', 'MNB', 'chubaba', '12314414', '123149844477', 'wuwe4ka', 'Menecca_', 'MyNet33', 'notprofe', 'riveldud', 'Kyero', 'ZaharTop', 'ruVi', 'Sanders', 'lemo4eeek', 'ROSIA_RUINA', 'gleb782', 'egortop', 'kFC_top']
        nicknames_list2 = ['paporotnek', '8988888', 'blacksuetolog', 'Mikhailovksy', 'FataLeer', 'neg0r', 'HEFOPMAJI', 'sduhauhsduahda', 'notya', 'lolik', 'pusiJusi', 'baranovichi', 'moscow_cow', 'SLAVA_UKRAINA', 'v_v_puten', 'OLYA1929', 'Stilet', 'kokocuk']
        screens_list = ['Докозательств нет.', 'Докозательства есть.', 'Спорные докозательства.']
        
        screens_r = random.choice(screens_list)
        nicknames_r = random.choice(nicknames_list)
        nicknames_r2 = random.choice(nicknames_list2)
        reports_r = random.choice(reports_list)
        
        while True: 
            print('К вам поступила жалоба!')
            time.sleep(3)
            print('----------')
            print(f'Жалоба от {nicknames_r} на {nicknames_r2}; Причина: {reports_r}; {screens_r}')
            print('----------')
            time.sleep(1)
            print('----------')
            print('Итак. У вас есть команды: /ban, /kick, /warn, /mute и /ignore; но используйте их с умом!')

            command = input('Введите команду: ')
            if command == "/ban":
                command2 = input('Введите ник нарушителя: ')
                if command2 in nicknames_list2:
                    command3 = int(input('Введите время накакзания в днях: '))
                    if command3 < 360:
                        command4 = input('Введите причину: ')
                        time.sleep(4)
                        print('--------------------------------------------------------------------------------')
                        print(f'ixcUwu_ забанил игрока {command2} на {command3} дней с комментарием: "{command4}"')
                        print('----------------------------------------------------------------------------------')
                        #
                        xp_r = random.randint(1, 5)
                        xp += xp_r
                        xp = xp
                        print(f'Вы получили {xp_r} XP. Всего у вас {xp} XP')
                        #
                        time.sleep(9.6)
                        #
                        screens_r = random.choice(screens_list)
                        nicknames_r = random.choice(nicknames_list)
                        nicknames_r2 = random.choice(nicknames_list2)
                        reports_r = random.choice(reports_list)
                        #
                        
                    elif command3 > 360:
                        print('Нельзя забанить игрока больше, чем на 360 часов!')
                else:
                    print('ERROR')
            #
            elif command == '/kick':
                command2 = input('Введите ник нарушителя: ')
                command3 = input('Введите причину: ')
                if command2 in nicknames_list2:
                    time.sleep(2)
                    print('--------------------------------------------------------------------------------')
                    print(f'ixcUwu_ кикнул игрока {command2} с комментарием "{command3}"')
                    print('----------------------------------------------------------------------------------')   
                    time.sleep(8.3)
                    #
                    xp_r = random.randint(1, 5)
                    xp += xp_r
                    xp = xp
                    print(f'Вы получили {xp_r} XP. Всего у вас {xp} XP')
                    #
                    screens_r = random.choice(screens_list)
                    nicknames_r = random.choice(nicknames_list)
                    nicknames_r2 = random.choice(nicknames_list2)
                    reports_r = random.choice(reports_list)   
                    #     
                else:
                        print('ERROR')                                                                                                                           
            #
            elif command == '/mute':
                command2 = input('Введите ник нарушителя: ')
                command3 = int(input('Введите время наказания в часах: '))
                if command3 > 72:
                    print('Нельзя выдавать мут больше чем на 72 часа!')
                elif command3 < 72:
                    command4 = input('Введите причину: ')
                    if command2 in nicknames_list2:
                        time.sleep(2)
                    print('--------------------------------------------------------------------------------')
                    print(f'ixcUwu_ замутил {command2} на {command3} часов с комментарием "{command4}"')
                    print('----------------------------------------------------------------------------------')   
                    time.sleep(11.1)
                    #
                    xp_r = random.randint(1, 5)
                    xp += xp_r
                    xp = xp
                    print(f'Вы получили {xp_r} XP. Всего у вас {xp} XP')
                    #
                    screens_r = random.choice(screens_list)
                    nicknames_r = random.choice(nicknames_list)
                    nicknames_r2 = random.choice(nicknames_list2)
                    reports_r = random.choice(reports_list)   
                    #     
                else:
                        print('ERROR')  
            #
            elif command == '/warn':
                command2 = input('Введите ник нарушителя: ')
                command3 = input('Введите время удержания варна в часах: ')
                if command3 > 24:
                    print('Нельзя выдавать варн больше чем на 24 часа!')
                elif command3 < 24:
                    command4 = input('Введите причину: ')
                    if command2 in nicknames_list2:
                            time.sleep(2)
                    print('--------------------------------------------------------------------------------')
                    print(f'ixcUwu_ выдал предупреждение игроку {command2} с удержанием на {command3} часов с комментарием "{command4}"')
                    print('----------------------------------------------------------------------------------')   
                    time.sleep(13.1)
                    #
                    xp_r = random.randint(1, 5)
                    xp += xp_r
                    xp = xp
                    print(f'Вы получили {xp_r} XP. Всего у вас {xp} XP')
                    #
                    screens_r = random.choice(screens_list)
                    nicknames_r = random.choice(nicknames_list)
                    nicknames_r2 = random.choice(nicknames_list2)
                    reports_r = random.choice(reports_list)   
                    #     
                else:
                        print('ERROR')  
            #
            elif command == '/ignore':
                 #
                screens_r = random.choice(screens_list)
                nicknames_r = random.choice(nicknames_list)
                nicknames_r2 = random.choice(nicknames_list2)
                reports_r = random.choice(reports_list)   
                #    
                print('Вы проигнорировали жалобу. Она передана другому сотруднику, а вы получили дебафф к опыту.') 
            #
            elif command == '/console:debug':
                print('--------------------')
                time.sleep(0.5)
                print(f'PaperMC Console p7.1.1 (Actual) (c) 2023')
                time.sleep(2.8)
                print('--------------------')
                print(f'[Console] Current user: (mod.) IxcUwu_')
                time.sleep(0.4)
                print(f'[Console] XP Info: {xp}')
                time.sleep(1.2)
                print(f'[Console] Aviable players: {nicknames_list}; {nicknames_list2}')
                #
                screens_r = random.choice(screens_list)
                nicknames_r = random.choice(nicknames_list)
                nicknames_r2 = random.choice(nicknames_list2)
                reports_r = random.choice(reports_list)   
                #    
                time.sleep(10)
                print('----------------------')
                time.sleep(0.5)
                print('Exit debug mode...')
                time.sleep(2)
            else:
                 print('ERROR')
elif start == 2:
    time.sleep(0.5)
    print('Выход...')
    time.sleep(2)
    sys.exit()