import numpy as np
import scipy.io
import pandas as pd
import datetime
import random
import os.path
from os import path
from gurobipy import *
import time
import math
from plotnine import *
import copy
from statistics import mean
from sklearn import preprocessing
from matplotlib import pyplot as plt

County_name = ["Adams","Alexander","Bond","Boone","Brown","Bureau","Calhoun","Carroll","Cass","Champaign","Christian","Clark","Clay","Clinton","Coles","Cook","Crawford","Cumberland","DeKalb","DeWitt","Douglas","DuPage","Edgar","Edwards","Effingham","Fayette","Ford","Franklin","Fulton","Gallatin","Greene","Grundy","Hamilton","Hancock","Hardin","Henderson","Henry","Iroquois","Jackson","Jasper","Jefferson","Jersey","JoDaviess","Johnson","Kane","Kankakee","Kendall","Knox","Lake","LaSalle","Lawrence","Lee","Livingston","Logan","McDonough","McHenry","McLean","Macon","Macoupin","Madison","Marion","Marshall","Mason","Massac","Menard","Mercer","Monroe","Montgomery","Morgan","Moultrie","Ogle","Peoria","Perry","Piatt","Pike","Pope","Pulaski","Putnam","Randolph","Richland","RockIsland","StClair","Saline","Sangamon","Schuyler","Scott","Shelby","Stark","Stephenson","Tazewell","Union","Vermilion","Wabash","Warren","Washington","Wayne","White","Whiteside","Will","Williamson","Winnebago","Woodford",
               "Adams","Allen","Bartholomew","Benton","Blackford","Boone","Brown","Carroll","Cass","Clark","Clay","Clinton","Crawford","Daviess","Dearborn","Decatur","DeKalb","Delaware","Dubois","Elkhart","Fayette","Floyd","Fountain","Franklin","Fulton","Gibson","Grant","Greene","Hamilton","Hancock","Harrison","Hendricks","Henry","Howard","Huntington","Jackson","Jasper","Jay","Jefferson","Jennings","Johnson","Knox","Kosciusko","LaGrange","Lake","LaPorte","Lawrence","Madison","Marion","Marshall","Martin","Miami","Monroe","Montgomery","Morgan","Newton","Noble","Ohio","Orange","Owen","Parke","Perry","Pike","Porter","Posey","Pulaski","Putnam","Randolph","Ripley","Rush","StJoseph","Scott","Shelby","Spencer","Starke","Steuben","Sullivan","Switzerland","Tippecanoe","Tipton","Union","Vanderburgh","Vermillion","Vigo","Wabash","Warren","Warrick","Washington","Wayne","Wells","White","Whitley",
               "Adair","Adams","Allamakee","Appanoose","Audubon","Benton","BlackHawk","Boone","Bremer","Buchanan","BuenaVista","Butler","Calhoun","Carroll","Cass","Cedar","CerroGordo","Cherokee","Chickasaw","Clarke","Clay","Clayton","Clinton","Crawford","Dallas","Davis","Decatur","Delaware","DesMoines","Dickinson","Dubuque","Emmet","Fayette","Floyd","Franklin","Fremont","Greene","Grundy","Guthrie","Hamilton","Hancock","Hardin","Harrison","Henry","Howard","Humboldt","Ida","Iowa","Jackson","Jasper","Jefferson","Johnson","Jones","Keokuk","Kossuth","Lee","Linn","Louisa","Lucas","Lyon","Madison","Mahaska","Marion","Marshall","Mills","Mitchell","Monona","Monroe","Montgomery","Muscatine","O'Brien","Osceola","Page","PaloAlto","Plymouth","Pocahontas","Polk","Pottawattamie","Poweshiek","Ringgold","Sac","Scott","Shelby","Sioux","Story","Tama","Taylor","Union","VanBuren","Wapello","Warren","Washington","Wayne","Webster","Winnebago","Winneshiek","Woodbury","Worth","Wright",
               "Allen","Anderson","Atchison","Barber","Barton","Bourbon","Brown","Butler","Chase","Chautauqua","Cherokee","Cheyenne","Clark","Clay","Cloud","Coffey","Comanche","Cowley","Crawford","Decatur","Dickinson","Doniphan","Douglas","Edwards","Elk","Ellis","Ellsworth","Finney","Ford","Franklin","Geary","Gove","Graham","Grant","Gray","Greeley","Greenwood","Hamilton","Harper","Harvey","Haskell","Hodgeman","Jackson","Jefferson","Jewell","Johnson","Kearny","Kingman","Kiowa","Labette","Lane","Leavenworth","Lincoln","Linn","Logan","Lyon","McPherson","Marion","Marshall","Meade","Miami","Mitchell","Montgomery","Morris","Morton","Nemaha","Neosho","Ness","Norton","Osage","Osborne","Ottawa","Pawnee","Phillips","Pottawatomie","Pratt","Rawlins","Reno","Republic","Rice","Riley","Rooks","Rush","Russell","Saline","Scott","Sedgwick","Seward","Shawnee","Sheridan","Sherman","Smith","Stafford","Stanton","Stevens","Sumner","Thomas","Trego","Wabaunsee","Wallace","Washington","Wichita","Wilson","Woodson","Wyandotte",
               "Adair","Allen","Anderson","Ballard","Barren","Bath","Bell","Boone","Bourbon","Boyd","Boyle","Bracken","Breathitt","Breckinridge","Bullitt","Butler","Caldwell","Calloway","Campbell","Carlisle","Carroll","Carter","Casey","Christian","Clark","Clay","Clinton","Crittenden","Cumberland","Daviess","Edmonson","Elliott","Estill","Fayette","Fleming","Floyd","Franklin","Fulton","Gallatin","Garrard","Grant","Graves","Grayson","Green","Greenup","Hancock","Hardin","Harlan","Harrison","Hart","Henderson","Henry","Hickman","Hopkins","Jackson","Jefferson","Jessamine","Johnson","Kenton","Knott","Knox","Larue","Laurel","Lawrence","Lee","Leslie","Letcher","Lewis","Lincoln","Livingston","Logan","Lyon","McCracken","McCreary","McLean","Madison","Magoffin","Marion","Marshall","Martin","Mason","Meade","Menifee","Mercer","Metcalfe","Monroe","Montgomery","Morgan","Muhlenberg","Nelson","Nicholas","Ohio","Oldham","Owen","Owsley","Pendleton","Perry","Pike","Powell","Pulaski","Robertson","Rockcastle","Rowan","Russell","Scott","Shelby","Simpson","Spencer","Taylor","Todd","Trigg","Trimble","Union","Warren","Washington","Wayne","Webster","Whitley","Wolfe","Woodford",
               "Alcona","Alger","Allegan","Alpena","Antrim","Arenac","Baraga","Barry","Bay","Benzie","Berrien","Branch","Calhoun","Cass","Charlevoix","Cheboygan","Chippewa","Clare","Clinton","Crawford","Delta","Dickinson","Eaton","Emmet","Genesee","Gladwin","Gogebic","GrandTraverse","Gratiot","Hillsdale","Houghton","Huron","Ingham","Ionia","Iosco","Iron","Isabella","Jackson","Kalamazoo","Kalkaska","Kent","Keweenaw","Lake","Lapeer","Leelanau","Lenawee","Livingston","Luce","Mackinac","Macomb","Manistee","Marquette","Mason","Mecosta","Menominee","Midland","Missaukee","Monroe","Montcalm","Montmorency","Muskegon","Newaygo","Oakland","Oceana","Ogemaw","Ontonagon","Osceola","Oscoda","Otsego","Ottawa","PresqueIsle","Roscommon","Saginaw","StClair","StJoseph","Sanilac","Schoolcraft","Shiawassee","Tuscola","VanBuren","Washtenaw","Wayne","Wexford",
               "Aitkin","Anoka","Becker","Beltrami","Benton","BigStone","BlueEarth","Brown","Carlton","Carver","Cass","Chippewa","Chisago","Clay","Clearwater","Cook","Cottonwood","CrowWing","Dakota","Dodge","Douglas","Faribault","Fillmore","Freeborn","Goodhue","Grant","Hennepin","Houston","Hubbard","Isanti","Itasca","Jackson","Kanabec","Kandiyohi","Kittson","Koochiching","LacquiParle","Lake","LakeoftheWoods","LeSueur","Lincoln","Lyon","McLeod","Mahnomen","Marshall","Martin","Meeker","MilleLacs","Morrison","Mower","Murray","Nicollet","Nobles","Norman","Olmsted","OtterTail","Pennington","Pine","Pipestone","Polk","Pope","Ramsey","RedLake","Redwood","Renville","Rice","Rock","Roseau","StLouis","Scott","Sherburne","Sibley","Stearns","Steele","Stevens","Swift","Todd","Traverse","Wabasha","Wadena","Waseca","Washington","Watonwan","Wilkin","Winona","Wright","YellowMedicine",
               "Adair","Andrew","Atchison","Audrain","Barry","Barton","Bates","Benton","Bollinger","Boone","Buchanan","Butler","Caldwell","Callaway","Camden","CapeGirardeau","Carroll","Carter","Cass","Cedar","Chariton","Christian","Clark","Clay","Clinton","Cole","Cooper","Crawford","Dade","Dallas","Daviess","DeKalb","Dent","Douglas","Dunklin","Franklin","Gasconade","Gentry","Greene","Grundy","Harrison","Henry","Hickory","Holt","Howard","Howell","Iron","Jackson","Jasper","Jefferson","Johnson","Knox","Laclede","Lafayette","Lawrence","Lewis","Lincoln","Linn","Livingston","McDonald","Macon","Madison","Maries","Marion","Mercer","Miller","Mississippi","Moniteau","Monroe","Montgomery","Morgan","NewMadrid","Newton","Nodaway","Oregon","Osage","Ozark","Pemiscot","Perry","Pettis","Phelps","Pike","Platte","Polk","Pulaski","Putnam","Ralls","Randolph","Ray","Reynolds","Ripley","StCharles","StClair","SteGenevieve","StFrancois","StLouis","Saline","Schuyler","Scotland","Scott","Shannon","Shelby","Stoddard","Stone","Sullivan","Taney","Texas","Vernon","Warren","Washington","Wayne","Webster","Worth","Wright",
               "Adams","Antelope","Arthur","Banner","Blaine","Boone","BoxButte","Boyd","Brown","Buffalo","Burt","Butler","Cass","Cedar","Chase","Cherry","Cheyenne","Clay","Colfax","Cuming","Custer","Dakota","Dawes","Dawson","Deuel","Dixon","Dodge","Douglas","Dundy","Fillmore","Franklin","Frontier","Furnas","Gage","Garden","Garfield","Gosper","Grant","Greeley","Hall","Hamilton","Harlan","Hayes","Hitchcock","Holt","Hooker","Howard","Jefferson","Johnson","Kearney","Keith","KeyaPaha","Kimball","Knox","Lancaster","Lincoln","Logan","Loup","McPherson","Madison","Merrick","Morrill","Nance","Nemaha","Nuckolls","Otoe","Pawnee","Perkins","Phelps","Pierce","Platte","Polk","RedWillow","Richardson","Rock","Saline","Sarpy","Saunders","ScottsBluff","Seward","Sheridan","Sherman","Sioux","Stanton","Thayer","Thomas","Thurston","Valley","Washington","Wayne","Webster","Wheeler","York",
               "Adams","Barnes","Benson","Billings","Bottineau","Bowman","Burke","Burleigh","Cass","Cavalier","Dickey","Divide","Dunn","Eddy","Emmons","Foster","GoldenValley","GrandForks","Grant","Griggs","Hettinger","Kidder","LaMoure","Logan","McHenry","McIntosh","McKenzie","McLean","Mercer","Morton","Mountrail","Nelson","Oliver","Pembina","Pierce","Ramsey","Ransom","Renville","Richland","Rolette","Sargent","Sheridan","Sioux","Slope","Stark","Steele","Stutsman","Towner","Traill","Walsh","Ward","Wells","Williams",
               "Adams","Allen","Ashland","Ashtabula","Athens","Auglaize","Belmont","Brown","Butler","Carroll","Champaign","Clark","Clermont","Clinton","Columbiana","Coshocton","Crawford","Cuyahoga","Darke","Defiance","Delaware","Erie","Fairfield","Fayette","Franklin","Fulton","Gallia","Geauga","Greene","Guernsey","Hamilton","Hancock","Hardin","Harrison","Henry","Highland","Hocking","Holmes","Huron","Jackson","Jefferson","Knox","Lake","Lawrence","Licking","Logan","Lorain","Lucas","Madison","Mahoning","Marion","Medina","Meigs","Mercer","Miami","Monroe","Montgomery","Morgan","Morrow","Muskingum","Noble","Ottawa","Paulding","Perry","Pickaway","Pike","Portage","Preble","Putnam","Richland","Ross","Sandusky","Scioto","Seneca","Shelby","Stark","Summit","Trumbull","Tuscarawas","Union","VanWert","Vinton","Warren","Washington","Wayne","Williams","Wood","Wyandot",
               "Aurora","Beadle","Bennett","BonHomme","Brookings","Brown","Brule","Buffalo","Butte","Campbell","CharlesMix","Clark","Clay","Codington","Corson","Custer","Davison","Day","Deuel","Dewey","Douglas","Edmunds","FallRiver","Faulk","Grant","Gregory","Haakon","Hamlin","Hand","Hanson","Harding","Hughes","Hutchinson","Hyde","Jackson","Jerauld","Jones","Kingsbury","Lake","Lawrence","Lincoln","Lyman","McCook","McPherson","Marshall","Meade","Mellette","Miner","Minnehaha","Moody","Pennington","Perkins","Potter","Roberts","Sanborn","OglalaLakota","Spink","Stanley","Sully","Todd","Tripp","Turner","Union","Walworth","Yankton","Ziebach",
               "Adams","Ashland","Barron","Bayfield","Brown","Buffalo","Burnett","Calumet","Chippewa","Clark","Columbia","Crawford","Dane","Dodge","Door","Douglas","Dunn","EauClaire","Florence","FondduLac","Forest","Grant","Green","GreenLake","Iowa","Iron","Jackson","Jefferson","Juneau","Kenosha","Kewaunee","LaCrosse","Lafayette","Langlade","Lincoln","Manitowoc","Marathon","Marinette","Marquette","Menominee","Milwaukee","Monroe","Oconto","Oneida","Outagamie","Ozaukee","Pepin","Pierce","Polk","Portage","Price","Racine","Richland","Rock","Rusk","StCroix","Sauk","Sawyer","Shawano","Sheboygan","Taylor","Trempealeau","Vernon","Vilas","Walworth","Washburn","Washington","Waukesha","Waupaca","Waushara","Winnebago","Wood"]
