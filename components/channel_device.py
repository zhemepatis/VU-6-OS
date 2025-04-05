class ChannelDevice:
    def __init__(self):
        self.SB = None  # Source Block
        self.DB = None  # Destination Block
        self.ST = None  # Source Type
        self.DT = None  # Destination Type
    
    def transfer_data(self, SB, DB, ST, DT):
        self.SB = SB
        self.DB = DB
        self.ST = ST
        self.DT = DT
        print(f"Data transfer initiated: Source ({SB}, {ST}) -> Destination ({DB}, {DT})")
    
    def get_number(self, block, word, memory):
        value = input(f"Enter a value for Block {block}, Word {word}: ")
        memory[block][word] = int(value)
        print(f"Value {value} stored at Block {block}, Word {word}")
        
    def put_number(self, block, word, memory):
        value = memory[block][word]
        print(f"Value at Block {block}, Word {word}: {value}")
        
    def put_data(self, block, word, memory):
        print("Data output starting from Block {block}, Word {word}:")
        for i in range(10):
            current_word = word + i
            if current_word >= len(memory[block]):
                break
            if memory[block][current_word] == ord('$'):
                break
            print(memory[block][current_word], end=" ")
        print()
