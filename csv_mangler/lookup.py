"""Lookup tables for mapping into ACS files.

These mappings are derived from ACS geo files:
http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/g20115tn.txt
or (equivalently):
http://www2.census.gov/acs2011_5yr/summaryfile/2007-2011_ACSSF_By_State_By_Sequence_Table_Subset/Tennessee/All_Geographies_Not_Tracts_Block_Groups/g20115tn.csv
"""

"""Mapping of Census logical record numbers to Davidson county districts.
The variable name reflects my mistaken impression that these were 'location' record numbers.
"""
LOCRECNO_TO_DESCRIPTOR = {
    "0000256":"District 1",
    "0000257":"District 2",
    "0000258":"District 3",
    "0000259":"District 4",
    "0000260":"District 5",
    "0000261":"District 6",
    "0000262":"District 7",
    "0000263":"District 8",
    "0000264":"District 9",
    "0000265":"District 10",
    "0000266":"District 11",
    "0000267":"District 12",
    "0000268":"District 13",
    "0000269":"District 14",
    "0000270":"District 15",
    "0000271":"District 16",
    "0000272":"District 17",
    "0000273":"District 18",
    "0000274":"District 19",
    "0000275":"District 20",
    "0000276":"District 21",
    "0000277":"District 22",
    "0000278":"District 23",
    "0000279":"District 24",
    "0000280":"District 25",
    "0000281":"District 26",
    "0000282":"District 27",
    "0000283":"District 28",
    "0000284":"District 29",
    "0000285":"District 30",
    "0000286":"District 31",
    "0000287":"District 32",
    "0000288":"District 33",
    "0000289":"District 34",
    "0000290":"District 35",
}