County_FIPS = [17001,17003,17005,17007,17009,17011,17013,17015,17017,17019,17021,17023,17025,17027,17029,17031,17033,17035,17037,17039,17041,17043,17045,17047,17049,17051,17053,17055,17057,17059,17061,17063,17065,17067,17069,17071,17073,17075,17077,17079,17081,17083,17085,17087,17089,17091,17093,17095,17097,17099,17101,17103,17105,17107,17109,17111,17113,17115,17117,17119,17121,17123,17125,17127,17129,17131,17133,17135,17137,17139,17141,17143,17145,17147,17149,17151,17153,17155,17157,17159,17161,17163,17165,17167,17169,17171,17173,17175,17177,17179,17181,17183,17185,17187,17189,17191,17193,17195,17197,17199,17201,17203,
                18001,18003,18005,18007,18009,18011,18013,18015,18017,18019,18021,18023,18025,18027,18029,18031,18033,18035,18037,18039,18041,18043,18045,18047,18049,18051,18053,18055,18057,18059,18061,18063,18065,18067,18069,18071,18073,18075,18077,18079,18081,18083,18085,18087,18089,18091,18093,18095,18097,18099,18101,18103,18105,18107,18109,18111,18113,18115,18117,18119,18121,18123,18125,18127,18129,18131,18133,18135,18137,18139,18141,18143,18145,18147,18149,18151,18153,18155,18157,18159,18161,18163,18165,18167,18169,18171,18173,18175,18177,18179,18181,18183,
                19001,19003,19005,19007,19009,19011,19013,19015,19017,19019,19021,19023,19025,19027,19029,19031,19033,19035,19037,19039,19041,19043,19045,19047,19049,19051,19053,19055,19057,19059,19061,19063,19065,19067,19069,19071,19073,19075,19077,19079,19081,19083,19085,19087,19089,19091,19093,19095,19097,19099,19101,19103,19105,19107,19109,19111,19113,19115,19117,19119,19121,19123,19125,19127,19129,19131,19133,19135,19137,19139,19141,19143,19145,19147,19149,19151,19153,19155,19157,19159,19161,19163,19165,19167,19169,19171,19173,19175,19177,19179,19181,19183,19185,19187,19189,19191,19193,19195,19197,
                20001,20003,20005,20007,20009,20011,20013,20015,20017,20019,20021,20023,20025,20027,20029,20031,20033,20035,20037,20039,20041,20043,20045,20047,20049,20051,20053,20055,20057,20059,20061,20063,20065,20067,20069,20071,20073,20075,20077,20079,20081,20083,20085,20087,20089,20091,20093,20095,20097,20099,20101,20103,20105,20107,20109,20111,20113,20115,20117,20119,20121,20123,20125,20127,20129,20131,20133,20135,20137,20139,20141,20143,20145,20147,20149,20151,20153,20155,20157,20159,20161,20163,20165,20167,20169,20171,20173,20175,20177,20179,20181,20183,20185,20187,20189,20191,20193,20195,20197,20199,20201,20203,20205,20207,20209,
                21001,21003,21005,21007,21009,21011,21013,21015,21017,21019,21021,21023,21025,21027,21029,21031,21033,21035,21037,21039,21041,21043,21045,21047,21049,21051,21053,21055,21057,21059,21061,21063,21065,21067,21069,21071,21073,21075,21077,21079,21081,21083,21085,21087,21089,21091,21093,21095,21097,21099,21101,21103,21105,21107,21109,21111,21113,21115,21117,21119,21121,21123,21125,21127,21129,21131,21133,21135,21137,21139,21141,21143,21145,21147,21149,21151,21153,21155,21157,21159,21161,21163,21165,21167,21169,21171,21173,21175,21177,21179,21181,21183,21185,21187,21189,21191,21193,21195,21197,21199,21201,21203,21205,21207,21209,21211,21213,21215,21217,21219,21221,21223,21225,21227,21229,21231,21233,21235,21237,21239,
                26001,26003,26005,26007,26009,26011,26013,26015,26017,26019,26021,26023,26025,26027,26029,26031,26033,26035,26037,26039,26041,26043,26045,26047,26049,26051,26053,26055,26057,26059,26061,26063,26065,26067,26069,26071,26073,26075,26077,26079,26081,26083,26085,26087,26089,26091,26093,26095,26097,26099,26101,26103,26105,26107,26109,26111,26113,26115,26117,26119,26121,26123,26125,26127,26129,26131,26133,26135,26137,26139,26141,26143,26145,26147,26149,26151,26153,26155,26157,26159,26161,26163,26165,
                27001,27003,27005,27007,27009,27011,27013,27015,27017,27019,27021,27023,27025,27027,27029,27031,27033,27035,27037,27039,27041,27043,27045,27047,27049,27051,27053,27055,27057,27059,27061,27063,27065,27067,27069,27071,27073,27075,27077,27079,27081,27083,27085,27087,27089,27091,27093,27095,27097,27099,27101,27103,27105,27107,27109,27111,27113,27115,27117,27119,27121,27123,27125,27127,27129,27131,27133,27135,27137,27139,27141,27143,27145,27147,27149,27151,27153,27155,27157,27159,27161,27163,27165,27167,27169,27171,27173,
                29001,29003,29005,29007,29009,29011,29013,29015,29017,29019,29021,29023,29025,29027,29029,29031,29033,29035,29037,29039,29041,29043,29045,29047,29049,29051,29053,29055,29057,29059,29061,29063,29065,29067,29069,29071,29073,29075,29077,29079,29081,29083,29085,29087,29089,29091,29093,29095,29097,29099,29101,29103,29105,29107,29109,29111,29113,29115,29117,29119,29121,29123,29125,29127,29129,29131,29133,29135,29137,29139,29141,29143,29145,29147,29149,29151,29153,29155,29157,29159,29161,29163,29165,29167,29169,29171,29173,29175,29177,29179,29181,29183,29185,29186,29187,29189,29195,29197,29199,29201,29203,29205,29207,29209,29211,29213,29215,29217,29219,29221,29223,29225,29227,29229,
                31001,31003,31005,31007,31009,31011,31013,31015,31017,31019,31021,31023,31025,31027,31029,31031,31033,31035,31037,31039,31041,31043,31045,31047,31049,31051,31053,31055,31057,31059,31061,31063,31065,31067,31069,31071,31073,31075,31077,31079,31081,31083,31085,31087,31089,31091,31093,31095,31097,31099,31101,31103,31105,31107,31109,31111,31113,31115,31117,31119,31121,31123,31125,31127,31129,31131,31133,31135,31137,31139,31141,31143,31145,31147,31149,31151,31153,31155,31157,31159,31161,31163,31165,31167,31169,31171,31173,31175,31177,31179,31181,31183,31185,
                38001,38003,38005,38007,38009,38011,38013,38015,38017,38019,38021,38023,38025,38027,38029,38031,38033,38035,38037,38039,38041,38043,38045,38047,38049,38051,38053,38055,38057,38059,38061,38063,38065,38067,38069,38071,38073,38075,38077,38079,38081,38083,38085,38087,38089,38091,38093,38095,38097,38099,38101,38103,38105,
                39001,39003,39005,39007,39009,39011,39013,39015,39017,39019,39021,39023,39025,39027,39029,39031,39033,39035,39037,39039,39041,39043,39045,39047,39049,39051,39053,39055,39057,39059,39061,39063,39065,39067,39069,39071,39073,39075,39077,39079,39081,39083,39085,39087,39089,39091,39093,39095,39097,39099,39101,39103,39105,39107,39109,39111,39113,39115,39117,39119,39121,39123,39125,39127,39129,39131,39133,39135,39137,39139,39141,39143,39145,39147,39149,39151,39153,39155,39157,39159,39161,39163,39165,39167,39169,39171,39173,39175,
                46003,46005,46007,46009,46011,46013,46015,46017,46019,46021,46023,46025,46027,46029,46031,46033,46035,46037,46039,46041,46043,46045,46047,46049,46051,46053,46055,46057,46059,46061,46063,46065,46067,46069,46071,46073,46075,46077,46079,46081,46083,46085,46087,46089,46091,46093,46095,46097,46099,46101,46103,46105,46107,46109,46111,46102,46115,46117,46119,46121,46123,46125,46127,46129,46135,46137,
                55001,55003,55005,55007,55009,55011,55013,55015,55017,55019,55021,55023,55025,55027,55029,55031,55033,55035,55037,55039,55041,55043,55045,55047,55049,55051,55053,55055,55057,55059,55061,55063,55065,55067,55069,55071,55073,55075,55077,55078,55079,55081,55083,55085,55087,55089,55091,55093,55095,55097,55099,55101,55103,55105,55107,55109,55111,55113,55115,55117,55119,55121,55123,55125,55127,55129,55131,55133,55135,55137,55139,55141]

