__author__ = 'N05F3R4TU'

class Banners(object):

    def options(self):
        import inspect
        from veryprettytable import VeryPrettyTable

        commands = VeryPrettyTable(["Command", "Description"])
        commands.align = "l"
        commands.padding_width = 2

        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr)()])
        return commands

    def randomize(self):
        import inspect
        import random

        banner = []
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__", "randomize"]:
                banner.append(attr)
        getattr(self, random.choice(banner))()
        # return random.choice(banner)

    @classmethod
    def daemon_threat(cls):
        print("""
                            daemon_threat
                      \,,,/      was here
                      (o o)
            ----o000o--(_)--o000o----""")

    @classmethod
    def kilroy(cls):
        print("""
                            kilroy was
                      \,,,/      here
                      (o o)
            ----o000o--(_)--o000o----""")
    @classmethod
    def rain_with_rage(cls):
        print("""
            _______________▄▄▄▄▄▄__▄▄▄▄▄
            __________▄▄▀▀_______▀▀▀____▀▀█▄
            _____▄▄▄█▀________________▄▄▄▄▄██▄
            __█▀▀▄▄▄▄▄▄▄██████████████████▄
            _███████████████████████████████▄
            █████████████████████████████████
            ▀████████████████████████████████
            _▀██████████████████████████████▀
            ___▀██████████████████████████▀▀
            __________▀███████████████████▀
            ________▄▄____▀▀▀▀▀▀_____▄_▀▀
            _____▄███_________▄____▄██____
            ___█████_______▄██___████____▄
            ____▀██▀_____▄████___▀▀▀__▄██
            __________▄█__████________████
            _______▄███___▀▀_________████
            ________▀▀_________________▀▀
            ________▄________________▄
            ____▄███_________▄____▄██
            __█████_______▄██___████____▄
            ___▀██▀_____▄████___▀▀▀__▄██
            _________▄█__████________████
            ______▄███___▀▀_________████
            _______▀▀_________________▀▀

            -- Rain with Rage,
                    exploit with Love --""")
    @classmethod
    def arachnida(cls):
        print('''
                   ;               ,
                 ,;                 '.
                ;:                   :;
               ::                     ::
               ::                     ::
               ':                     :
                :.                    :
             ;' ::                   ::  '
            .'  ';                   ;'  '.
           ::    :;                 ;:    ::
           ;      :;.             ,;:     ::
           :;      :;:           ,;"      ::
           ::.      ':;  ..,.;  ;:'     ,.;:
            "'"...   '::,::::: ;:   .;.;""'
                '"""....;:::::;,;.;"""
            .:::.....'"':::::::'",...;::::;.
           ;:' '""'"";.,;:::::;.'""""""  ':;
          ::'         ;::;:::;::..         :;
         ::         ,;:::::::::::;:..       ::
         ;'     ,;;:;::::::::::::::;";..    ':.
        ::     ;:"  ::::::"""'::::::  ":     ::
         :.    ::   ::::::;  :::::::   :     ;
          ;    ::   :::::::  :::::::   :    ;
           '   ::   ::::::....:::::'  ,:   '
            '  ::    :::::::::::::"   ::
               ::     ':::::::::"'    ::
               ':       """""""'      ::
                ::                   ;:
                ':;                 ;:"
                  ';              ,;'
        ''')
    @classmethod
    def targets(cls):
        print('''
    ████████╗_█████╗_██████╗__██████╗_███████╗████████╗███████╗
    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝_██╔════╝╚══██╔══╝██╔════╝
    ___██║___███████║██████╔╝██║__███╗█████╗_____██║___███████╗
    ___██║___██╔══██║██╔══██╗██║___██║██╔══╝_____██║___╚════██║
    ___██║___██║__██║██║__██║╚██████╔╝███████╗___██║___███████║
    ___╚═╝___╚═╝__╚═╝╚═╝__╚═╝_╚═════╝_╚══════╝___╚═╝___╚══════╝
    ___________________________________________________________
        ''')
    @classmethod
    def pirate(cls):
        print('''
                                                        :8@@@@@@@@8C
                                                  t@@@@@@@@@@@@@@@@@@@@@1
                                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       There comes a time in most men’s lives
                                            @@@@i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.         where they feel the need
                                           @@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@C          to raise the Black Flag
                                          1@@@i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,
@                                         @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                           @
@@                                       @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0                                         @@
@@@f                                     @@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                       1@@@
G@@@@                                    @@@i@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@f                                     @@@@8
 @@@@@i                                  @@@.@@@@f    f@@@@@@@@@@@@81  L@@@@@8t@@@C                                   ;@@@@@
  @@@@@@                                 @@0G@@@          @@@@@@@         1@@@.@@@1                                  @@@@@@
   @@@@@@8                               @@Gf@@@          @@@@@@L          @@@ @@@                                 8@@@@@@.
    @@@@@@@                              @@0.@@@         .@@@@@@@,        .@@@.@@i                                @@@@8@@.
     @@@@@@@@                            :@G.@@@G       @@@@  8@@@@,      @@@@ @;                               @@@@@1@@
      @@@@@@@@8                             @@@@@@   :@@@@@.   G@@@@@@8f8@@@@@@@8                             8@@@@@ @@
       8@@@@@@@@t                         @@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@;                          f@@@@@@1@8
        ,@@@@@@@@@:                        @@@@@@@@@@@@@@@;      @@@@@@@@@@@@@@@@                         t@@@@@@ @@,
          @@@@@@@@@@i                       0@@L   G@@@@@@ .@@   @@@@@@@@.  :88.                        L@@@@@@LL@@
           .@@@@@@@@@@C                        @i   @@@@@@@@@@@@@@@@@@@@  8@@                         0@@@@@@@ @@
             0@@@@@@@@@@@                     8@@@  ,@@@@@@@@@@@@@@@@@@: @@@0                       @@@@@@@@ @@G
               @@@@@@@@@@@@                    @@@i  ,@@@@@@@@@@@@@@@C  L@@@                     .@@@@@@@@ @@@
                 @@@@@@@@@@@@0                 i@@@   @ 0@f @@ 8@  @@   @@@@                   8@@@@@@@@ @@@
                   @@@@@@@@@@@@@               .@@@i L@ @@@f@@ @@@ @@L  @@@                 ,@@@@@@@@@@@@@
                     @@@@@@@@88@@@@            i@@@@   ..              G@@@               @@@@8@@@@@@@@@
                       8@@@@@@@,1@@@@L          @@@@@ .@@:8@@ @@@ @@G @@@@8            0@@@@:L@@@@@@@C
                         ;@@@@@@@1 @@@@@;        G@@@@@@@@@@@@@@@@@@@@@@@L          8@@@@@ 8@@@@@@@
                            @@@@@@@@ ;@@@@@C        @@@@@@@@@@@@@@@@@@@          8@@@@@. @@@@@@@@
                              f@@@@@@@C C@@@@@@      .@@@@@@@@@@@@@@@t       ,@@@@@@i @@@@@@@@:
                                 @@@@@@@@C 8@@@@@@G     ,,.     .:;.      @@@@@@@; 8@@@@@@@@
                                    @@@@@@@@8 L@@@@@@@t               8@@@@@@@; @@@@@@@@@
                                       @@@@@@@@@ ,@@@@@@@@0       @@@@@@@@@ i@@@@@@@@@
                                          @@@@@@@@@C 8@@@@@@@@@  @@@@@@t @@@@@@@@@G
                       C@@@@t                L@@@@@@@@@i 8@@@@@@@@@0 0@@@@@@@@@                .@@@@@
                     ;@@@@@@@@@i                 @@@@@@@@@@f ;@@@@@@@@@@C it                 @@@@@@@@@@
                     @@@@@@@@@@@@            ,@@@@@; 8@@@@@@@@@@  :@@@@@@@@@@@,            @@@@@@@@@@@@
                     .@@@@@i@@@@@@      8@@@@@@@@@@@.  G G@@@@@@@@@@8   f@@@@@@@@@@@;     @@@@@@,@@@@@0
                       ;80   .@@@@@. @@@@@@@@@,  1@@@@@@@@@@ ;@@@@@@@@@@@@@   G@@@@@@@@f @@@@@@   f@f
                      .@0  .L  @@@@@@,      @@@@@@@@@@@@@@        i@@@@@@@@@@@@@i     :@@@@@@0 :1  t@1
         @@@@@@@ @@@@;@@@@i@@@C.@@@@@@8 @@@@@@@@@@@@t                  .@@@@@@@@@@@@  @@@@@@8 @@@ @@@@ @@@@ @@@@@@@
        @@@@@@@@@1@@@@.@@@@@0@@GL@@@@@ @@@@@@@G                              ,@@@@@@@ L@@@@@ @@@0@@@@.@@@@@;@@@@@@@@
        @@@@@@@@; @@@@@@@@@@@@@@ @@@@@ @i                                          .0 t@@@@.@@@@@@@@@@@@@@  @@@@@@@@
        G@@@@@,   ; @@@@@@@@@@@@ :@@@@                                                0@@@@ C@@@@@@@@@@@, .   @@@@@@
         :@@@@@@@.                @@@@C                                               @@@@.               G@@@@@@@8
            .t.                   .@@@@@ @@@@                                  C@@@. @@@@@                   .t:
                                   @@@@@@@@@@@                                 @@@@@@@@@@
                                    @@@@@@@@@C                                 @@@@@@@@@
                                       @@@@G                                     8@@@0

        ''')

    @classmethod
    def sql_inject(cls):
        print("""
           :fGGGGGGGGC             :1fGGGGft:           CGGGGG
        ,GGGGGGGGGGGGC         .fGGGGGGGGGGGGGGG;       CGGGGG
       fGGGGGGGGGGGGGC       ,GGGGGGGGGGGGGGGGGGGG1     CGGGGG
      ;GGGGGC;              LGGGGGGGLi:  ,:tGGGGGGGG.   CGGGGG
      tGGGGG               CGGGGGG,           fGGGGGG.  CGGGGG
      :GGGGGC.            tGGGGGL              ,GGGGGG  CGGGGG
       1GGGGGGGGGGGf,    .GGGGGG                1GGGGG, CGGGGG
        .LGGGGGGGGGGGGt  .GGGGGC                .GGGGGi CGGGGG
           .ifLGGGGGGGGC  GGGGGG                fGGGGG. CGGGGG
                  ;GGGGG1 iGGGGGG        iiiiiitGGGGGG  CGGGGG
                  ,GGGGGf  fG08GGGt       tGGGGGGGGGG   CGGGGG
         ;iiiiii1LGGGGGG.   iGG08GGGGGfiitfGGGGGGGGC    CGGGGGiiiiiiiiiiiiii.
         LGGGGGGGGGGGGG,      fGG08GGGGGGGGGGGGGGGGC    CGGGGGGGGGGGGGGGGGGG,
         LGGGGGGGGGGGi          :LG08GGGGGGGGGGGGGGGG.  CGGGGGGGGGGGGGGGGGGG,
         ;iiiiiii:                   i8iii:,   ;iiiiii. iiiiiiiiiiiiiiiiiiii.
                                       ;G
                                         ;G@@f     f@@@@@G;
                                         :@@@@@L.0@@@@@@@@@@1
                                          ,@@@@@@@@@@@@@@@@@@@i
                                            :@@@@@@@0   i@@@@@@@1
                                           0@@@@@@0       i@@@@@@@1
                                         .@@@@@@0           i@@@@@@@1
                                         G@@@@@               i@@@@@@@1
                                         t@@@@@0.               i@@@@@@@1
                                          L@@@@@@0.              ,i@@@@@@@1
                                            G@@@@@@0.          :8@@ti@@@@@@@1
                                              G@@@@@@0.      :8@@@@@@;i@@@@@@@i
                                                G@@@@@@0.  :8@@@@@@8.   i@@@@@@f
                                                  G@@@@@@0,G@@@@@@@@@C    L@@@@@.
                                                    G@@@@@@0.G@L,8@@@@@C.0@@@@@G
                                                      G@@@@@@0.   ,8@@@@@@@@@@C
                                                        G@@@@@@0.   ,@@@@@@@G.
                                                          G@@@@@@8i0@@@@@@@@@C.
                                                            G@@@@@@@@@@@G8@@@@@C.
                                                              C@@@@@@@C.  ,8@@@@@C.
                                                                 .,.        ,8@@@@@C.
                                                                              ,8@@@@@G.    i@@@G.
                                                                                ,8@@@@@G.i@@@@@@:
                                                                                  ,8@@@@@@@@@@t
                                                                                    ,8@@@@@@t
                                                                                   i@@@@@@1
                                                                                 :@@@@@@t
                                                                                 C@@@@t
                                                                                  ,i;
        """)

    @classmethod
    def heartbleed(cls):
        print("""
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╣▒▒▒▒▒▒▒╣╬╠▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╣▒▒▒▒▒▒▒╣╬╠▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓╬▒▒▒▒▒▒▒▒╢▓▓▓▓▓▄▒▒▒▒▒▒▒▒▒░▓▓▓▓░▒▒▒▒▒▒▒▒╣╬▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒╣╣▒▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓█▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▒▒▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒╬▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▌▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒╫▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╬▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╫▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▌▒▒▒▒▒▒╠▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒╣▒▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▒▒▒╣▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬▒▒▒▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒╬░▒▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒╣▓▓▓▓▓▓▓▓░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒╠▓▓▓▒▒▒▒▒▒▒╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▒▒╣╬▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒╬▓▓▓▓▓▒▒▒▒▒▒▒▒▒╣▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒╬▓▓▓▓▓▓▓▓▒▒▒▒╣▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒╬▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        """)