"""Another mapping of Census LOGRECNO to descriptor.
These are at the partial-tract level, which is more fine-grained than what ended up being used here.
"""
SAMPLE_UNIT_TO_DESCRIPTOR = {
    "010103":"Census Tract 101.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 1",
    "010104":"Census Tract 101.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 1",
    "010105":"Census Tract 101.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 1",
    "012801":"Census Tract 128.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 1",
    "012802":"Census Tract 128.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 1",
    "013100":"Census Tract 131, Nashville-Davidson metropolitan government (balance) (part), District 1",
    "010904":"Census Tract 109.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "011001":"Census Tract 110.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "012701":"Census Tract 127.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "012702":"Census Tract 127.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "012801":"Census Tract 128.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "012802":"Census Tract 128.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "013700":"Census Tract 137 (part), Nashville-Davidson metropolitan government (balance) (part), District 2",
    "010103":"Census Tract 101.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010104":"Census Tract 101.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010105":"Census Tract 101.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010106":"Census Tract 101.06, Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010201":"Census Tract 102.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010202":"Census Tract 102.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010901":"Census Tract 109.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010903":"Census Tract 109.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010904":"Census Tract 109.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "012701":"Census Tract 127.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 3",
    "010202":"Census Tract 102.02 (part), Ridgetop city (part), District 3",
    "010201":"Census Tract 102.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010401":"Census Tract 104.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010402":"Census Tract 104.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010701":"Census Tract 107.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010702":"Census Tract 107.02, Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010801":"Census Tract 108.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010802":"Census Tract 108.02, Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010901":"Census Tract 109.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "010903":"Census Tract 109.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "011002":"Census Tract 110.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "011100":"Census Tract 111 (part), Nashville-Davidson metropolitan government (balance) (part), District 4",
    "011001":"Census Tract 110.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "011300":"Census Tract 113 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "011700":"Census Tract 117 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "011800":"Census Tract 118, Nashville-Davidson metropolitan government (balance) (part), District 5",
    "011900":"Census Tract 119 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "012600":"Census Tract 126, Nashville-Davidson metropolitan government (balance) (part), District 5",
    "012702":"Census Tract 127.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "019300":"Census Tract 193 (part), Nashville-Davidson metropolitan government (balance) (part), District 5",
    "011700":"Census Tract 117 (part), Nashville-Davidson metropolitan government (balance) (part), District 6",
    "011900":"Census Tract 119 (part), Nashville-Davidson metropolitan government (balance) (part), District 6",
    "012100":"Census Tract 121 (part), Nashville-Davidson metropolitan government (balance) (part), District 6",
    "012200":"Census Tract 122, Nashville-Davidson metropolitan government (balance) (part), District 6",
    "019200":"Census Tract 192, Nashville-Davidson metropolitan government (balance) (part), District 6",
    "019300":"Census Tract 193 (part), Nashville-Davidson metropolitan government (balance) (part), District 6",
    "019500":"Census Tract 195 (part), Nashville-Davidson metropolitan government (balance) (part), District 6",
    "011100":"Census Tract 111 (part), Nashville-Davidson metropolitan government (balance) (part), District 7",
    "011200":"Census Tract 112 (part), Nashville-Davidson metropolitan government (balance) (part), District 7",
    "011400":"Census Tract 114 (part), Nashville-Davidson metropolitan government (balance) (part), District 7",
    "011500":"Census Tract 115, Nashville-Davidson metropolitan government (balance) (part), District 7",
    "011600":"Census Tract 116, Nashville-Davidson metropolitan government (balance) (part), District 7",
    "011700":"Census Tract 117 (part), Nashville-Davidson metropolitan government (balance) (part), District 7",
    "012100":"Census Tract 121 (part), Nashville-Davidson metropolitan government (balance) (part), District 7",
    "010903":"Census Tract 109.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011001":"Census Tract 110.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011002":"Census Tract 110.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011100":"Census Tract 111 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011200":"Census Tract 112 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011300":"Census Tract 113 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011400":"Census Tract 114 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "011700":"Census Tract 117 (part), Nashville-Davidson metropolitan government (balance) (part), District 8",
    "010401":"Census Tract 104.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 9",
    "010402":"Census Tract 104.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 9",
    "010601":"Census Tract 106.01, Nashville-Davidson metropolitan government (balance) (part), District 9",
    "010602":"Census Tract 106.02, Nashville-Davidson metropolitan government (balance) (part), District 9",
    "010701":"Census Tract 107.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 9",
    "010202":"Census Tract 102.02 (part), Goodlettsville city (part), District 10",
    "010301":"Census Tract 103.01 (part), Goodlettsville city (part), District 10",
    "010302":"Census Tract 103.02, Goodlettsville city (part), District 10",
    "010303":"Census Tract 103.03, Goodlettsville city (part), District 10",
    "010201":"Census Tract 102.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 10",
    "010202":"Census Tract 102.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 10",
    "010301":"Census Tract 103.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 10",
    "010401":"Census Tract 104.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 10",
    "010801":"Census Tract 108.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 10",
    "010202":"Census Tract 102.02 (part), Ridgetop city (part), District 10",
    "010502":"Census Tract 105.02 (part), Lakewood city, District 11",
    "010501":"Census Tract 105.01, Nashville-Davidson metropolitan government (balance) (part), District 11",
    "010502":"Census Tract 105.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 11",
    "015401":"Census Tract 154.01, Nashville-Davidson metropolitan government (balance) (part), District 11",
    "015404":"Census Tract 154.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 11",
    "015404":"Census Tract 154.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015405":"Census Tract 154.05, Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015609":"Census Tract 156.09 (part), Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015610":"Census Tract 156.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015622":"Census Tract 156.22, Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015623":"Census Tract 156.23 (part), Nashville-Davidson metropolitan government (balance) (part), District 12",
    "015610":"Census Tract 156.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015612":"Census Tract 156.12 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015617":"Census Tract 156.17 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015619":"Census Tract 156.19 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015624":"Census Tract 156.24 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015625":"Census Tract 156.25, Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015700":"Census Tract 157 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015802":"Census Tract 158.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015803":"Census Tract 158.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015804":"Census Tract 158.04, Nashville-Davidson metropolitan government (balance) (part), District 13",
    "980100":"Census Tract 9801 (part), Nashville-Davidson metropolitan government (balance) (part), District 13",
    "015300":"Census Tract 153 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015402":"Census Tract 154.02, Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015404":"Census Tract 154.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015501":"Census Tract 155.01, Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015502":"Census Tract 155.02, Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015609":"Census Tract 156.09 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015610":"Census Tract 156.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015623":"Census Tract 156.23 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015624":"Census Tract 156.24 (part), Nashville-Davidson metropolitan government (balance) (part), District 14",
    "015100":"Census Tract 151, Nashville-Davidson metropolitan government (balance) (part), District 15",
    "015200":"Census Tract 152, Nashville-Davidson metropolitan government (balance) (part), District 15",
    "015300":"Census Tract 153 (part), Nashville-Davidson metropolitan government (balance) (part), District 15",
    "015803":"Census Tract 158.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 15",
    "015900":"Census Tract 159 (part), Nashville-Davidson metropolitan government (balance) (part), District 15",
    "019600":"Census Tract 196 (part), Nashville-Davidson metropolitan government (balance) (part), District 15",
    "015700":"Census Tract 157 (part), Nashville-Davidson metropolitan government (balance) (part), District 16",
    "015802":"Census Tract 158.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 16",
    "015900":"Census Tract 159 (part), Nashville-Davidson metropolitan government (balance) (part), District 16",
    "017200":"Census Tract 172 (part), Nashville-Davidson metropolitan government (balance) (part), District 16",
    "017300":"Census Tract 173, Nashville-Davidson metropolitan government (balance) (part), District 16",
    "017401":"Census Tract 174.01, Nashville-Davidson metropolitan government (balance) (part), District 16",
    "017402":"Census Tract 174.02, Nashville-Davidson metropolitan government (balance) (part), District 16",
    "017500":"Census Tract 175, Nashville-Davidson metropolitan government (balance) (part), District 16",
    "019006":"Census Tract 190.06 (part), Nashville-Davidson metropolitan government (balance) (part), District 16",
    "980200":"Census Tract 9802, Nashville-Davidson metropolitan government (balance) (part), District 16",
    "016100":"Census Tract 161 (part), Berry Hill city, District 17",
    "017100":"Census Tract 171 (part), Berry Hill city, District 17",
    "017200":"Census Tract 172 (part), Berry Hill city, District 17",
    "017800":"Census Tract 178 (part), Berry Hill city, District 17",
    "014800":"Census Tract 148, Nashville-Davidson metropolitan government (balance) (part), District 17",
    "015900":"Census Tract 159 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "016000":"Census Tract 160, Nashville-Davidson metropolitan government (balance) (part), District 17",
    "016100":"Census Tract 161 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "016200":"Census Tract 162 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "017000":"Census Tract 170 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "017100":"Census Tract 171 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "017200":"Census Tract 172 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "017800":"Census Tract 178 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "019600":"Census Tract 196 (part), Nashville-Davidson metropolitan government (balance) (part), District 17",
    "016300":"Census Tract 163 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "016400":"Census Tract 164 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "016500":"Census Tract 165 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "016600":"Census Tract 166 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "016800":"Census Tract 168 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "016900":"Census Tract 169, Nashville-Davidson metropolitan government (balance) (part), District 18",
    "017000":"Census Tract 170 (part), Nashville-Davidson metropolitan government (balance) (part), District 18",
    "013700":"Census Tract 137 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "013900":"Census Tract 139 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "014200":"Census Tract 142, Nashville-Davidson metropolitan government (balance) (part), District 19",
    "014400":"Census Tract 144 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "016200":"Census Tract 162 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "016300":"Census Tract 163 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "016400":"Census Tract 164 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "019400":"Census Tract 194, Nashville-Davidson metropolitan government (balance) (part), District 19",
    "019500":"Census Tract 195 (part), Nashville-Davidson metropolitan government (balance) (part), District 19",
    "013000":"Census Tract 130, Nashville-Davidson metropolitan government (balance) (part), District 20",
    "013201":"Census Tract 132.01, Nashville-Davidson metropolitan government (balance) (part), District 20",
    "013202":"Census Tract 132.02, Nashville-Davidson metropolitan government (balance) (part), District 20",
    "013300":"Census Tract 133, Nashville-Davidson metropolitan government (balance) (part), District 20",
    "013602":"Census Tract 136.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 20",
    "018101":"Census Tract 181.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 20",
    "018201":"Census Tract 182.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 20",
    "018301":"Census Tract 183.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 20",
    "013500":"Census Tract 135 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "013601":"Census Tract 136.01, Nashville-Davidson metropolitan government (balance) (part), District 21",
    "013602":"Census Tract 136.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "013700":"Census Tract 137 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "013800":"Census Tract 138, Nashville-Davidson metropolitan government (balance) (part), District 21",
    "013900":"Census Tract 139 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "014300":"Census Tract 143, Nashville-Davidson metropolitan government (balance) (part), District 21",
    "014400":"Census Tract 144 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "016500":"Census Tract 165 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "016600":"Census Tract 166 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "016800":"Census Tract 168 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "019500":"Census Tract 195 (part), Nashville-Davidson metropolitan government (balance) (part), District 21",
    "018202":"Census Tract 182.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018301":"Census Tract 183.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018401":"Census Tract 184.01, Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018404":"Census Tract 184.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018405":"Census Tract 184.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018407":"Census Tract 184.07 (part), Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018409":"Census Tract 184.09, Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018410":"Census Tract 184.10, Nashville-Davidson metropolitan government (balance) (part), District 22",
    "018000":"Census Tract 180 (part), Belle Meade city, District 23",
    "018500":"Census Tract 185 (part), Belle Meade city, District 23",
    "018102":"Census Tract 181.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 23",
    "018201":"Census Tract 182.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 23",
    "018202":"Census Tract 182.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 23",
    "018203":"Census Tract 182.03, Nashville-Davidson metropolitan government (balance) (part), District 23",
    "018404":"Census Tract 184.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 23",
    "018500":"Census Tract 185 (part), Nashville-Davidson metropolitan government (balance) (part), District 23",
    "013400":"Census Tract 134, Nashville-Davidson metropolitan government (balance) (part), District 24",
    "013500":"Census Tract 135 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "016700":"Census Tract 167 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "017901":"Census Tract 179.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "018000":"Census Tract 180 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "018101":"Census Tract 181.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "018102":"Census Tract 181.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 24",
    "016700":"Census Tract 167 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "017701":"Census Tract 177.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "017702":"Census Tract 177.02, Nashville-Davidson metropolitan government (balance) (part), District 25",
    "017800":"Census Tract 178 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "017901":"Census Tract 179.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "017902":"Census Tract 179.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "018000":"Census Tract 180 (part), Nashville-Davidson metropolitan government (balance) (part), District 25",
    "018801":"Census Tract 188.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 26",
    "018901":"Census Tract 189.01, Nashville-Davidson metropolitan government (balance) (part), District 26",
    "018902":"Census Tract 189.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 26",
    "018905":"Census Tract 189.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 26",
    "019004":"Census Tract 190.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 26",
    "019005":"Census Tract 190.05, Nashville-Davidson metropolitan government (balance) (part), District 26",
    "019006":"Census Tract 190.06 (part), Nashville-Davidson metropolitan government (balance) (part), District 26",
    "018801":"Census Tract 188.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 27",
    "018902":"Census Tract 189.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 27",
    "018904":"Census Tract 189.04, Nashville-Davidson metropolitan government (balance) (part), District 27",
    "018905":"Census Tract 189.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 27",
    "019105":"Census Tract 191.05, Nashville-Davidson metropolitan government (balance) (part), District 27",
    "019106":"Census Tract 191.06, Nashville-Davidson metropolitan government (balance) (part), District 27",
    "015613":"Census Tract 156.13, Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015614":"Census Tract 156.14, Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015615":"Census Tract 156.15, Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015626":"Census Tract 156.26 (part), Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015627":"Census Tract 156.27, Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015700":"Census Tract 157 (part), Nashville-Davidson metropolitan government (balance) (part), District 28",
    "980100":"Census Tract 9801 (part), Nashville-Davidson metropolitan government (balance) (part), District 28",
    "015612":"Census Tract 156.12 (part), Nashville-Davidson metropolitan government (balance) (part), District 29",
    "015617":"Census Tract 156.17 (part), Nashville-Davidson metropolitan government (balance) (part), District 29",
    "015618":"Census Tract 156.18, Nashville-Davidson metropolitan government (balance) (part), District 29",
    "015620":"Census Tract 156.20 (part), Nashville-Davidson metropolitan government (balance) (part), District 29",
    "019003":"Census Tract 190.03, Nashville-Davidson metropolitan government (balance) (part), District 30",
    "019004":"Census Tract 190.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 30",
    "019108":"Census Tract 191.08, Nashville-Davidson metropolitan government (balance) (part), District 30",
    "019109":"Census Tract 191.09, Nashville-Davidson metropolitan government (balance) (part), District 30",
    "019110":"Census Tract 191.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 30",
    "019111":"Census Tract 191.11 (part), Nashville-Davidson metropolitan government (balance) (part), District 30",
    "018700":"Census Tract 187 (part), Nashville-Davidson metropolitan government (balance) (part), District 31",
    "018801":"Census Tract 188.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 31",
    "018803":"Census Tract 188.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 31",
    "018804":"Census Tract 188.04, Nashville-Davidson metropolitan government (balance) (part), District 31",
    "019112":"Census Tract 191.12 (part), Nashville-Davidson metropolitan government (balance) (part), District 31",
    "019114":"Census Tract 191.14 (part), Nashville-Davidson metropolitan government (balance) (part), District 31",
    "019115":"Census Tract 191.15, Nashville-Davidson metropolitan government (balance) (part), District 31",
    "019116":"Census Tract 191.16, Nashville-Davidson metropolitan government (balance) (part), District 31",
    "015628":"Census Tract 156.28 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "015629":"Census Tract 156.29 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "015630":"Census Tract 156.30, Nashville-Davidson metropolitan government (balance) (part), District 32",
    "015631":"Census Tract 156.31 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019110":"Census Tract 191.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019111":"Census Tract 191.11 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019112":"Census Tract 191.12 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019114":"Census Tract 191.14 (part), Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019117":"Census Tract 191.17, Nashville-Davidson metropolitan government (balance) (part), District 32",
    "019118":"Census Tract 191.18, Nashville-Davidson metropolitan government (balance) (part), District 32",
    "015610":"Census Tract 156.10 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015619":"Census Tract 156.19 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015620":"Census Tract 156.20 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015626":"Census Tract 156.26 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015628":"Census Tract 156.28 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015629":"Census Tract 156.29 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "015631":"Census Tract 156.31 (part), Nashville-Davidson metropolitan government (balance) (part), District 33",
    "018601":"Census Tract 186.01 (part), Forest Hills city, District 34",
    "018602":"Census Tract 186.02 (part), Forest Hills city, District 34",
    "018700":"Census Tract 187 (part), Forest Hills city, District 34",
    "017701":"Census Tract 177.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "017800":"Census Tract 178 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "017901":"Census Tract 179.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "017902":"Census Tract 179.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018404":"Census Tract 184.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018405":"Census Tract 184.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018500":"Census Tract 185 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018601":"Census Tract 186.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018602":"Census Tract 186.02 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018700":"Census Tract 187 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "018803":"Census Tract 188.03 (part), Nashville-Davidson metropolitan government (balance) (part), District 34",
    "017701":"Census Tract 177.01 (part), Oak Hill city, District 34",
    "017800":"Census Tract 178 (part), Oak Hill city, District 34",
    "018700":"Census Tract 187 (part), Oak Hill city, District 34",
    "018301":"Census Tract 183.01 (part), Nashville-Davidson metropolitan government (balance) (part), District 35",
    "018302":"Census Tract 183.02, Nashville-Davidson metropolitan government (balance) (part), District 35",
    "018404":"Census Tract 184.04 (part), Nashville-Davidson metropolitan government (balance) (part), District 35",
    "018405":"Census Tract 184.05 (part), Nashville-Davidson metropolitan government (balance) (part), District 35",
    "018407":"Census Tract 184.07 (part), Nashville-Davidson metropolitan government (balance) (part), District 35",
    "018408":"Census Tract 184.08, Nashville-Davidson metropolitan government (balance) (part), District 35",
}