State_County_FIPS = [[17001,17003,17005,17007,17009,17011,17013,17015,17017,17019,17021,17023,17025,17027,17029,17031,17033,17035,17037,17039,17041,17043,17045,17047,17049,17051,17053,17055,17057,17059,17061,17063,17065,17067,17069,17071,17073,17075,17077,17079,17081,17083,17085,17087,17089,17091,17093,17095,17097,17099,17101,17103,17105,17107,17109,17111,17113,17115,17117,17119,17121,17123,17125,17127,17129,17131,17133,17135,17137,17139,17141,17143,17145,17147,17149,17151,17153,17155,17157,17159,17161,17163,17165,17167,17169,17171,17173,17175,17177,17179,17181,17183,17185,17187,17189,17191,17193,17195,17197,17199,17201,17203],
                    [18001,18003,18005,18007,18009,18011,18013,18015,18017,18019,18021,18023,18025,18027,18029,18031,18033,18035,18037,18039,18041,18043,18045,18047,18049,18051,18053,18055,18057,18059,18061,18063,18065,18067,18069,18071,18073,18075,18077,18079,18081,18083,18085,18087,18089,18091,18093,18095,18097,18099,18101,18103,18105,18107,18109,18111,18113,18115,18117,18119,18121,18123,18125,18127,18129,18131,18133,18135,18137,18139,18141,18143,18145,18147,18149,18151,18153,18155,18157,18159,18161,18163,18165,18167,18169,18171,18173,18175,18177,18179,18181,18183],
                    [19001,19003,19005,19007,19009,19011,19013,19015,19017,19019,19021,19023,19025,19027,19029,19031,19033,19035,19037,19039,19041,19043,19045,19047,19049,19051,19053,19055,19057,19059,19061,19063,19065,19067,19069,19071,19073,19075,19077,19079,19081,19083,19085,19087,19089,19091,19093,19095,19097,19099,19101,19103,19105,19107,19109,19111,19113,19115,19117,19119,19121,19123,19125,19127,19129,19131,19133,19135,19137,19139,19141,19143,19145,19147,19149,19151,19153,19155,19157,19159,19161,19163,19165,19167,19169,19171,19173,19175,19177,19179,19181,19183,19185,19187,19189,19191,19193,19195,19197],
                    [20001,20003,20005,20007,20009,20011,20013,20015,20017,20019,20021,20023,20025,20027,20029,20031,20033,20035,20037,20039,20041,20043,20045,20047,20049,20051,20053,20055,20057,20059,20061,20063,20065,20067,20069,20071,20073,20075,20077,20079,20081,20083,20085,20087,20089,20091,20093,20095,20097,20099,20101,20103,20105,20107,20109,20111,20113,20115,20117,20119,20121,20123,20125,20127,20129,20131,20133,20135,20137,20139,20141,20143,20145,20147,20149,20151,20153,20155,20157,20159,20161,20163,20165,20167,20169,20171,20173,20175,20177,20179,20181,20183,20185,20187,20189,20191,20193,20195,20197,20199,20201,20203,20205,20207,20209],
                    [21001,21003,21005,21007,21009,21011,21013,21015,21017,21019,21021,21023,21025,21027,21029,21031,21033,21035,21037,21039,21041,21043,21045,21047,21049,21051,21053,21055,21057,21059,21061,21063,21065,21067,21069,21071,21073,21075,21077,21079,21081,21083,21085,21087,21089,21091,21093,21095,21097,21099,21101,21103,21105,21107,21109,21111,21113,21115,21117,21119,21121,21123,21125,21127,21129,21131,21133,21135,21137,21139,21141,21143,21145,21147,21149,21151,21153,21155,21157,21159,21161,21163,21165,21167,21169,21171,21173,21175,21177,21179,21181,21183,21185,21187,21189,21191,21193,21195,21197,21199,21201,21203,21205,21207,21209,21211,21213,21215,21217,21219,21221,21223,21225,21227,21229,21231,21233,21235,21237,21239],
                    [26001,26003,26005,26007,26009,26011,26013,26015,26017,26019,26021,26023,26025,26027,26029,26031,26033,26035,26037,26039,26041,26043,26045,26047,26049,26051,26053,26055,26057,26059,26061,26063,26065,26067,26069,26071,26073,26075,26077,26079,26081,26083,26085,26087,26089,26091,26093,26095,26097,26099,26101,26103,26105,26107,26109,26111,26113,26115,26117,26119,26121,26123,26125,26127,26129,26131,26133,26135,26137,26139,26141,26143,26145,26147,26149,26151,26153,26155,26157,26159,26161,26163,26165],
                    [27001,27003,27005,27007,27009,27011,27013,27015,27017,27019,27021,27023,27025,27027,27029,27031,27033,27035,27037,27039,27041,27043,27045,27047,27049,27051,27053,27055,27057,27059,27061,27063,27065,27067,27069,27071,27073,27075,27077,27079,27081,27083,27085,27087,27089,27091,27093,27095,27097,27099,27101,27103,27105,27107,27109,27111,27113,27115,27117,27119,27121,27123,27125,27127,27129,27131,27133,27135,27137,27139,27141,27143,27145,27147,27149,27151,27153,27155,27157,27159,27161,27163,27165,27167,27169,27171,27173],
                    [29001,29003,29005,29007,29009,29011,29013,29015,29017,29019,29021,29023,29025,29027,29029,29031,29033,29035,29037,29039,29041,29043,29045,29047,29049,29051,29053,29055,29057,29059,29061,29063,29065,29067,29069,29071,29073,29075,29077,29079,29081,29083,29085,29087,29089,29091,29093,29095,29097,29099,29101,29103,29105,29107,29109,29111,29113,29115,29117,29119,29121,29123,29125,29127,29129,29131,29133,29135,29137,29139,29141,29143,29145,29147,29149,29151,29153,29155,29157,29159,29161,29163,29165,29167,29169,29171,29173,29175,29177,29179,29181,29183,29185,29186,29187,29189,29195,29197,29199,29201,29203,29205,29207,29209,29211,29213,29215,29217,29219,29221,29223,29225,29227,29229],
                    [31001,31003,31005,31007,31009,31011,31013,31015,31017,31019,31021,31023,31025,31027,31029,31031,31033,31035,31037,31039,31041,31043,31045,31047,31049,31051,31053,31055,31057,31059,31061,31063,31065,31067,31069,31071,31073,31075,31077,31079,31081,31083,31085,31087,31089,31091,31093,31095,31097,31099,31101,31103,31105,31107,31109,31111,31113,31115,31117,31119,31121,31123,31125,31127,31129,31131,31133,31135,31137,31139,31141,31143,31145,31147,31149,31151,31153,31155,31157,31159,31161,31163,31165,31167,31169,31171,31173,31175,31177,31179,31181,31183,31185],
                    [38001,38003,38005,38007,38009,38011,38013,38015,38017,38019,38021,38023,38025,38027,38029,38031,38033,38035,38037,38039,38041,38043,38045,38047,38049,38051,38053,38055,38057,38059,38061,38063,38065,38067,38069,38071,38073,38075,38077,38079,38081,38083,38085,38087,38089,38091,38093,38095,38097,38099,38101,38103,38105],
                    [39001,39003,39005,39007,39009,39011,39013,39015,39017,39019,39021,39023,39025,39027,39029,39031,39033,39035,39037,39039,39041,39043,39045,39047,39049,39051,39053,39055,39057,39059,39061,39063,39065,39067,39069,39071,39073,39075,39077,39079,39081,39083,39085,39087,39089,39091,39093,39095,39097,39099,39101,39103,39105,39107,39109,39111,39113,39115,39117,39119,39121,39123,39125,39127,39129,39131,39133,39135,39137,39139,39141,39143,39145,39147,39149,39151,39153,39155,39157,39159,39161,39163,39165,39167,39169,39171,39173,39175],
                    [46003,46005,46007,46009,46011,46013,46015,46017,46019,46021,46023,46025,46027,46029,46031,46033,46035,46037,46039,46041,46043,46045,46047,46049,46051,46053,46055,46057,46059,46061,46063,46065,46067,46069,46071,46073,46075,46077,46079,46081,46083,46085,46087,46089,46091,46093,46095,46097,46099,46101,46103,46105,46107,46109,46111,46102,46115,46117,46119,46121,46123,46125,46127,46129,46135,46137],
                    [55001,55003,55005,55007,55009,55011,55013,55015,55017,55019,55021,55023,55025,55027,55029,55031,55033,55035,55037,55039,55041,55043,55045,55047,55049,55051,55053,55055,55057,55059,55061,55063,55065,55067,55069,55071,55073,55075,55077,55078,55079,55081,55083,55085,55087,55089,55091,55093,55095,55097,55099,55101,55103,55105,55107,55109,55111,55113,55115,55117,55119,55121,55123,55125,55127,55129,55131,55133,55135,55137,55139,55141]]