class BannersMain(object):

    def options(self):
        import inspect
        from veryprettytable import VeryPrettyTable

        commands = VeryPrettyTable(["Command", "Description"])
        commands.align = "l"
        commands.padding_width = 2

        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr)()])
        return commands

    def randomize(self):
        import inspect
        import random

        banner = []
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__", "randomize"]:
                banner.append(attr)
        getattr(self, random.choice(banner))()
        # return random.choice(banner)

    def nimbus01(self):
        print("""
    ███╗   ██╗██╗███╗   ███╗██████╗ ██╗   ██╗███████╗
    ████╗  ██║██║████╗ ████║██╔══██╗██║   ██║██╔════╝
    ██╔██╗ ██║██║██╔████╔██║██████╔╝██║   ██║███████╗
    ██║╚██╗██║██║██║╚██╔╝██║██╔══██╗██║   ██║╚════██║
    ██║ ╚████║██║██║ ╚═╝ ██║██████╔╝╚██████╔╝███████║
    ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝
        """)

    def nimbus02(self):
        print("""
    ███╗   ██╗██╗███╗   ███╗██████╗ ██╗   ██╗███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
    ████╗  ██║██║████╗ ████║██╔══██╗██║   ██║██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
    ██╔██╗ ██║██║██╔████╔██║██████╔╝██║   ██║███████╗    █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝
    ██║╚██╗██║██║██║╚██╔╝██║██╔══██╗██║   ██║╚════██║    ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗
    ██║ ╚████║██║██║ ╚═╝ ██║██████╔╝╚██████╔╝███████║    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
        """)

    # def nimbus03(self):
    #     print("""
    #  __________  ___  _______  ______   ________  ___  ___  ________
    # |\    ____  \|\  \|\   _  \  _   \|\   __  \|\  \|\  \|\   ____\
    #  \ \  \ \ \  \ \  \ \  \ \ \__\ \  \ \  \|\ /\ \  \\\  \ \  \___|_
    #   \ \  \ \ \  \ \  \ \  \ \ |__| \  \ \   __  \ \  \\\  \ \_____  \
    #    \ \  \ \ \  \ \  \ \  \      \ \  \ \  \|\  \ \  \\\  \|____|\  \
    #     \ \__\ \ \__\ \__\ \__\      \ \__\ \_______\ \_______\____\_\  \
    #      \|__|  \|__|\|__|\|__|       \|__|\|_______|\|_______|\_________\
    #                                                         \|_________|
    #     """)

    def nimbus04(self):
        print("""
     ███▄    █  ██▓ ███▄ ▄███▓ ▄▄▄▄    █    ██   ██████
     ██ ▀█   █ ▓██▒▓██▒▀█▀ ██▒▓█████▄  ██  ▓██▒▒██    ▒
    ▓██  ▀█ ██▒▒██▒▓██    ▓██░▒██▒ ▄██▓██  ▒██░░ ▓██▄
    ▓██▒  ▐▌██▒░██░▒██    ▒██ ▒██░█▀  ▓▓█  ░██░  ▒   ██▒
    ▒██░   ▓██░░██░▒██▒   ░██▒░▓█  ▀█▓▒▒█████▓ ▒██████▒▒
    ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ░  ░░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
    ░ ░░   ░ ▒░ ▒ ░░  ░      ░▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░
       ░   ░ ░  ▒ ░░      ░    ░    ░  ░░░ ░ ░ ░  ░  ░
             ░  ░         ░    ░         ░           ░
                                    ░
        """)

    # def nimbus05(self):
    #     print("""
    #  __  __                  __
    # /\ \/\ \  __            /\ \
    # \ \ `\\ \/\_\    ___ ___\ \ \____  __  __    ____
    #  \ \ , ` \/\ \ /' __` __`\ \ '__`\/\ \/\ \  /',__\
    #   \ \ \`\ \ \ \/\ \/\ \/\ \ \ \L\ \ \ \_\ \/\__, `\
    #    \ \_\ \_\ \_\ \_\ \_\ \_\ \_,__/\ \____/\/\____/
    #     \/_/\/_/\/_/\/_/\/_/\/_/\/___/  \/___/  \/___/
    #     """)

    def nimbus06(self):
        print("""
     _______ __ _______ ______ _______ _______
    |    |  |__|   |   |   __ \   |   |     __|
    |       |  |       |   __ <   |   |__     |
    |__|____|__|__|_|__|______/_______|_______|
        """)

    def nimbus07(self):
        print("""
                  ,,
    `7MN.   `7MF' db  `7MMM.     ,MMF'`7MM'""Yp, `7MMF'   `7MF'.M"'"bgd
      MMN.    M         MMMb    dPMM    MM    Yb   MM       M ,MI    "Y
      M YMb   M `7MM    M YM   ,M MM    MM    dP   MM       M `MMb.
      M  `MN. M   MM    M  Mb  M' MM    MM""'bg.   MM       M   `YMMNq.
      M   `MM.M   MM    M  YM.P'  MM    MM    `Y   MM       M .     `MM
      M     YMM   MM    M  `YM'   MM    MM    ,9   YM.     ,M Mb     dM
    .JML.    YM .JMML..JML. `'  .JMML..JMMmmmd9     `bmmmmd"' P"Ybmmd"
        """)

    def nimbus08(self):
        print("""
     _______ _______ _______ _______ _______ _______
    |\     /|\     /|\     /|\     /|\     /|\     /|
    | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
    | |   | | |   | | |   | | |   | | |   | | |   | |
    | |N  | | |i  | | |M  | | |B  | | |U  | | |S  | |
    | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
    |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
        """)

    def nimbus09(self):
        print("""
     ____ ____ ____ ____ ____ ____
    ||N |||i |||M |||B |||U |||S ||
    ||__|||__|||__|||__|||__|||__||
    |/__\|/__\|/__\|/__\|/__\|/__\|
        """)