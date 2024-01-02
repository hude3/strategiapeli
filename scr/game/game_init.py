# luo pelin tiedoston pohjalta
from scr.game.game import Game
from scr.tiles.city import City
from scr.game.game_errors import CorruptedSaveFileError


class GameInit(object):



    def load_game(self, input):
        tiles_read = False
        players_read = False
        info_read = False
        cities_read = False
        units_read = False

        game = Game()


        try:
            current_line = input.readline()
            header_parts = current_line.split(' ')

            if header_parts[0].strip() != 'STRAT':                      # headerin luku
                raise CorruptedSaveFileError('Error in header parts')

            if header_parts[1].strip() != 'Savefile':
                raise CorruptedSaveFileError('Error in header parts')


            data_types = ['#game info', '#players', '#tiles', '#cities', '#units', '#end']

            current_line = input.readline()
            while tiles_read == False or players_read == False or info_read == False or cities_read == False or units_read == False:
                if current_line.strip().lower() in data_types:



                    if current_line.strip().lower() == '#game info':            # game info pakko löytyä tiedostosta
                        vuorot_read = False
                        size_read = False
                        while info_read == False:
                            current_line = input.readline()
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().split(':')[0].strip().lower() == 'turns played':
                                turn_amount = int(current_line.strip().split(':')[1].strip().lower())
                                game.set_turn_counter(turn_amount)
                                vuorot_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'map size':
                                width = int(current_line.strip().split(':')[1].strip().lower().split('x')[0])
                                height = int(current_line.strip().split(':')[1].strip().lower().split('x')[1])
                                game.set_saved_map(int(width), int(height))
                                size_read = True
                            else:
                                if current_line.strip()[0] == '#':
                                    raise CorruptedSaveFileError('Error in game info')
                            if vuorot_read and size_read:
                                info_read = True


                    elif current_line.strip().lower() == '#players':
                        player_read = False
                        ai_read = False
                        while players_read == False:
                            current_line = input.readline()
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().split(':')[0].strip().lower() == 'player':
                                name = current_line.strip().split(':')[1].strip()
                                money = int(current_line.strip().split(':')[2].strip())
                                game.set_player(name,money)
                                player_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'ai money':
                                money = int(current_line.strip().split(':')[1].strip())
                                game.set_AI(None,money)
                                ai_read = True
                            else:
                                if current_line.strip()[0] == '#':
                                    raise CorruptedSaveFileError('Error in player info')

                            if player_read and ai_read:
                                players_read = True


                    elif current_line.strip().lower() == '#tiles':
                        if not info_read:
                            raise CorruptedSaveFileError('Game info needs to be before tiles')
                        tiles_counted = 0
                        tiles_need_to_be_counted = height * width       # tallennusmuodossa pitää tulla pelin tiedot ennen laattoja, jotta tiedetään oikea laattojen määrä
                        while tiles_counted != tiles_need_to_be_counted:
                            current_line = input.readline()
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().lower().split(',')[0] in ['w', 'p', 'm', 'h', 'f']:
                                type = current_line.strip().lower().split(',')[0]
                                x = int(current_line.strip().lower().split(',')[1])
                                y = int(current_line.strip().lower().split(',')[2])

                                game.map.set_saved_tile(type, x, y)
                                tiles_counted += 1
                            else:
                                if current_line.strip()[0] == '#':
                                    raise CorruptedSaveFileError('Error in tiles')
                        tiles_read = True

                    elif current_line.strip().lower() == '#cities':
                        current_line = input.readline()
                        while current_line.strip().lower() not in data_types:
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().lower().split(',')[0] == 'p':
                                player = game.player
                                x = int(current_line.strip().lower().split(',')[1])
                                y = int(current_line.strip().lower().split(',')[2])
                                hp = int(current_line.strip().lower().split(',')[3])
                                tile = game.map.tiles[x][y]
                                city = City(player, tile)
                                city.set_hp(hp)
                            elif current_line.strip().lower().split(',')[0] == 'a':
                                player = game.AI
                                x = int(current_line.strip().lower().split(',')[1])
                                y = int(current_line.strip().lower().split(',')[2])
                                hp = int(current_line.strip().lower().split(',')[3])
                                tile = game.map.tiles[x][y]
                                city = City(player, tile)
                                city.set_hp(hp)
                            current_line = input.readline()
                        cities_read = True

                    elif current_line.strip().lower() == '#units':
                        current_line = input.readline()
                        while current_line.strip().lower() not in data_types:
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().lower().split(',')[0] in ['p','a']:
                                if current_line.strip().lower().split(',')[0] == 'p':
                                    player = game.player
                                else:
                                    player = game.AI
                                x = int(current_line.strip().lower().split(',')[3])
                                y = int(current_line.strip().lower().split(',')[4])
                                tile = game.map.tiles[x][y]
                                type = current_line.strip().lower().split(',')[1]
                                unit = game.build_saved_unit(type,tile,player)
                                if type in ['sw','kn','ar']:
                                    hp = int(current_line.strip().lower().split(',')[2])
                                    unit.set_health_points(hp)
                            current_line = input.readline()
                        units_read = True
                else:
                    current_line = input.readline()

            return game
        except OSError as e:
            error = CorruptedSaveFileError('Error in opening the file')
            raise error from e
        except CorruptedSaveFileError:
            return False