State_County_FIPS = [[17001,17003,17005,17007,17009,17011,17013,17015,17017,17019,17021,17023,17025,17027,17029,17031,17033,17035,17037,17039,17041,17043,17045,17047,17049,17051,17053,17055,17057,17059,17061,17063,17065,17067,17069,17071,17073,17075,17077,17079,17081,17083,17085,17087,17089,17091,17093,17095,17097,17099,17101,17103,17105,17107,17109,17111,17113,17115,17117,17119,17121,17123,17125,17127,17129,17131,17133,17135,17137,17139,17141,17143,17145,17147,17149,17151,17153,17155,17157,17159,17161,17163,17165,17167,17169,17171,17173,17175,17177,17179,17181,17183,17185,17187,17189,17191,17193,17195,17197,17199,17201,17203],
                    [18001,18003,18005,18007,18009,18011,18013,18015,18017,18019,18021,18023,18025,18027,18029,18031,18033,18035,18037,18039,18041,18043,18045,18047,18049,18051,18053,18055,18057,18059,18061,18063,18065,18067,18069,18071,18073,18075,18077,18079,18081,18083,18085,18087,18089,18091,18093,18095,18097,18099,18101,18103,18105,18107,18109,18111,18113,18115,18117,18119,18121,18123,18125,18127,18129,18131,18133,18135,18137,18139,18141,18143,18145,18147,18149,18151,18153,18155,18157,18159,18161,18163,18165,18167,18169,18171,18173,18175,18177,18179,18181,18183],
                    [19001,19003,19005,19007,19009,19011,19013,19015,19017,19019,19021,19023,19025,19027,19029,19031,19033,19035,19037,19039,19041,19043,19045,19047,19049,19051,19053,19055,19057,19059,19061,19063,19065,19067,19069,19071,19073,19075,19077,19079,19081,19083,19085,19087,19089,19091,19093,19095,19097,19099,19101,19103,19105,19107,19109,19111,19113,19115,19117,19119,19121,19123,19125,19127,19129,19131,19133,19135,19137,19139,19141,19143,19145,19147,19149,19151,19153,19155,19157,19159,19161,19163,19165,19167,19169,19171,19173,19175,19177,19179,19181,19183,19185,19187,19189,19191,19193,19195,19197],
                    [20001,20003,20005,20007,20009,20011,20013,20015,20017,20019,20021,20023,20025,20027,20029,20031,20033,20035,20037,20039,20041,20043,20045,20047,20049,20051,20053,20055,20057,20059,20061,20063,20065,20067,20069,20071,20073,20075,20077,20079,20081,20083,20085,20087,20089,20091,20093,20095,20097,20099,20101,20103,20105,20107,20109,20111,20113,20115,20117,20119,20121,20123,20125,20127,20129,20131,20133,20135,20137,20139,20141,20143,20145,20147,20149,20151,20153,20155,20157,20159,20161,20163,20165,20167,20169,20171,20173,20175,20177,20179,20181,20183,20185,20187,20189,20191,20193,20195,20197,20199,20201,20203,20205,20207,20209],
                    [21001,21003,21005,21007,21009,21011,21013,21015,21017,21019,21021,21023,21025,21027,21029,21031,21033,21035,21037,21039,21041,21043,21045,21047,21049,21051,21053,21055,21057,21059,21061,21063,21065,21067,21069,21071,21073,21075,21077,21079,21081,21083,21085,21087,21089,21091,21093,21095,21097,21099,21101,21103,21105,21107,21109,21111,21113,21115,21117,21119,21121,21123,21125,21127,21129,21131,21133,21135,21137,21139,21141,21143,21145,21147,21149,21151,21153,21155,21157,21159,21161,21163,21165,21167,21169,21171,21173,21175,21177,21179,21181,21183,21185,21187,21189,21191,21193,21195,21197,21199,21201,21203,21205,21207,21209,21211,21213,21215,21217,21219,21221,21223,21225,21227,21229,21231,21233,21235,21237,21239],
                    [26001,26003,26005,26007,26009,26011,26013,26015,26017,26019,26021,26023,26025,26027,26029,26031,26033,26035,26037,26039,26041,26043,26045,26047,26049,26051,26053,26055,26057,26059,26061,26063,26065,26067,26069,26071,26073,26075,26077,26079,26081,26083,26085,26087,26089,26091,26093,26095,26097,26099,26101,26103,26105,26107,26109,26111,26113,26115,26117,26119,26121,26123,26125,26127,26129,26131,26133,26135,26137,26139,26141,26143,26145,26147,26149,26151,26153,26155,26157,26159,26161,26163,26165],
                    [27001,27003,27005,27007,27009,27011,27013,27015,27017,27019,27021,27023,27025,27027,27029,27031,27033,27035,27037,27039,27041,27043,27045,27047,27049,27051,27053,27055,27057,27059,27061,27063,27065,27067,27069,27071,27073,27075,27077,27079,27081,27083,27085,27087,27089,27091,27093,27095,27097,27099,27101,27103,27105,27107,27109,27111,27113,27115,27117,27119,27121,27123,27125,27127,27129,27131,27133,27135,27137,27139,27141,27143,27145,27147,27149,27151,27153,27155,27157,27159,27161,27163,27165,27167,27169,27171,27173],
                    [29001,29003,29005,29007,29009,29011,29013,29015,29017,29019,29021,29023,29025,29027,29029,29031,29033,29035,29037,29039,29041,29043,29045,29047,29049,29051,29053,29055,29057,29059,29061,29063,29065,29067,29069,29071,29073,29075,29077,29079,29081,29083,29085,29087,29089,29091,29093,29095,29097,29099,29101,29103,29105,29107,29109,29111,29113,29115,29117,29119,29121,29123,29125,29127,29129,29131,29133,29135,29137,29139,29141,29143,29145,29147,29149,29151,29153,29155,29157,29159,29161,29163,29165,29167,29169,29171,29173,29175,29177,29179,29181,29183,29185,29186,29187,29189,29195,29197,29199,29201,29203,29205,29207,29209,29211,29213,29215,29217,29219,29221,29223,29225,29227,29229],
                    [31001,31003,31005,31007,31009,31011,31013,31015,31017,31019,31021,31023,31025,31027,31029,31031,31033,31035,31037,31039,31041,31043,31045,31047,31049,31051,31053,31055,31057,31059,31061,31063,31065,31067,31069,31071,31073,31075,31077,31079,31081,31083,31085,31087,31089,31091,31093,31095,31097,31099,31101,31103,31105,31107,31109,31111,31113,31115,31117,31119,31121,31123,31125,31127,31129,31131,31133,31135,31137,31139,31141,31143,31145,31147,31149,31151,31153,31155,31157,31159,31161,31163,31165,31167,31169,31171,31173,31175,31177,31179,31181,31183,31185],
                    [38001,38003,38005,38007,38009,38011,38013,38015,38017,38019,38021,38023,38025,38027,38029,38031,38033,38035,38037,38039,38041,38043,38045,38047,38049,38051,38053,38055,38057,38059,38061,38063,38065,38067,38069,38071,38073,38075,38077,38079,38081,38083,38085,38087,38089,38091,38093,38095,38097,38099,38101,38103,38105],
                    [39001,39003,39005,39007,39009,39011,39013,39015,39017,39019,39021,39023,39025,39027,39029,39031,39033,39035,39037,39039,39041,39043,39045,39047,39049,39051,39053,39055,39057,39059,39061,39063,39065,39067,39069,39071,39073,39075,39077,39079,39081,39083,39085,39087,39089,39091,39093,39095,39097,39099,39101,39103,39105,39107,39109,39111,39113,39115,39117,39119,39121,39123,39125,39127,39129,39131,39133,39135,39137,39139,39141,39143,39145,39147,39149,39151,39153,39155,39157,39159,39161,39163,39165,39167,39169,39171,39173,39175],
                    [46003,46005,46007,46009,46011,46013,46015,46017,46019,46021,46023,46025,46027,46029,46031,46033,46035,46037,46039,46041,46043,46045,46047,46049,46051,46053,46055,46057,46059,46061,46063,46065,46067,46069,46071,46073,46075,46077,46079,46081,46083,46085,46087,46089,46091,46093,46095,46097,46099,46101,46103,46105,46107,46109,46111,46102,46115,46117,46119,46121,46123,46125,46127,46129,46135,46137],
                    [55001,55003,55005,55007,55009,55011,55013,55015,55017,55019,55021,55023,55025,55027,55029,55031,55033,55035,55037,55039,55041,55043,55045,55047,55049,55051,55053,55055,55057,55059,55061,55063,55065,55067,55069,55071,55073,55075,55077,55078,55079,55081,55083,55085,55087,55089,55091,55093,55095,55097,55099,55101,55103,55105,55107,55109,55111,55113,55115,55117,55119,55121,55123,55125,55127,55129,55131,55133,55135,55137,55139,55141]]



