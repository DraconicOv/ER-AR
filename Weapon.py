class Weapeon():
    def __init__(self,BasePhys, BaseMag, BaseFir, BaseLit, BaseHol,StrSca,DexSca,IntSca,FaiSca,ArcSca,ids):
        self.BasePhys = BasePhys
        self.BaseMag = BaseMag
        self.BaseFir = BaseFir
        self.BaseLit = BaseLit
        self.BaseHol = BaseHol
        self.Str = StrSca
        self.Dex = DexSca
        self.Int = IntSca
        self.Fai = FaiSca
        self.Arc = ArcSca
        self.ids = {"phy":ids['phy'],"mag":ids['mag'],'fir':ids['fir'],"lit":ids['lit'],"hol":ids['hol']}
