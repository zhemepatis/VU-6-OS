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
    
