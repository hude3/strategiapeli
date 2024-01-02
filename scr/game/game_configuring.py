from scr.game.game_errors import CorruptedConfigureFileError

class Configure(object):            # luen configure tiedoston siten, että jokaisella rivillä pitää olla arvo
                                    # järjestyksen pitää olla kohdillaan


    def config(self):
        try:
            file = open('configure.txt', 'r')


            current_line = file.readline()
            header_parts = current_line.split(' ')

            if header_parts[0] != 'STRAT':                                      # katsoo että header kunnossa
                raise CorruptedConfigureFileError('Error in header parts')

            if header_parts[1] != 'Configure\n':
                raise CorruptedConfigureFileError('Error in header parts')

            data_types = ['#game options', '#unit options', '#tile options']

            game_options_read = False
            unit_options_read = False
            tile_options_read = False

            current_line = file.readline()
            while not game_options_read or not unit_options_read or not tile_options_read:          # pitää siis lukea kaikki datatyypit
                if current_line.strip().lower() in data_types:

                    if current_line.strip().lower() == '#game options':         # lukee game options
                        ai_color_read = False
                        p_color_read = False
                        while not game_options_read:

                            current_line = file.readline()
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().split(':')[0].strip().lower() == 'player color(rgb)':
                                self.pl_color = (int(current_line.strip().split(':')[1].strip().split(',')[0]),int(current_line.strip().split(':')[1].strip().split(',')[1]),int(current_line.strip().split(':')[1].strip().split(',')[2]))
                                p_color_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'ai color(rgb)':
                                self.ai_color = (int(current_line.strip().split(':')[1].strip().split(',')[0]),int(current_line.strip().split(':')[1].strip().split(',')[1]),int(current_line.strip().split(':')[1].strip().split(',')[2]))
                                ai_color_read = True
                            if p_color_read and ai_color_read:
                                game_options_read = True
                    elif current_line.strip().lower() == '#unit options':
                        sw_read = False
                        ar_read = False
                        kn_read = False
                        se_read = False
                        current_line = file.readline()
                        while not unit_options_read:

                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().split(':')[0].strip().lower() == 'swordsman':
                                info = self.read_unit_info(file)
                                self.sw_name = info[0]
                                self.sw_hp = info[1]
                                self.sw_combat = info[2]
                                self.sw_range = info[3]
                                self.sw_speed = info[4]
                                self.sw_cost = info[5]
                                sw_read = True

                            elif current_line.strip().split(':')[0].strip().lower() == 'archer':
                                info = self.read_unit_info(file)
                                self.ar_name = info[0]
                                self.ar_hp = info[1]
                                self.ar_combat = info[2]
                                self.ar_range = info[3]
                                self.ar_speed = info[4]
                                self.ar_cost = info[5]
                                ar_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'knight':
                                info = self.read_unit_info(file)
                                self.kn_name = info[0]
                                self.kn_hp = info[1]
                                self.kn_combat = info[2]
                                self.kn_range = info[3]
                                self.kn_speed = info[4]
                                self.kn_cost = info[5]
                                kn_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'settler':
                                info = self.read_unit_info(file)
                                self.se_name = info[0]
                                self.se_speed = info[4]
                                self.se_cost = info[5]
                                se_read = True
                            if ar_read and sw_read and kn_read and se_read:
                                unit_options_read = True
                            current_line = file.readline()


                    elif current_line.strip().lower() == '#tile options':           # käydään läpi jokasen tilen options
                        f_read = False
                        m_read = False
                        w_read = False
                        h_read = False
                        p_read = False
                        while not tile_options_read:
                            current_line = file.readline()
                            if current_line.strip().lower() == '':
                                pass
                            elif current_line.strip().split(':')[0].strip().lower() == 'forest':
                                info = self.read_tile_info(file)
                                self.f_def = info[0]
                                self.f_color = info[1]
                                self.f_amount = info[2]
                                f_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'water':
                                info = self.read_tile_info(file)
                                self.w_def = info[0]
                                self.w_color = info[1]
                                self.w_amount = info[2]
                                w_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'mountain':
                                info = self.read_tile_info(file)
                                self.m_def = info[0]
                                self.m_color = info[1]
                                self.m_amount = info[2]
                                m_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'hills':
                                info = self.read_tile_info(file)
                                self.h_def = info[0]
                                self.h_color = info[1]
                                self.h_amount = info[2]
                                h_read = True
                            elif current_line.strip().split(':')[0].strip().lower() == 'plains':
                                info = self.read_tile_info(file)
                                self.p_def = info[0]
                                self.p_color = info[1]
                                self.p_amount = info[2]
                                p_read = True
                            if f_read and w_read and m_read and h_read and p_read:
                                tile_options_read = True

                else:
                    current_line = file.readline()
            file.close()








        except OSError as e:                 # nappaa error corruptedconffile errorina
            error = CorruptedConfigureFileError('Error in opening the file')
            raise error from e
        except ValueError as e:
            error = CorruptedConfigureFileError('Error in configure values')
            raise error from e
        except CorruptedConfigureFileError:
            return False



    def read_unit_info(self, file):                         # apufunktio unitin tietojen lukuun
        current_line = file.readline()
        name = None
        max_hp = None
        combat_s = None
        range = None
        speed = None
        cost = None
        while cost == None:                             # cost on tiedoston viimeinen unitin ominaisuus ja se pitää olla kaikilla eli lopettaa tietyn unitin tietojenluvun
            if current_line.strip().lower() == '':
                pass
            elif current_line.strip().split(':')[0].strip().lower() == 'name':
                name = current_line.strip().split(':')[1].strip()
            elif current_line.strip().split(':')[0].strip().lower() == 'max hp':
                max_hp = int(current_line.strip().split(':')[1].strip())
            elif current_line.strip().split(':')[0].strip().lower() == 'combat strength':
                combat_s = int(current_line.strip().split(':')[1].strip())
            elif current_line.strip().split(':')[0].strip().lower() == 'range':
                range = int(current_line.strip().split(':')[1].strip())
            elif current_line.strip().split(':')[0].strip().lower() == 'speed':
                speed = int(current_line.strip().split(':')[1].strip())
            elif current_line.strip().split(':')[0].strip().lower() == 'cost':
                cost = int(current_line.strip().split(':')[1].strip())
            current_line = file.readline()
        return name, max_hp, combat_s, range, speed, cost


    def read_tile_info(self, file):         # apufunktio tilen tietojen lukuun
        current_line = file.readline()
        defence = None
        color = None
        amount = None

        while amount == None:               # amount on tilen vaihtoehtojen viimeinen parametri joten se päättää yksittäisen tilen luvun
            if current_line.strip().lower() == '':
                pass
            elif current_line.strip().split(':')[0].strip().lower() == 'defence multiplier':
                defence = float(current_line.strip().split(':')[1].strip())
            elif current_line.strip().split(':')[0].strip().lower() == 'color(rgb)':
                color = (int(current_line.strip().split(':')[1].strip().split(',')[0]),int(current_line.strip().split(':')[1].strip().split(',')[1]),int(current_line.strip().split(':')[1].strip().split(',')[2]))
            elif current_line.strip().split(':')[0].strip().lower() == 'amount':
                amount = int(current_line.strip().split(':')[1].strip())
            current_line = file.readline()
        return defence, color, amount

