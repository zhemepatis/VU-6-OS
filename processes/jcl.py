from process import Process

class JCL(Process):
    def __init__(self, memory):
        # process specific
        self.step = 1
        self.memory = memory

    def exec(self, title):
        supervisor_memory_start = self.memory.SUPERVISOR_MEMORY_START #supervisor memory index
        supervisor_index = 0
        lines_index = 0 #index of the lines

        if self.step == 1: #blokavimasis laukiant "uzkrauk faila"
            self.step = 2
            return

        if self.step == 2: #blokavimasis laukiant "kanalu irenginys"
            self.step = 3
            return

        if self.step == 3: #nuskaitomas visas hdd failas
            lines = self.read_hdd_file("hdd.txt")
            self.step = 4
            return

        if self.step == 4: #imama viena failo eilute
            current_line = lines[lines_index]
            lines_index += 1
            self.step = 5
            return

        if self.step == 5: #ar pasiekta failo pabaiga? jei taip - step 6
            self.step = 6 if lines_index >= len(lines) else self.step = 7
            return

        if self.step == 6: #atlaisvinama "eilute atmintyje" su pranesimu apie programos nebuvima
            self.step = 18
            return

        if self.step == 7: #ar tai programos pavadinimas?
            self.step = 8 if current_line==title+'\n' else self.step = 4
            return

        if self.step == 8: #ar pries tai esanti eilute yra $AMJ?
            self.step = 9 if lines_index-1 == 0 or lines[lines_index-2].strip() != "$AMJ" else self.step = 10
            return

        if self.step == 9: #atlaisvinti "eilute atmintyje" su pranesimu apie AMJ trukuma
            self.step = 18
            return

        if self.step == 10: #imama viena failo eilute
            current_line = lines[lines_index]
            lines_index += 1
            self.step = 11
            return

        if self.step == 11: #ar tai $END blokas?
            self.step = 12 if current_line.strip() == "$END" else self.step = 13
            return

        if self.step == 12: #atlaisvinti "uzduotis supervizorineje" su konstanta 1
            self.step = 18
            return

        if self.step == 13: #ar tai failo pabaiga?
            self.step = 14 if lines_index >= len(lines) else self.step = 15
            return

        if self.step == 14: #atlaisvinti "eilute atmintyje" su pranesimu apie END trukuma
            self.step = 18
            return

        if self.step == 15: #ar tai yra DATA blokas?
            self.step = 16 if current_line.strip() == "DATA" else self.step = 17
            return

        if self.step == 16: #pakeiciami atitinkami kintamieji data segmento irasymui
            self.step = 17
            return

        if self.step == 17: #eilute irasoma i supervizorine atminti
            self.step = 18
            return

        if self.step == 18: #atlaisvinamas kanalu irenginys
            self.step = 1
            return
        
    def read_hdd_file(self, file):
        hdd_file = open(file, "r")
        lines = hdd_file.readlines()
        hdd_file.close()
        return lines