state_name = ['IL', 'IN', 'IA', 'KS', 'KY', 'MI', 'MN', 'MO', 'NE', 'ND', 'OH', 'SD', 'WI']
state_index = [17, 18, 19, 20, 21, 26, 27, 29, 31, 38, 39, 46, 55]
#state_name = ['IA']
simulation_input = []
missing_state = []
for state in state_name:
    Name = state
    name_low = Name.lower()
    filename = '***input_data_file'
    array = np.load(filename)
    for arr in array:
        if math.isnan(arr[5]):
            missing_state.append(Name)
        simulation_input.append(arr)
        
        

Year_index = [[] for x in range(40)]
Year_County_index = [[[] for x in range(len(County_FIPS))] for x in range(40)]
Year_State_index = [[[] for x in range(len(state_index))] for x in range(40)]
County_index = [[] for x in range(len(County_FIPS))]
State_index = [[] for x in range(len(state_index))]
State_area = [0 for x in range(len(state_index))]
Year_area = [0 for x in range(40)]
for i in range(len(simulation_input)):
    year = int(simulation_input[i][1])
    Year_index[year-1981].append(i)
    county = int(simulation_input[i][0])
    County_index[County_FIPS.index(county)].append(i)
    Year_County_index[year-1981][County_FIPS.index(county)].append(i)
    state_id = int(county/1000)
    area = int(simulation_input[i][3])
    Year_State_index[year-1981][state_index.index(state_id)].append(i)
    State_index[state_index.index(state_id)].append(i)
    State_area[state_index.index(state_id)] += area
    Year_area[year-1981] += area
    