"""Mapping of partial Census tract LOGRECNO to the LOGRECNO of the district to which the tract belongs.
Not actually used here.
"""
SAMPLE_UNIT_TO_DISTRICT = {
    "0003540":90038,
    "0003541":90038,
    "0003542":90038,
    "0003543":90038,
    "0003544":90038,
    "0003545":90038,
    "0003546":90228,
    "0003547":90228,
    "0003548":90228,
    "0003549":90228,
    "0003550":90228,
    "0003551":90228,
    "0003552":90228,
    "0003553":90418,
    "0003554":90418,
    "0003555":90418,
    "0003556":90418,
    "0003557":90418,
    "0003558":90418,
    "0003559":90418,
    "0003560":90418,
    "0003561":90418,
    "0003562":90418,
    "0003563":90418,
    "0003564":90608,
    "0003565":90608,
    "0003566":90608,
    "0003567":90608,
    "0003568":90608,
    "0003569":90608,
    "0003570":90608,
    "0003571":90608,
    "0003572":90608,
    "0003573":90608,
    "0003574":90608,
    "0003575":90798,
    "0003576":90798,
    "0003577":90798,
    "0003578":90798,
    "0003579":90798,
    "0003580":90798,
    "0003581":90798,
    "0003582":90798,
    "0003583":90988,
    "0003584":90988,
    "0003585":90988,
    "0003586":90988,
    "0003587":90988,
    "0003588":90988,
    "0003589":90988,
    "0003590":91178,
    "0003591":91178,
    "0003592":91178,
    "0003593":91178,
    "0003594":91178,
    "0003595":91178,
    "0003596":91178,
    "0003597":91368,
    "0003598":91368,
    "0003599":91368,
    "0003600":91368,
    "0003601":91368,
    "0003602":91368,
    "0003603":91368,
    "0003604":91368,
    "0003605":91558,
    "0003606":91558,
    "0003607":91558,
    "0003608":91558,
    "0003609":91558,
    "0003610":91748,
    "0003611":91748,
    "0003612":91748,
    "0003613":91748,
    "0003614":91748,
    "0003615":91748,
    "0003616":91748,
    "0003617":91748,
    "0003618":91748,
    "0003619":91748,
    "0003620":91938,
    "0003621":91938,
    "0003622":91938,
    "0003623":91938,
    "0003624":91938,
    "0003625":92128,
    "0003626":92128,
    "0003627":92128,
    "0003628":92128,
    "0003629":92128,
    "0003630":92128,
    "0003631":92318,
    "0003632":92318,
    "0003633":92318,
    "0003634":92318,
    "0003635":92318,
    "0003636":92318,
    "0003637":92318,
    "0003638":92318,
    "0003639":92318,
    "0003640":92318,
    "0003641":92318,
    "0003642":92508,
    "0003643":92508,
    "0003644":92508,
    "0003645":92508,
    "0003646":92508,
    "0003647":92508,
    "0003648":92508,
    "0003649":92508,
    "0003650":92508,
    "0003651":92698,
    "0003652":92698,
    "0003653":92698,
    "0003654":92698,
    "0003655":92698,
    "0003656":92698,
    "0003657":92888,
    "0003658":92888,
    "0003659":92888,
    "0003660":92888,
    "0003661":92888,
    "0003662":92888,
    "0003663":92888,
    "0003664":92888,
    "0003665":92888,
    "0003666":92888,
    "0003667":93078,
    "0003668":93078,
    "0003669":93078,
    "0003670":93078,
    "0003671":93078,
    "0003672":93078,
    "0003673":93078,
    "0003674":93078,
    "0003675":93078,
    "0003676":93078,
    "0003677":93078,
    "0003678":93078,
    "0003679":93078,
    "0003680":93078,
    "0003681":93268,
    "0003682":93268,
    "0003683":93268,
    "0003684":93268,
    "0003685":93268,
    "0003686":93268,
    "0003687":93268,
    "0003688":93458,
    "0003689":93458,
    "0003690":93458,
    "0003691":93458,
    "0003692":93458,
    "0003693":93458,
    "0003694":93458,
    "0003695":93458,
    "0003696":93458,
    "0003697":93648,
    "0003698":93648,
    "0003699":93648,
    "0003700":93648,
    "0003701":93648,
    "0003702":93648,
    "0003703":93648,
    "0003704":93648,
    "0003705":93838,
    "0003706":93838,
    "0003707":93838,
    "0003708":93838,
    "0003709":93838,
    "0003710":93838,
    "0003711":93838,
    "0003712":93838,
    "0003713":93838,
    "0003714":93838,
    "0003715":93838,
    "0003716":93838,
    "0003717":94028,
    "0003718":94028,
    "0003719":94028,
    "0003720":94028,
    "0003721":94028,
    "0003722":94028,
    "0003723":94028,
    "0003724":94028,
    "0003725":94218,
    "0003726":94218,
    "0003727":94218,
    "0003728":94218,
    "0003729":94218,
    "0003730":94218,
    "0003731":94218,
    "0003732":94218,
    "0003733":94408,
    "0003734":94408,
    "0003735":94408,
    "0003736":94408,
    "0003737":94408,
    "0003738":94408,
    "0003739":94408,
    "0003740":94598,
    "0003741":94598,
    "0003742":94598,
    "0003743":94598,
    "0003744":94598,
    "0003745":94598,
    "0003746":94598,
    "0003747":94940,
    "0003748":94940,
    "0003749":94940,
    "0003750":94940,
    "0003751":94940,
    "0003752":94940,
    "0003753":94940,
    "0003754":95130,
    "0003755":95130,
    "0003756":95130,
    "0003757":95130,
    "0003758":95130,
    "0003759":95130,
    "0003760":95320,
    "0003761":95320,
    "0003762":95320,
    "0003763":95320,
    "0003764":95320,
    "0003765":95320,
    "0003766":95320,
    "0003767":95510,
    "0003768":95510,
    "0003769":95510,
    "0003770":95510,
    "0003771":95700,
    "0003772":95700,
    "0003773":95700,
    "0003774":95700,
    "0003775":95700,
    "0003776":95700,
    "0003777":95890,
    "0003778":95890,
    "0003779":95890,
    "0003780":95890,
    "0003781":95890,
    "0003782":95890,
    "0003783":95890,
    "0003784":95890,
    "0003785":96080,
    "0003786":96080,
    "0003787":96080,
    "0003788":96080,
    "0003789":96080,
    "0003790":96080,
    "0003791":96080,
    "0003792":96080,
    "0003793":96080,
    "0003794":96080,
    "0003795":96270,
    "0003796":96270,
    "0003797":96270,
    "0003798":96270,
    "0003799":96270,
    "0003800":96270,
    "0003801":96270,
    "0003802":96460,
    "0003803":96460,
    "0003804":96460,
    "0003805":96460,
    "0003806":96460,
    "0003807":96460,
    "0003808":96460,
    "0003809":96460,
    "0003810":96460,
    "0003811":96460,
    "0003812":96460,
    "0003813":96460,
    "0003814":96460,
    "0003815":96460,
    "0003816":96460,
    "0003817":96460,
    "0003818":96460,
    "0003819":96650,
    "0003820":96650,
    "0003821":96650,
    "0003822":96650,
    "0003823":96650,
    "0003824":96650,
    }