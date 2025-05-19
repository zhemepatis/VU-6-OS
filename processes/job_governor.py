from process import Process

class JobGovernor(Process):
    def __init__(self):
        # process specific
        self.step = 1

    def exec(self):
        if self.step == 1: #blokavimasis laukiant "uzduotis supervizorineje"
            self.step = 2
            return

        if self.step == 2: #proceso "virtuali masina" kurimas
            self.step = 3
            return

        if self.step == 3: #blokavimasis laukiant "vartotojo atmintis"
            self.step = 4
            return

        if self.step == 4: #nustatomas PTR ir isskiriama 16 bloku VM
            self.step = 5
            return

        if self.step == 5: #blokavimasis laukiant "supervizorine atmintis"
            self.step = 6 
            return

        if self.step == 6: #blokavimasis laukiant "kanalu irenginys"
            self.step = 7
            return

        if self.step == 7: #kopijuojami duomenys is supervizorines i virtualia atminti
            self.step = 8 
            return

        if self.step == 8: #atlaisvinamas "kanalu irenginys"
            self.step = 9 
            return

        if self.step == 9: #atlaisvinama "supervizorine atmintis"
            self.step = 10
            return

        if self.step == 10: #atlaisvinama "Vartotojo atmintis"
            self.step = 11
            return

        if self.step == 11: #blokavimasis laukiant "Is interrupt"
            self.step = 12 
            return

        if self.step == 12: #proceso "virtuali masina" stabdymas    
            self.step = 13
            return

        if self.step == 13: #ar tai PD?
            self.step = 14
            return

        if self.step == 14: #i isvedimo srauta isvedama 10 zodziu nuo nurodytos atminties vietos
            self.step = 15
            return

        if self.step == 15: #ar tai GS?
            self.step = 16 
            return

        if self.step == 16: #atlaisinama "naudojama bendroji atmintis" su pranesimu kad tai nuskaitymas
            self.step = 17
            return

        if self.step == 17: #ar tai PS?
            self.step = 18
            return

        if self.step == 18: #atlaisinama "naudojama bendroji atmintis" su pranesimu kad tai ivedimas
            self.step = 19
            return
        
        if self.step == 19: #ar tai PN?
            self.step = 20
            return
        
        if self.step == 20: #i isvedimo srauta pasiunciamas atsiustu adresu esantis vartotojo atminties blokas 
            self.step = 21
            return
        
        if self.step == 21: #ar tai GN?
            self.step = 22
            return
        
        if self.step == 22: #blokavimasis laukiant "vartotojo atmintis, skirto sitam JobGovernor"
            self.step = 23
            return
        
        if self.step == 23: #proceso "virtuali masina" aktyvavimas
            self.step = 24
            return
        
        if self.step == 24: #naikinti procesa "virtuali masina"
            self.step = 25
            return
        
        if self.step == 25: #atlaisvinti "vartotojo atmintis"
            self.step = 26
            return
        
        if self.step == 26: #atlaisvinti "uzduotis supervizorineje" su konstanta 0
            self.step = 27
            return
        
        if self.step == 27: #blokavimasis laukiant "neegzistuojantis"
            self.step = 1
            return