all_index = [i for i in range(len(simulation_input))]



filename = '***Best Performance Result Record***'
result_array = np.load(filename)
loc = 0
for year in range(40):
    for county in range(len(County_FIPS)):
        seed_rue[year][county] = result_array[loc]; loc+=1
        seed_plant[year][county] = result_array[loc]; loc+=1
        seed_emerge[year][county] = result_array[loc]; loc+=1
        seed_flower[year][county] = result_array[loc]; loc+=1
        seed_grain[year][county] = result_array[loc]; loc+=1
        seed_leaf_size[year][county] = result_array[loc]; loc+=1
        seed_leaf_rate1[year][county] = result_array[loc]; loc+=1
        seed_leaf_rate2[year][county] = result_array[loc]; loc+=1
        seed_leaf_change[year][county] = result_array[loc]; loc+=1
        seed_leaf_decline_date[year][county] = result_array[loc]; loc+=1
        seed_leaf_decline_rate[year][county] = result_array[loc]; loc+=1
        seed_water_supply_rate[year][county] = result_array[loc]; loc+=1
        seed_plant_date[year][county] = result_array[loc]; loc+=1
        rue_rate_f[year][county] = result_array[loc]; loc+=1
        rue_rate_g[year][county] = result_array[loc]; loc+=1
        rue_rate_m[year][county] = result_array[loc]; loc+=1
        water_uptake_rate_f[year][county] = result_array[loc]; loc+=1
        water_uptake_rate_g[year][county] = result_array[loc]; loc+=1
        water_uptake_rate_m[year][county] = result_array[loc]; loc+=1
        seed_drought[year][county] = result_array[loc]; loc+=1
