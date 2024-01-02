


class GameSaver(object):


    def save_game(self, game, filename):
        self.save_file = open(filename, 'w')

        self.save_file.write('STRAT Savefile 1\n')
        self.empty_row()                                        # metodilla tehdään tyhjä rivi

        self.save_file.write('#Game info\n')
        self.empty_row()

        self.save_file.write(f'Turns played: {game.turn_counter:d}\n')
        self.save_file.write(f'Map size: {game.map.get_width():d}x{game.map.get_length():d}\n')
        self.empty_row()

        self.save_file.write('#Players\n')
        self.empty_row()

        self.save_file.write(f'Player: {game.player.name:s} : {game.player.money:d}\n')
        self.save_file.write(f'AI money: {game.AI.money:d}\n')
        self.empty_row()

        self.save_file.write('#Tiles\n')

        width = game.map.get_width()
        length = game.map.get_length()
        for x in range(width):
            for y in range(length):
                tile = game.map.get_tile(x,y)
                self.save_file.write(f'{tile.type:s},{x:d},{y:d}\n')
        self.empty_row()

        self.save_file.write('#Cities\n')
        for i in range(len(game.player.cities_list)):
            city_x = game.player.cities_list[i].coordinates[0]
            city_y = game.player.cities_list[i].coordinates[1]
            city_hp = game.player.cities_list[i].health_points
            self.save_file.write(f'p,{city_x:d},{city_y:d},{city_hp:d}\n')
        for i in range(len(game.AI.cities_list)):
            city_x = game.AI.cities_list[i].coordinates[0]
            city_y = game.AI.cities_list[i].coordinates[1]
            city_hp = game.AI.cities_list[i].health_points
            self.save_file.write(f'a,{city_x:d},{city_y:d},{city_hp:d}\n')
        self.empty_row()

        self.save_file.write('#Units\n')
        for i in range(len(game.player.units_list)):
            hp = game.player.units_list[i].health_points
            if hp == None:
                hp = 'n'
            else:
                hp = str(hp)
            unit_x = game.player.units_list[i].coordinates[0]
            unit_y = game.player.units_list[i].coordinates[1]
            type = game.player.units_list[i].type
            self.save_file.write(f'p,{type:s},{hp:s},{unit_x:d},{unit_y:d}\n')

        for i in range(len(game.AI.units_list)):
            hp = game.AI.units_list[i].health_points
            if hp == None:
                hp = 'n'
            else:
                hp = str(hp)
            unit_x = game.AI.units_list[i].coordinates[0]
            unit_y = game.AI.units_list[i].coordinates[1]
            type = game.AI.units_list[i].type
            self.save_file.write(f'a,{type:s},{hp:s},{unit_x:d},{unit_y:d}\n')


        self.empty_row()
        self.save_file.write('#END')


        self.save_file.close()



    def empty_row(self):            # metodi joka tekee tyhjän rivin
        self.save_file.write('\n')