for county in range(len(County_FIPS)):
    soil_runoff_rate[county] = result_array[loc]; loc+=1
    soil_evaporation_rate[county] = result_array[loc]; loc+=1
    waterlogged_level[county] = result_array[loc]; loc+=1
    waterlogged_loss_rate[county] = result_array[loc]; loc+=1
    soil_bestplant[county] = result_array[loc]; loc+=1

soil_runoff_rate_test = copy.deepcopy(soil_runoff_rate)
soil_evaporation_rate_test = copy.deepcopy(soil_evaporation_rate)
waterlogged_level_test = copy.deepcopy(waterlogged_level)
waterlogged_loss_rate_test = copy.deepcopy(waterlogged_loss_rate)
seed_plant_date_test = copy.deepcopy(seed_plant_date)
seed_rue_test = copy.deepcopy(seed_rue)
seed_plant_test = copy.deepcopy(seed_plant)
seed_emerge_test = copy.deepcopy(seed_emerge)
seed_flower_test = copy.deepcopy(seed_flower)
seed_grain_test = copy.deepcopy(seed_grain)
seed_leaf_size_test = copy.deepcopy(seed_leaf_size)
seed_leaf_rate1_test = copy.deepcopy(seed_leaf_rate1)
seed_leaf_rate2_test = copy.deepcopy(seed_leaf_rate2)
seed_leaf_change_test = copy.deepcopy(seed_leaf_change)
seed_leaf_max_test = copy.deepcopy(seed_leaf_max)
seed_leaf_decline_date_test = copy.deepcopy(seed_leaf_decline_date)
seed_leaf_decline_rate_test = copy.deepcopy(seed_leaf_decline_rate)
seed_water_supply_rate_test = copy.deepcopy(seed_water_supply_rate)
water_uptake_rate_f_test = copy.deepcopy(water_uptake_rate_f)
water_uptake_rate_g_test = copy.deepcopy(water_uptake_rate_g)
water_uptake_rate_m_test = copy.deepcopy(water_uptake_rate_m)
rue_rate_f_test = copy.deepcopy(rue_rate_f)
rue_rate_g_test = copy.deepcopy(rue_rate_g)
rue_rate_m_test = copy.deepcopy(rue_rate_m)
seed_drought_test = copy.deepcopy(seed_drought)



def compute_yield_all(year_index_set, seed_county, seed_year):
    obj_up = 0
    obj_down = 0
    for x in year_index_set:
        county = int(simulation_input[x][0])
        env_year = int(simulation_input[x][1])-1981
        test_county = County_FIPS.index(county)
        yield_ob = float(simulation_input[x][2])
        area = int(simulation_input[x][3])
        district = int(simulation_input[x][4])
        plant_density = int(simulation_input[x][5])
        soil_thickness = float(simulation_input[x][7])
        crop_index = float(simulation_input[x][10])
        soil_water = float(simulation_input[x][13]) * seed_drought[env_year][test_county]
        
        input_index = 15

        date = 1
        while date < seed_plant_date[seed_year][seed_county]:
            prcp = simulation_input[x][input_index+1]
            MJ = simulation_input[x][input_index+2]
            if prcp > 20:
                runoff = (prcp/10)**2/soil_runoff_rate[seed_county]
            else:
                runoff = 0
            soil_water = soil_water + prcp - runoff - MJ*soil_evaporation_rate[seed_county]

            if soil_water > waterlogged_level[seed_county]:
                soil_water = waterlogged_level[seed_county]

            date += 1
            input_index += 6

        GDD = 0
        root = 0
        waterlogged_loss_days = 0

        emerge_threshold = seed_plant[seed_year][seed_county]
        flower_threshold = emerge_threshold + seed_emerge[seed_year][seed_county]
        grain_threshold = flower_threshold + seed_flower[seed_year][seed_county]
        mature_threshold = grain_threshold + seed_grain[seed_year][seed_county]
        #plant to emerge
        while GDD < emerge_threshold:
            if input_index+1 >= len(simulation_input[x]): break
            prcp = simulation_input[x][input_index+1]
            MJ = simulation_input[x][input_index+2]
            MGDD = simulation_input[x][input_index+5]
            tmean = (simulation_input[x][input_index+3]+simulation_input[x][input_index+4])/2
            vp_air = simulation_input[x][input_index+6]/1000
            vp_sat = 610.7*10**(7.5*tmean/(237.3+tmean))/1000
            vpd = vp_sat - vp_air
            GDD += MGDD

            if prcp > 20:
                runoff = (prcp/10)**2/soil_runoff_rate[seed_county]
            else:
                runoff = 0

            soil_water = soil_water + prcp - runoff - MJ*soil_evaporation_rate[seed_county] - 2

            if soil_water > waterlogged_level[seed_county]:
                soil_water = waterlogged_level[seed_county]
                waterlogged_loss_days += 1
            #print(MGDD, soil_water)
            date += 1
            input_index += 6
            root += random.randint(10,15)

        leaf_num = round(GDD/seed_leaf_rate1[seed_year][seed_county],2)
        LAI = []
        water = []
        water_demand = []
        water.append(soil_water)
        LAI.append(leaf_num*seed_leaf_size[seed_year][seed_county]*plant_density/4047)

        #emerge to flower (end of junvenile)
        while GDD < flower_threshold:
            if input_index+1 >= len(simulation_input[x]): break
            prcp = simulation_input[x][input_index+1]
            MJ = simulation_input[x][input_index+2]
            MGDD = simulation_input[x][input_index+5]
            tmean = (simulation_input[x][input_index+3]+simulation_input[x][input_index+4])/2
            vp_air = simulation_input[x][input_index+6]/1000
            vp_sat = 610.7*10**(7.5*tmean/(237.3+tmean))/1000
            vpd = vp_sat - vp_air
            GDD += MGDD




            if prcp > 20:
                runoff = (prcp/10)**2/soil_runoff_rate[seed_county]
            else:
                runoff = 0
            soil_water = soil_water + prcp - runoff - MJ*soil_evaporation_rate[seed_county]/leaf_num
            if soil_water < 5:
                soil_water = 5
            water.append(soil_water)
            if soil_water > waterlogged_level[seed_county]:
                soil_water = waterlogged_level[seed_county]
                waterlogged_loss_days += 1
            #print(MGDD, soil_water)
            if leaf_num <= seed_leaf_change[seed_year][seed_county]:
                leaf_num += round(MGDD/seed_leaf_rate1[seed_year][seed_county],2)
                LAI.append(leaf_num*seed_leaf_size[seed_year][seed_county]*plant_density/4047)
            else:
                leaf_num += round(MGDD/seed_leaf_rate2[seed_year][seed_county],2)
                LAI.append(leaf_num*seed_leaf_size[seed_year][seed_county]*1.5*plant_density/4047)

            water_demand.append(seed_rue[seed_year][seed_county]*rue_rate_f[seed_year][seed_county]*LAI[-1]*0.5/0.9/vpd*water_uptake_rate_f[seed_year][seed_county])
            soil_water = soil_water - water_demand[-1]*plant_density/soil_bestplant[seed_county]

            date += 1
            input_index += 6
            if root < 1500: root += random.randint(10,15)

        #flower (end of junvenile) to start grain
        while GDD < grain_threshold:
            if input_index+1 >= len(simulation_input[x]): break
            prcp = simulation_input[x][input_index+1]
            MJ = simulation_input[x][input_index+2]
            MGDD = simulation_input[x][input_index+5]
            tmean = (simulation_input[x][input_index+3]+simulation_input[x][input_index+4])/2
            vp_air = simulation_input[x][input_index+6]/1000
            vp_sat = 610.7*10**(7.5*tmean/(237.3+tmean))/1000
            vpd = vp_sat - vp_air
            GDD += MGDD

            if prcp > 20:
                runoff = (prcp/10)**2/soil_runoff_rate[seed_county]
            else:
                runoff = 0
            soil_water = soil_water + prcp - runoff - MJ*soil_evaporation_rate[seed_county]/leaf_num
            water.append(soil_water)
            if soil_water > waterlogged_level[seed_county]:
                soil_water = waterlogged_level[seed_county]
                waterlogged_loss_days += 1
            #print(MGDD, soil_water)
            if date <= seed_leaf_change[seed_year][seed_county]:
                leaf_num += round(MGDD/seed_leaf_rate1[seed_year][seed_county],2)
                #if leaf_num > seed_leaf_max[seed_year][seed_county]:
                #    leaf_num = seed_leaf_max[seed_year][seed_county]
                LAI.append(leaf_num*seed_leaf_size[seed_year][seed_county]*plant_density/4047)
            else:
                leaf_num += round(MGDD/seed_leaf_rate2[seed_year][seed_county],2)
                LAI.append(leaf_num*seed_leaf_size[seed_year][seed_county]*1.5*plant_density/4047)

            water_demand.append(seed_rue[seed_year][seed_county]*rue_rate_g[seed_year][seed_county]*LAI[-1]*0.5/0.9/vpd*water_uptake_rate_g[seed_year][seed_county])
            soil_water = soil_water - water_demand[-1]*plant_density/soil_bestplant[seed_county]
            date += 1
            input_index += 6
            if root < 1500: root += random.randint(31,33)

        grain_date = date
        day_pass_grain = -seed_leaf_decline_date[seed_year][seed_county]
        LAI_max = LAI[-1]
        yield_test = 0
        while GDD < mature_threshold:
            if input_index+1 >= len(simulation_input[x]): break
            prcp = simulation_input[x][input_index+1]
            MJ = simulation_input[x][input_index+2]
            MGDD = simulation_input[x][input_index+5]
            tmean = (simulation_input[x][input_index+3]+simulation_input[x][input_index+4])/2
            vp_air = simulation_input[x][input_index+6]/1000
            vp_sat = 610.7*10**(7.5*tmean/(237.3+tmean))/1000
            vpd = vp_sat - vp_air
            GDD += MGDD

            if prcp > 20:
                runoff = (prcp/10)**2/soil_runoff_rate[seed_county]
            else:
                runoff = 0
            soil_water = soil_water + prcp - runoff - MJ*soil_evaporation_rate[seed_county]/leaf_num
            if soil_water < 5:
                soil_water = 5
            water.append(soil_water)
            if soil_water > waterlogged_level[seed_county]:
                soil_water = waterlogged_level[seed_county]
                waterlogged_loss_days += 1
            if day_pass_grain > 0:
                if day_pass_grain > 15:
                    #leaf_num = leaf_num - leaf_num * seed_leaf_decline_rate[seed_year][seed_county]*1.2
                    LAI.append(LAI_max -day_pass_grain*seed_leaf_decline_rate[seed_year][seed_county]*1.2)
                else:
                    #leaf_num = leaf_num - leaf_num * seed_leaf_decline_rate[seed_year][seed_county]*0.8
                    LAI.append(LAI_max - day_pass_grain*seed_leaf_decline_rate[seed_year][seed_county]*0.8)
            else:
                LAI.append(LAI[-1])

            water_demand.append(seed_rue[seed_year][seed_county]*rue_rate_m[seed_year][seed_county]*LAI[-1]*0.5/0.9/vpd*water_uptake_rate_m[seed_year][seed_county])

            water_supply = seed_water_supply_rate[seed_year][seed_county] * soil_water
            water_deficit = water_supply/(water_demand[-1]*plant_density/soil_bestplant[seed_county])
            if water_deficit > 1:
                soil_water = soil_water - water_demand[-1]*plant_density/soil_bestplant[seed_county]
                yield_test += seed_rue[seed_year][seed_county]*rue_rate_m[seed_year][seed_county]*LAI[-1]*0.45
            else:
                soil_water = soil_water - water_demand[-1]*water_deficit*plant_density/soil_bestplant[seed_county]
                yield_test += seed_rue[seed_year][seed_county]*rue_rate_m[seed_year][seed_county]*LAI[-1]*0.45*water_deficit
                #if water_deficit > 0.5:
                #    yield_test -= 1/water_deficit*seed_drought[seed_year][seed_county]
            day_pass_grain += 1 
            date += 1
            input_index += 6
            if input_index + 2 >len(simulation_input[x]): break

        yield_test = yield_test/1000/25.4*plant_density*(1-waterlogged_loss_days*waterlogged_loss_rate[seed_county])
        #yield_test = yield_test * crop_index_rate[seed_county]
        
    return(yield_test)
    
    
yield_record = [[0 for j in County_FIPS] for i in range(40)]
area_record = [[0 for j in County_FIPS] for i in range(40)]

for i in range(len(simulation_input)):
    county = int(simulation_input[i][0])
    year = int(simulation_input[i][1])-1981
    yield_ob = float(simulation_input[i][2])
    area = int(simulation_input[i][3])
    yield_record[year][County_FIPS.index(county)] = yield_ob
    area_record[year][County_FIPS.index(county)] = area
    
best_yield_record = copy.deepcopy(yield_record)
best_yield_record_seedyear = [[0  for i in County_FIPS] for j in range(40)]
best_yield_record_seedcounty = [[0  for i in County_FIPS] for j in range(40)]

for county in County_FIPS:
    #start_time = time.time()
    
    county_index = County_FIPS.index(county)
    
    state_num = int(county/1000)
    state_now = state_index.index(state_num)
    
    Current_FIPS = State_County_FIPS[state_now]
    
    max_value = 0
    max_seedyear = -1
    max_seedcounty = -1
    #count = 0
    for env_year in range(1, 40):
        current_yield_record = [[0 for i in County_FIPS]for j in range(40)]
        if best_yield_record[env_year][county_index] > 0:
            env_index = Year_County_index[env_year][county_index]
            for test_county in Current_FIPS:
                test_county_index = County_FIPS.index(test_county)
                for seed_year in range(env_year):
                    current_yield_record[seed_year][test_county_index] = compute_yield_all(env_index, test_county_index, seed_year)
            
            
            for seed_year in range(env_year):
                for test_county in Current_FIPS:
                    test_county_index = County_FIPS.index(test_county)
                    if current_yield_record[seed_year][test_county_index] > best_yield_record[env_year][county_index]:
                        #count += 1
                        best_yield_record[env_year][county_index] = copy.deepcopy(current_yield_record[seed_year][test_county_index])
                        best_yield_record_seedyear[env_year][county_index] = seed_year
                        best_yield_record_seedcounty[env_year][county_index] = test_county_index


    
    #print(str(time.time()-start_time))
    print(str(county))
    #print(count)
        
            
            




































