import logging
import struct
import random
import time

from src.callback.base import Base

logger = logging.getLogger('chewang')


class CallBack(Base):
    vehicle_list = ['56EZPWQA', '8JBUK42X', '8JBUPIWF', '56F4B0BT', 'WFEHKPL3', '8JBQ3BXC', '56EUHCKX', '8JBV9VXP',
                    '56F7ATDD', 'WFDBYLAG', '56EPHXH8', '560ZLCCM', '8JBQIP7S', 'WFGLEPRU', '8JBNPPHY', '56ERNZSZ',
                    '56ED829G', '56EWZBON', '56ERW2VD', '56F0LMGO', '56EO5T4F', '560N8BWN', '8JBJV35G', '56F4MPSW',
                    '8JBRNK6Y', 'WFH8IRRL', 'WFFCM79P', '56EW2VQQ', 'WFF9BRKH', '56EFIUMO', '56ESN9PW', 'WFE6NF8E',
                    'WFK4IAB1', '8JBQPU7O', '8JBLGURY', 'WFCVXBM3', '56EINHS7', '56F30RRJ', '8JBRG1BV', '56EDEM7F',
                    '8JBV6JLQ', '56F1H824', '56EQAQ3D', '56EZLIQT', '56ELXR9O', '56F7S10K', '56EEI4I8', '8JBNMZO9',
                    '560VX62Z', '56EKJ1UB', '8JBUFGDM', '8JBKYV7P', '8JBV6L9M', 'WFEFH4EG', '56F4USD2', '56EI6JO1',
                    '56EFO8SD', '56F0XPKW', 'WFGT1AF7', '56ERJNS9', '8JBM9FHY', '8JBV0MNT', '560FEEX5', '56EFNY78',
                    '56F55VLH', '56F59WMZ', '560SNG42', '56EUBCSC', '56ER8I45', 'WFFEZNGR', '56EILP12', '56EX18QQ',
                    '56EIDCTF', 'WFI3S7LE', '8JBP55SL', '56EXPUVB', '56EY4PO3', '56F7AJV6', '56EDV62H', '56F4LTNA',
                    '8JBLRD0K', '8JBSR333', '56EYAXWH', '56ESCQU7', '560G65GB', '56ECYQ3A', '56F4Q99C', '56EMGE2L',
                    '8JBR1Y04', '56EHMX3V', '56F5EFEA', '56EODFXI', '56EK14B1', '56EYQYCP', '560ZSR0E', '56F4ERCS',
                    '56EF5AF6', '8JBQJA75', '56EHX362', '56EHCYKA', '56ET2LA0', '56F8JZLI', '560KFYM8', 'WFH2HPBT',
                    'WFDMKR73', '56ED7S23', '8JBT0VSE', '56F3JMKF', '56F54VRY', '8JBU6V8V', '56EGJ292', '56ED211B',
                    '56EJSE4I', '56EG1ZS2', '56EGAFLU', '560XYT77', 'WFK042TA', '56EOTVNT', '8JBO6C57', '56EIC1FC',
                    '56EOGWHX', '56EO3ULW', '56EH54SY', '56F4FYQV', '8JBKFTOO', '56F09LRT', '560ZMF08', '56ES8TJC',
                    '56F4MPE9', '56ETCTNF', '56EFN4OJ', '56EPU7DO', '56EN8NOY', '56EUL6NT', '8JBRZZ6C', '56EQ37Y3',
                    '560RK3FH', '56F6Z8J1', '56EE1TMC', '56EHNRTE', '560VPMJD', '8JBQUM5X', '56EZMO8A', '8JBL1ICJ',
                    '56EGZZAT', '56EVEP5T', '56EDO78O', '56EIHOW9', '8JBOCZF3', '56F5R6MC', '560JAU56', '56EPVHX1',
                    '56ENUX2F', '56EBQK03', '56EBV1CB', '560Q9FXN', '56F6CQQL', '56EF2DIG', '56EU334L', '56EF3UAR',
                    '56EIB67H', '8JBVBXJ9', '56EGGON0', '56F1Z26P', '56F6MA25', '56EZYL6L', '56EQ90XT', '56EYE1WY',
                    '56EP2F15', '8JBO1M53', '560L659N', '56F051GW', 'WFEUZ5LY', '56EE2EX0', '56F2MLET', '560PYDEL',
                    '560P8LYC', '56F7RSF3', 'WFEDSMPD', '56F80IUD', '8JBO0OE4', '56EL5SM0', '56F1Q5F3', '56EFTJS5',
                    '56EY2IA2', '560VJ3RW', '8JBWGFX4', '56EVP3GG', 'WFKC7AF3', '56EIADW6', '56ETG28C', '8JBO04TT',
                    'WFGH9KQQ', 'WFEFKN6F', '56EV6L3O', '56EMJNTY', '56ETLNLI', '56EVMCZC', '8JBM0G52', '56EZZM2Z',
                    '56EXDYKY', 'WFI1V595', '8JBSKOR8', '8JBOYZLO', '560EL9D7', '56EOJTJ5', '56EWEEPV', 'WFDDD5C7',
                    '560I52RM', '56EOQORR', '56EXFT4A', '56ED2P3V', '8JBU4VYF', 'WFIQYDFE', '8JBOFL3X', '56F6SYD7',
                    '56ENEX4P', '8JBS7AGM', '56F4NC0W', '56EFDT8Q', '56F1EKKV', '56EX7H06', '56EGU1KO', '56EWEJWZ',
                    '56F6G8LB', '56F6EGAU', '56F4PE8M', '56F7WSF0', '56EVP884', '560OO4M5', 'WFK0GL5Q', '56EH30YH',
                    '56F1S0UI', 'WFIBV018', '56F56OSP', '8JBKKJWP', '56EHPKUA', 'WFD6VDUQ', '56EQF50S', '56EC7RRE',
                    'WFGXPZ19', 'WFIN3LAO', '560G22D1', '56EVV1UK', '8JBKDP6P', '56F4IN4D', '8JBN8PRA', '56EUONSW',
                    '8JBJYG5A', '56F6LH84', '56EE56UF', '56EF3LWH', 'WFFD5CA3', '56ET6IA1', '56ERLHYE', '56ENMP76',
                    '56EXUJG2', '56ENQ52J', '56F1M0K5', '563NNQLO', '56EZ7QZW', '56F39QU5', '8JBTV8FN', 'WFFHCX2X',
                    '560Q8CEV', '560L2F5N', '56EG1VO3', '8JBPHWTY', '56EJ302Y', '56F39HFJ', '56EGXR9N', '8JBPYUMD',
                    '560XTYJY', '8JBV6XO9', '56F4NNS5', 'WFK34DMM', '56ELQBR4', '8JBPO4FR', '8JBL9DE3', '8JBV7GKS',
                    '8JBVQGEE', 'WFEF99IQ', '56EGPY60', '56EDAKXU', '56EH9M60', '560XYV6R', 'WFDO92SK', '56EGSAKY',
                    '56ED6C7W', '56ETS65A', '56EYN11B', '8JBTX06J', 'WFF6OFSN', '8JBV9KBF', '560D0Z1Y', '560LB2BB',
                    '56EUNF40', '56EQ50WI', '8JBNS6HY', '56EKKR3T', '56EZAA5J', '56ETJGUQ', 'WFI028DR', '56EE42R2',
                    '8JBQRT59', '56EI5JAZ', 'WFJP0WWX', '56F2U63W', '56EJXQW1', '56F1DN50', '56EI83ZU', 'WFD5FALU',
                    'WFFENHH3', '8JBPVHNL', 'WFH4LBMD', '8JBNJ2N5', 'WFGXIN0E', 'WFF548OP', '8JBKU44K', '56EE2UEG',
                    '8JBUP6NV', '56EEF0PK', '560LE7K0', '56EHQDNH', 'WFHQR5SG', '56ESMWTP', '560S422F', '56EL8OB4',
                    '56EJC63K', '56ENDUT7', '56ECG4TX', '56EUHIX0', '56F54N7D', '56F7SSA6', '8JBRGLS4', '56EDV7PW',
                    '56EUZDO8', '56F6EVL8', '56EP1X74', '56EWYW15', 'WFIBTDEF', '56EETOGW', '56EVNXHQ', '560KBXPI',
                    '8JBLA5NL', '56F0EQKN', '56EQZ0OF', '56EWH4BD', '56F73PVZ', 'WFHMG7QC', '560KICTI', 'WFI7JO9G',
                    '8JBTF4UB', '560I8KCS', '56F77UKR', '569A70GN', '8JBLJ3TE', '56EN5VMK', '56EFBTDJ', '56F0VM4A',
                    '56ESZI8V', '56EHKZMI', 'WFH65OZ3', '8JBLL1GO', '8JBPMVYI', '56EX7VRF', '560QGS3N', '56EGR406',
                    '56EEQEWC', '560MZHSS', '56ECPMT7', '560Y1LIV', '8JBRJN5A', '56EGHA78', '560ZTHI6', '560ZVVBX',
                    '56EZZGWT', 'WFGRA8V7', 'WFDU9T5A', '56EZYCV5', '56EJ3CT0', '56ERRBOS', '56ECHO2L', '56EX34U1',
                    '56F2P8SZ', '8JBP4JK6', 'WFHZX8QV', 'WEE58IPF', '8JBMKRKR', '56EG57SD', '560T8D0Z', '56EUMJP4',
                    '56EWUNT0', '8JBNOO0C', '8JBK28ER', '8JBMSR07', '56EGKEHJ', '56ET0RGT', '560NU1ZK', '8JBOJLKZ',
                    '56F4ZMHG', '56EWKV1O', '560T1Y3W', '8JBQ512T', 'WFF7PGH7', '8JBUL6MS', '56EDBJQY', '56F4BFJD',
                    '56EKILSP', '56EEX2DD', '56F4ZWKS', '8JBOT8CZ', '56EFBU5R', '8JBL98TC', '56EU2N9K', '8JBL0GSD',
                    'WFJ8TZCU', '8JBRVT56', '56F4X6CV', '56F597FW', 'WFFKJPDC', '56F8ESG9', '560E6D6J', '56EJBRPO',
                    '560HW0W5', 'WFHXTK3A', '8JBNB1FQ', '560DY1BW', '56F3FU6W', 'WFKOH8QU', '8JBVYOKP', '56EZ919K',
                    '566DY00L', '56ES5H24', '8JBPS1O0', 'WFKCBWF0', '560Q2DLU', '560XTH4I', 'WFH9JT41', '56EMKQ0W',
                    'WFFZPMQ6', 'WFKE5CDG', 'WFHGABJF', '56ETQ9J5', '8JBU4D54', '560ODQNS', 'WFEAWC4C', '8JBTP4JT',
                    '56F5NYXY', '56F7FVBQ', '56EH5ARV', '56F890YC', '56EW1IWA', '56EHT2EJ', '8JBLB0O5', '8JBTVXGY',
                    '56F3DHBD', '56F01YG4', '56EQKWED', '56EFHJ97', '56EH7MFK', '56F1Q5FS', '56F5K0UU', '56F7BRVJ',
                    '56F1Y4W5', '560GBJ44', '56F70NLX', '8JBNGVVJ', '8JBLDI42', '56EXXNVH', '56EYCOWI', 'B21E88DQ',
                    '56EEGS17', '56F7GNO8', '56EQ0GEV', '56F1JBWY', '56EIF6DA', '560YHG6E', '56EIC61H', '560U6HGQ',
                    '560NHZM9', 'WFEXG39T', '56EEB5O7', '8JBO50P7', '56EBAGKE', '56F3JKQI', 'WFFKAURD', '56F55FLF',
                    '56F6U3EQ', '56ECG59L', '56F86VNY', '56EDREVS', '560IIR4S', '56EIDLEC', '56F2JOV4', '56ELWZA9',
                    '56F0RBPD', '56EOEC9B', 'WFI6NZRT', '8JBS4OUQ', 'WFD0B4S8', '56ERG0TM', '8JBN7VL6', '8JBLKF1F',
                    '56EO1V7N', '56EJCK3D', '8JBNGZ64', '56F72AZ3', '56F81GL1', '562ZCI2Y', '560Z4WTB', '8JBK9BT1',
                    '8JBLOUID', '56F4OK2N', '56F3I7T8', '56EZ5GD1', '56EZM1IT', '56F4XNQ2', '56EWXKPY', '8JBTMW0Y',
                    '56F11VTI', '56EYI9HR', '8JBO1EG7', '56ERAYUU', '8JBOJI04', '560SMRGO', '56EZJEIP', '56ENBXZG',
                    'WFE1C3V1', '560LE7D6', '56EZCBU7', '56EUYDU2', '56F5A9ZV', '56EWH496', '56ESHFAM', '8JBK0QAI',
                    '8JBSZ3XS', 'WFFMKM73', '56EIT73L', '8JBKQOQK', '56EDUE27', '560Y30BG', '56EODQBI', '56EJI2IQ',
                    '8JBPC37E', '56EOEC8C', '56EQ9RF6', '56EUB364', '56ETBYMJ', '56EG7C1T', '56F70I2D', '56F7M85I',
                    '56EHNJU9', '56F7RA27', '560SU125', '56EYGGOU', '56ERUYAM', '56F0HY35', '56EHW0PF', 'WFHBEY9V',
                    '56F4C7FL', '56F73PVT', '56EEHKEZ', '56F6JJSQ', '8JBPNY3R', '56EJNJSU', '56ET59OK', '8JBLHYUY',
                    'WFJ4CLP0', '56EIY44R', '560P54I9', 'WFJ5TJIT', '8JBKFUFA', '560QNQ9W', '560D1SSE', 'WFI2DB09',
                    '56ESMWVR', '8JBKV95O', '56EGTI58', '56F02YNL', '56EF4I7B', '56EHGV6M', '560SA4FB', '560ZJC3G',
                    'WFGECI4C', 'WFCVU5MP', 'WFH71RRP', '56F7POSV', '8JBOIF4W', 'WFGB9ZV2', '56EO095P', '56F17PQ1',
                    'WFJOOZG2', '56F0N7CL', '56EPT1KZ', '56F1KE9F', 'WFKMKTCR', '56F4A6NI', 'WFJ4JTL3', '56EZ4I9H',
                    '1P6KZVKU', '56F7V37A', '8JBNU1R2', '56F4R5V6', 'WFDKECOG', '8JBQQJ0J', '56EDACOR', '8JBQH2PP',
                    '56F7PKY4', '56EPK052', '56EGM55D', '56F4ENKU', '560FYGNQ', '56EOWRWB', '56F2SYUC', '56ECKRUY',
                    '56EDW7VI', 'WFFLS41L', '8JBO3U5Z', '56EKVO4S', '56ERI1O3', 'WFETR6VS', '56EEAGAK', '8JBMB0PU',
                    '560LKU76', '56EMUBDM', '8JBUA1G4', '8JBTMKYJ', '56EC6MNX', '56ENDC7F', '8JBPV2P3', '56F6ND2U',
                    '560XMTH9', '56ER1PSR', '560NST3T', '56F23NLJ', '56EV3J39', '8JBRHW0J', '56EOEL61', '56F8AXQ4',
                    '56ELXVWD', '56ET4Q7U', '56EVJSJM', '56ECNE51', '560W7VRX', '560LB21C', '56F59OCG', '56EDHLO2',
                    '56EUB3AG', '8JBVPNY4', '8JBQXHWN', '56EC89KK', '56ER7CXW', '8JBLVVDU', '56EWB0P4', 'WFFIZ0C1',
                    '8JBMHY4I', 'WFIB4FZ8', 'WFIR8RYF', '56EUP5SZ', 'WFFW15V6', '560P74PU', 'WFGJ48UN', '56EFAT11',
                    '560YB1GK', '8JBTT0SS', '56EIWJ62', '560W464J', '56EZ6PQS', '56F00QIK', '56EOXTDL', 'WFJJKP8F',
                    'WFIIGSK5', '56EQVPOZ', '56EUURZR', '8JBPVDLK', 'WFEWEJJV', '56EU4E75', '8JBOUKWD', '56F79O3Z',
                    '8JBMLDQ7', '560MSFD0', '56F320A1', '56ECKRUW', '8JBREJ9N', '56F8C8RI', '56EL0FR3', '8JBV3JGL',
                    '8JBWBSYK', '56EQY5B8', '56F4B86D', '56ERKPQV', '560NYE2U', '56ESH7WA', '56ELGIEK', '8JBM6LSD',
                    'WFDEN4CM', '56EHGHHO', '56EBJGN6', '56EKMQ8M', '56ECXCS2', '56EPKOKN', '56EHVWM9', '56EFLJVW',
                    '563N8A1G', '56EPTLO0', '56F7W8EU', '56F5E25Q', '560PYDEJ', '56EHE4R8', '56ECBKWX', '56EZLTG1',
                    '8JBKDRYV', '56F06NA5', '56EG72QK', '56EEVRTK', 'WFDQGVCG', '56EEEUFA', '56EEH6SA', '560M25M8',
                    '8JBQ1NSN', '56F5QB07', '56EPK2ML', '56EP39OG', '8JBTKOG0', '8JBW61YM', '56EHII6I', '8JBMUM7T',
                    '8JBL63ZZ', '56ERS6EH', 'WFI3RWFS', 'WFHAAHAP', '56EFWNKB', '56EQIF8S', '56EJ4SBK', '56ECEQMB',
                    '56EFANK5', '56F0EGJ8', '8JBKRQ2I', '56ETCDUY', '8JBORVE4', '56EFPA0N', '56EWD183', '56F02ELQ',
                    '56EE08XT', '56EQT8V7', 'WEE0FNUQ', '560C8BSW', '563N6WS2', '8JBKD13C', '56EU2CDR', '8JBMU5F0',
                    '8JBJVMV5', '56EZU430', '56ECTLY3', '56F4PGRM', '56EJ1K8D', '56EKY4D6', '56EGEFBE', '56EK2IET',
                    '56ECUVWN', '56EG54PM', '56ED0Z9Q', 'WFI5NL9N', '56EDDK0S', '56F2Y2K6', '569A02XG', '56ER3MT7',
                    '56EM91JE', '8JBUHSS0', '56EWJYRL', '560LJEN2', '8JBVAS3L', '56EQZO3R', '560ORV9S', '56EL83AV',
                    '56EO63DQ', '56F5A4CT', '56ELJHR1', '56EJ61K6', '56ENZIFO', '563N9PYV', '56F018WX', '56EF7FD9',
                    '8JBQC9M6', '560HYH3Z', '8JBNJSDS', '56F6UP0H', '56EKQ947', '560RK3FF', '56F2S495', 'WFCT16F3',
                    'WFFXXP8P', '56EF3LUT', '56EF0JSZ', 'WFI45HE1', '56ER87DF', '8JBRM1N1', '56ECO1VY', '56F4WUWP',
                    '56EBGHGX', '56ELXWK0', '56F2JYDA', '56ETGKE8', '56F07KS5', '56EKQ97A', '56EFAYTT', '56EY38QF',
                    'WFE5UXP1', '8JBKDN7X', '56EICPI7', '8JBP9JIQ', '8JBL4MUU', '8JBKPI9L', '56EQSY8T', '56ESQWCX',
                    'WFGHK447', '8JBNN4Z4', '56EX2V8C', '56EDYLRG', 'WFFZ75GF', '8JBMRFV5', '8JBNYA8W', '56EY5MDH',
                    '8JBKFJ2T', '56EHDCVV', '56F75BGR', '56EUGAGO', '560UFA77', '56EG7VPO', '56F27F10', '8JBRDXZG',
                    '56F5AP4I', '56ERBKYE', '56F4AOBH', '56EN3H40', '56F86HJG', 'WFJGGCYW', '56EPYXAM', 'WFIOIJ0T',
                    '8JBPEZPW', '56EUL6P5', '56EHQHEX', '56EGZNOL', 'WFK7O6K2', '56ELSFK5', 'WFJYT0GB', '56ED3X1J',
                    '56EZ73HI', '8JBUYKIO', '56ETRLS5', '56EIY438', '56ED75OU', '56EJ1T8G', '56F4WY1B', 'WFDWET8I',
                    '56F0VZR0', '56ENK6Q5', '56EYD9OJ', '8JBW5ZKM', '56EIHWTT', '56EM856H', '56F5QAXZ', '56F21DOQ',
                    '56EG64MM', 'WFHKWCKV', '8JBRRGSP', '56ES6EJN', 'WFECY9LO', '56F31FKU', '560XI5B2', '56F7MTU8',
                    'WFIAFGD7', '56ENR4BS', 'WFEB0JTL', '560QHL9O', '56EZ5BIH', '56F2JYOE', '56F77QTH', '56F7DMGH',
                    '56EBZWZE', '8JBSUFJ0', '8JBUB5M8', '56ETV5WJ', '560CMCTD', '56ECX0L8', '56EWZ54W', '8JBU8OTP',
                    '560YGLFC', '56EYMS6M', 'WFG5QL71', 'WFH9TFWD', 'WFCZ2QTB', '56EZKSID', '8JBOA1V8', '560DXHVJ',
                    '560UCB99', '560KDGC4', '560NGMZ9', '56EFCVGM', '563NIKL6', '56EHTSLF', '8JBPTW9K', '560HU8DA',
                    '56ESX1D0', '56EGZ756', '56ESTTB0', '8JBU5UED', '56EP61W8', 'WFITWENP', '56EPPP1L', 'WFECR5HP',
                    '56F5CJT0', '8JBVGTNZ', '56EHH895', '56F5EQ0Z', '56EGY56M', '8JBK8LE3', 'WFHK7V0D', '8JBJUPPY',
                    '56F1NFOR', 'WFIPZA66', '8JBLMDX1', '56EVA3HA', 'WFH8XKOX', '566G5HIB', '56F7NORG', '8JBPYSBV',
                    '56EHBIME', '56F0EDMS', '8JBP3FB6', '56F2R4ZH', '56ELT01E', '8JBVGUK9', '8JBMOVN1', '56ETSZMS',
                    '56F6ZMGM', '56ELWLF3', '56F87EYM', '8JBRDWXJ', '56EXG5BE', '56F54SWO', '56EMNVA5', '56F4W81M',
                    '560JJZ5N', '56EJK07V', '56ED64SZ', '56EN23C8', 'WFJVN3BE', '8JBVVQRL', '8JBTN8HY', '56EBHX0A',
                    '56EKW1M6', '560UJHNU', 'WFEJIMTV', '56EYQ65Y', '8JBRQT5G', '56EGHKAT', '560OKEK3', '8JBRVDVJ',
                    '56ES4WC4', '56F0IW35', '56EU4E7K', '56EDS12O', '8JBJVRG7', '8JBNDOS3', '56EGKFLN', '56EG2DPP',
                    '56EHUWF6', '8JBL3S8N', '56F76A40', 'WFJXKUHK', '56EHK70R', '560SL66C', '56EMXTPH', 'WFEZ9RME',
                    '560NGMYR', '56EFNL2C', '56EP078Y', '8JBSYHGE', '56F0G96Y', '56F2GPWK', '56EPNZVB', 'WFI78OZY',
                    '56ECDLVC', '56EH6WTG', '56F79ZCM', '8JBOPBHG', '56EPU7DA', '56F8KT7M', '56F6VWVK', '56EIB67K',
                    '566DYO78', '56EVTUE4', '56F7C1BT', '56EF5B6I', '56ETI5EG', '8JBU0ZYG', '56EGV6BG', '8JBTKE3J',
                    '56ED27PI', '8JBN8PR6', '8JBUEVFI', '560GTSL3', '56F32TJK', '8JBRWKOV', '56EUCFSJ', '8JBTDKA5',
                    '56F6ZLUA', 'WFDTLKI8', '56EVR2WQ', '56EG055Q', '8JBP1SZV', '560F96AU', '56EW13ZB', '56F2MRBV',
                    '8JBNTWLN', '8JBUB5M6', '8JBQZQRH', '8JBPD4QD', '56EZB33T', '56F0YVA1', '56ENMBYH', '56F8HS0H',
                    '56ESVV27', '56ECNE4Q', '560NMHSY', '56EH9NJ5', '56EW730Q', 'WFE2IN9A', '56EK8V0M', '8JBPDNTU',
                    '56EWLSB2', '56EFFOKU', '56EUWHUG', '56EYTQC7', 'WFENTZD9', '56EYOL0F', '56F5HPI0', '56F7TLWE',
                    '560CSA4E', '56EJPYXS', '8JBR5W6I', '56F52DL8', '560NXDH7', 'WFGQXI5B', '560NWTAO', '56ESTDGS',
                    '56EIE71Y', '56F0TWPO', '560ZXMS7', '56F56OSO', '8JBML83L', '56EIURAU', '8JBKIJCU', '56ETB8F3',
                    '560LPULA', '56EFOLL6', '56F31UE8', '560C4VTA', '8JBRHG6I', '56F78TT1', 'WFFAQIOF', '56EY1JEL',
                    '56EVEP1W', '56EHO1VP', '56F7BGV5', '56ELKV22', '569AEICH', '56EZA16O', '56F2FVRC', '56EBHODM',
                    '56EYJ3PV', '56EM8PHW', '8JBTGBBL', '56EYC9TE', 'WFET5NYV', '56F2L934', '8JBQ0PHV', '8JBJS47X',
                    '56EHC0YN', '8JBRBTWU', '566FFTQE', '8JBW6ISO', '56F7XFCU', 'WFIPW5OV', '56EZI9HL', '56F4DW71',
                    '8JBW9MWL', '56EWBFX0', '8JBTLTJ6', '56EC9YQ5', '566FPNDP', '8JBL78K2', '56EXFT53', '56EFYB1I',
                    '56EO8CEE', '563N8VQ0', '56EV0PRZ', '56EULPC8', '560N9QDT', '56ELKECQ', '56F4X6CL', '56F7WF7Q',
                    '56EJY9MZ', '56ET5ISV', '56F1O7YG', '56F7WCB3', '56F1LDG0', '56EOL87P', '56F2OWMV', '8JBMQP4K',
                    '560BQUB9', '56EI7I77', '56EGCW57', '56EEREOJ', 'WFGRMXJ6', '56F1EKKQ', '56EPL9WX', '56EH6WV4',
                    '56EE440O', '56EDUDYM', '8JBW34PA', '8JBU29W6', '8JBOEZVB', 'WFJOE10Z', '56EIWIRB', '8JBTZOC8',
                    '56ETWA3Q', '56ESS6NB', 'WFGSX66V', '56EV0GYJ', '56EZMO8M', '56EH42HK', '56EXKPLZ', '56F5G8DY',
                    '56EF717Z', '56F22LZJ', '56EG18SL', '560PHJO0', '56EK9SE2', '56EUUFCW', '56EMNV04', '56EF15R0',
                    '56EJN37F', '56ENTB9O', '56F7TVNG', 'WFHEKMOC', 'WFJCV1CT', '56F4GQO4', '56EWCD0T', '56EQ50WK',
                    '8JBP41OG', '56EFRR6D', '8JBPIHPV', '56ES4RSP', '56ERTFTU', 'B21E88HG', '560QS8MW', '8JBR6PJ1',
                    '56F71D0B', '56EE3IHR', '56EG7GM0', '56F56H4V', '8JBVZ8MU', '56F6RJ9D', '56F1XMTV', '56ER5RIC',
                    '8JBVF4HF', '56EP9PVD', '56F4KEM6', '56F0L7TZ', 'WFIQFVHH', '56F2LW2G', '56F7CY54', '56F4ARJ0',
                    '8JBNWL28', '56F4LI9N', '56ENEX05', '56EO8UOS', '569ABCYK', '56EFVVU1', '56EF9WZR', '56EO4GT5',
                    '56ERCHB0', '56EZWLHE', '56EINNYY', '8JBL51TA', '8JBT6JNF', '56F5D1KV', '56EMK3YS', 'WFJFKAN7',
                    '8JBSTVOP', '560Y5GRF', '56EILJ8R', '56EN8NRY', '560TQSQG', 'WFFYM32V', '8JBUFSMW', 'WFIM2NCD',
                    '56EXYSUC', '56F4FFIH', '56EPMU3X', '56EFR992', '56ER4RDN', '56EV6VW3', '56ECEBKC', '56EGZABU',
                    '8JBLHI8F', '56F1MBOM', '8JBVH5Q8', '8JBQ4EUN', '8JBM1N9C', '56EBXB1G', '56ENYWJ7', '56F7P5A6',
                    '560JS49Q', '8JBM6WXV', '56EY9HKG', '8JBU665U', '56ETYWL3', '56EIABXJ', '8JBWK98C', '56EGBDW7',
                    '56EF6T3N', '56EFVREN', '56F5BIPO', '56F1TX45', '8JBUNWE5', '56EHOQYX', '56F2S47D', 'WFGM6E03',
                    '8JBWG1MA', '56F08CST', '8JBO8UQ2', '560CR2FE', '8JBV5FXY', '56F5J98A', 'WFHZM4WF', 'WFDX2U9X',
                    '56ELZBSI', '56EGY8FG', '560IDKGG', '56EYWEJ8', '8JBNT6MM', '56EHULFI', '560HCWAA', '56EUI2SP',
                    '8JBR7M0F', '560XYT9C', '56F37PGJ', 'WFDH8XS9', '56F56YS2', '56F5PMPR', '8JBTENUK', '8JBKRZAC',
                    '56F4XSNO', '56EOHOBN', 'WFENKGNR', '56EUZVRT', '56EBAEMO', '56ECLJBT', '56EGMLCS', '56EOHLH1',
                    '56EDK5JQ', '56EZV0EM', '56EMZPOL', '56EPNFYO', 'WFEQIXHM', '56F15J6K', '56EHJ7IW', '560P89I4',
                    'WFI2ODCX', '56F2JYSB', '56EFV5OH', '560T2HBK', '56F6MEVF', '56F6Q1EA', '560V42Q5', '56ENJZSG',
                    '56EG9FBR', '56EVFIUH', '56EIJH48', '8JBSCYGW', '56F84K3E', '56F1VEPH', '56EO6JIG', '56ERPYVF',
                    '8JBQWCMD', 'WFJ5PWJD', '56EIEHWY', 'WFHUHOFX', '56EWGF5M', '56EJ06G2', '56F194LH', '56EQIO58',
                    '56EV3J1H', '56EBERVH', 'WFGN8IHW', '56F7R2AZ', '560LJEMY', '56EMD87A', '56ESQM0F', '56EHIS9N',
                    '56EN7CDQ', '8JBV792L', '8JBUDDOQ', '56ECB8EK', '8JBSXNWL', 'WFCUDEF3', '56EJ8EIW', '8JBK7W77',
                    '56F1L4N5', '56EV6L62', '56EVZABM', '8JBUA3U0', '8JBPEOXP', '56F6QD10', '56EE5C49', '8JBM7M1B',
                    '56EGL3FG', '560XJT9S', '56EIREQD', 'WFF2CA8L', '56F7SAG1', '56ENVY9E', '56EPDAVE', '56EHBH4D',
                    'WFEMEA81', '56EQ230M', '56EUPWSA', '56ESJN2T', '8JBR915F', '56F4TU9Q', '56F0ARC1', '56EDXZB0',
                    '56F7TVRB', '560ON2WC', '56EW6SMG', '8JBUQCPK', 'WFF4QBQ8', '56F4W7YN', 'WFIP4Q3M', '56EW1XV5',
                    'WFF6XBD5', '56EWUNWF', '56ETN7P9', '8JBU9NAD', 'WFJDOW7N', 'WFDR8FLW', '56EZ73DG', '56EJ61MM',
                    '56EN35M7', '56F7QSNZ', '56EPXFFZ', '8JBRO01P', 'WFFF494Q', 'WFI6CM6Z', '56EZA3PW', '56ETGCN3',
                    'WFF71AF2', '56ETBMZA', '56EMP382', '5W2PPT9Q', '8JBKTMED', 'WFF3E530', '56EK88ZE', '56EYIN70',
                    '8JBVSLVC', '56ESLQ9W', '56EC3ZY0', '56ECKIJ6', '56EMZD0H', '56EV37BP', '560S3HT1', '56EQDF4Y',
                    '8JBVOALN', '56EZHOJQ', '56EYZNWP', '56F534U5', '56F8CP8E', '56ED05X0', '56EE2EY4', '560QYLPQ',
                    '560KO1CH', '569AAG3B', '56EY0YWN', '560RDC8L', '56ED62OO', 'WFFT7GER', '56F89V0E', '56F7K9JR',
                    '56EJSVKZ', '560JMV9E', 'WFFSUVKZ', '8JBTHVWX', 'WFFIXEW7', '56F0EQW3', '8JBU725T', 'WFK4HJEZ',
                    '56EZCHCV', '56F78KN5', '8JBVKUHJ', '56F2ENO9', '560X4FLM', '8JBLNAZ3', '56ES0NLT', '56EO3UM3',
                    'WFGXL8ZK', '8JBRE36Y', 'WFHYKOJJ', '56F83PIC', '56EY7OW5', '8JBRDEZK', '560XUZ9P', '8JBR3RZF',
                    '8JBVDTUH', 'WFGE4OSS', '56EFV0VO', '56ER93TP', '560ZHA3L', '8JBVK1K7', 'WFDEHPVL', '56EKFH0T',
                    '56ETWG93', 'WFHID7HY', '56ER4RDT', '560PEYHN', '56EE5EZT', '56ETNZTP', '56EBVM7G', '56EEVC17',
                    '56ECNPZV', '56EBUBNE', 'WFK86LYP', '56F85Q7N', '56ES2ZY3', '56EVDK6X', '56EEGEBY', '56F37VGO',
                    '56ED8ELU', 'WFHKJC8O', '56ELQBPW', '56EFM8VH', '56ED2X8M', '56F1OUGE', 'WFJNU50R', '56EQG3AW',
                    '56F6YRXJ', '56F1Y4TI', '56EWJLM1', '56F8BFXF', '56F4TM3C', '56EWH47F', '56EGFB95', '56ETS61C',
                    '8JBV2S9C', '8JBKUYB4', '56F101W8', 'WFCUHC71', 'WFETFIEF', '566FM98V', '56F8BQEO', 'WFJRJFCY',
                    '56EVXN2T', '56ERQI9T', '56EH80US', '56EXPOZM', '56ECCIX9', 'WFE6WWDN', '560P647O', '56EUK0E9',
                    '56EMAXNR', '8JBS2DTK', '8JBS7CSE', '56F007OZ', '8JBMHGVE', '8JBNLEAV', 'WFDIBUNL', '8JBSEXNS',
                    '8JBOP9ZC', '560BZJHL', '56EDYSQO', '560G22CK', '8JBK81ZQ', '56F2H90F', '56ECAQ2J', '56EBRQXD',
                    '56F6QKLO', '56EIKMIW', '56EQNEHJ', '8JBOMBFH', '56EPQGA3', '56F1H10H', '8JBP1CWU', '56ERUD8A',
                    '56EBVG3J', '56F246KG', '56F0RQ5T', '56ECP2AG', '560STAT3', '56EIJ1VP', '560HCW6N', '56F7DTFE',
                    '56EKMQD8', '560KICSV', '56F7S71F', '56EGEQ52', '8JBOUZZZ', '56F6JJSU', '8JBJS8V9', '56F7LLZE',
                    '8JBQS5NJ', '56EXSWMD', '56F0K7PG', '56ETKSGA', '56ECLHRM', '56F5KJCL', '560XF1VC', 'WFDJ5P3Z',
                    '56EPFNUT', '56EINPOA', '56F6VUTJ', '56ER0LCY', '56F6DKBS', '8JBQOICP', '56ETTQBI', '8JBPOR55',
                    '56EZH8AV', '56EJ2M3N', '8JBMQ2I4', '560V555O', '56F03UO8', '560NJNC0', '56EHGK1H', '56F5NXR0',
                    '56EZVY0H', '56ED9GSB', '56F24H1O', '560YTK7R', '8JBPP0AJ', '560M8C1Q', '8JBT5O5U', '8JBT6Z50',
                    '56F35T9O', '560IPCRI', '56EEA8G8', '56EYD4XW', '560RZBTB', '56EVXFK8', '560O9C23', '8JBUVWU7',
                    '8JBU30LN', '56EYQIAS', '56F2G0JF', '56ESIRU3', 'WFKKU901', '56EZ1YQW', '56F5M0KP', '8JBQ7JR9',
                    '56F6CGVK', '560KUBF0', '56EQ4JXV', '56EDJMUT', 'WFEPAQOT', '56EQE70Z', 'WFHNZQFN', '56F6KE2O',
                    '56F5E7H3', 'WFJHVLPX', '56EEDPXK', '56EV268R', '56EIDLEA', 'WFEME2D8', 'WFE8VFBA', '56EHNLS1',
                    '56F6RJ4E', '56EMHD6F', '56EFHQ9S', '56EFBPM8', '56ET8VF8', '56EYPVIZ', '560HE1KD', '56F26EWD',
                    '56EIWF3W', '560OI67E', '56EEI33R', 'B21E88HD', '56F4OK5U', '56EXUMCU', '560K4Q12', '1YRWTLMW',
                    '56EDW7UW', '56F6LQL9', '56EZJIRJ', '56F4OK3I', '8JBMRJTI', '56EPB5EL', '56EUOBK9', '56F6SQ2G',
                    'WFDS75GF', 'WFE3TBCB', 'WFDNRRKJ', '56F5AWYM', 'WFDG0PI4', '56F6CQOK', '56F31J0G', '56EIGVJW',
                    '56EFZBKU', '560FCX1U', '56F6RTDY', '56EQ1OCA', '56EQQB8L', '560G4AVA', '56EQ235V', '56EBZN1U',
                    '56F0KINO', '8JBW6EH0', '560XLW51', '8JBP1QM2', '560X4FLJ', '56F2QNVM', 'WFIN75T2', '8JBTTNH9',
                    'WFIKLXLX', '56ELMA7R', '8JBNK4RG', '8JBQEWE7', 'WFGXWH9T', '56EEMUOL', '56EXHT8L', '8JBVG91M',
                    'WFEJO3MN', '56EGIOLM', '56F14VDR', '56EKPSNV', 'WFJ7PZ0Z', 'WFJBA1H5', '8JBM0V94', 'WFJPVJDZ',
                    '8JBKVC1I', '566FS6ZM', '560MJA0J', '56ED1FWR', '8JBNU9Y7', '56EVMPCN', '56EOSYIC', 'WFJ0H6ZB',
                    '56EJ1T7C', '56F3ECAC', '56F0RECO', '560ENPO8', 'WFHPN91R', '560DZC3J', '56EJ4XC4', '56F15TIH',
                    '56EDHDRM', '560CAXCJ', '560NQNVQ', '56EX3WI7', '56EIQO41', '8JBMS0G9', '8JBTTEIR', '560O15B4',
                    '56F7D1HX', '56EHRBGK', '56EDW7YK', '56EZN2DC', '56F56YS7', 'WFH06K71', '56EO095R', '56F17QSJ',
                    '56EGG5B4', '56F3IPUY', '8JBUCBJ0', '560KZYBU', '8JBO0XQ1', '56EVLWET', '560NPD9P', '56EEYFS5',
                    '56EW9BAE', '8JBMEMBK', '8JBPSOCL', '56EPQRKW', 'WFJRKNDI', '56ENO30U', '56EEC6QS', 'WFK0WFTX',
                    '8JBV1NYV', '56EJVGCI', '8JBMCIND', '56ES42XR', '8JBS9WO5', '56EP92TC', '560H3UQ0', '560OHLFM',
                    '56EU08KZ', '560YGBUB', 'WFDZQ70H', '8JBQBG3B', '56EUTXYM', '56EPO8BK', '56EI7BQM', 'WFCXE4Q7',
                    '56EC4NOZ', 'WFDSG3IM', '56ECB0ZZ']

    def __init__(self):
        self.vehicle_list_len = len(self.vehicle_list) - 1

    def get_data(self, middleware_type):
        """
        获取当前中间件的消息起始值，并记录当前时间
        {topic, payload, qos, retain, properties}
        """
        if middleware_type == 'emqx':
            vehicle_id = self.get_vehicle_id()
            return {
                "topic": self.get_random_topic(vehicle_id),
                "payload": self.generate_random_binary(vehicle_id.encode()),
            }

    def get_vehicle_id(self):
        return self.vehicle_list[random.randint(0, self.vehicle_list_len)]

    def get_random_topic(self, vehicle_id):
        return f"manufacturer/v1/device/binary/{vehicle_id}/vehicle/travel"

    def generate_random_binary(self, vehicle_id):
        # Head Level
        message_type = 1  # 1 byte (B)
        data_type = 2  # 1 byte (B)
        version_number = 3  # 1 byte (B)
        millisecond = 4  # 2 bytes (H)
        minute = 5  # 4 bytes (I)

        head_format = ">B B B B B B H I"
        head_binary = struct.pack(
            head_format,
            message_type,
            message_type,
            message_type,
            message_type,
            data_type,
            version_number,
            millisecond,
            minute
        )

        timestamp = int(time.time() * 1000)  # 8 bytes (Q)
        speed = random.randint(0, 255)  # 2 bytes (H)
        gnss_status = random.randint(0, 255)  # 1 byte (B)
        longitude = 1201530160 + random.randint(0, 100)  # 4 bytes (I)
        latitude = 303103960 + random.randint(0, 100)  # 4 bytes (I)
        altitude = random.randint(0, 255)  # 4 bytes (i)
        heading_angle = random.randint(0, 255)  # 4 bytes (I)
        hdop = random.randint(0, 255)  # 2 bytes (H)
        vdop = random.randint(0, 255)  # 2 bytes (H)
        gear_information = random.randint(0, 255)  # 1 byte (B)
        steering_wheel_angle = random.randint(0, 255)  # 4 bytes (i)
        light_state = random.randint(0, 255)  # 2 bytes (H)
        velocity_can = random.randint(0, 255)  # 2 bytes (H)
        longitudinal_acceleration = random.randint(0, 255)  # 2 bytes (h)
        lateral_acceleration = random.randint(0, 255)  # 2 bytes (h)
        throttle_pedal_opening = random.randint(0, 255)  # 1 byte (B)
        engine_speed = random.randint(0, 255)  # 4 bytes (i)
        engine_torque = random.randint(0, 255)  # 4 bytes (i)
        driving_brake = random.randint(0, 255)  # 1 byte (B)
        brake_pedal_opening = random.randint(0, 255)  # 1 byte (B)
        brake_pressure = random.randint(0, 255)  # 2 bytes (H)
        yaw_rate = random.randint(0, 255)  # 2 bytes (H)
        wheel_velocity_fl = random.randint(0, 255)  # 2 bytes (H)
        wheel_velocity_fr = random.randint(0, 255)  # 2 bytes (H)
        wheel_velocity_rl = random.randint(0, 255)  # 2 bytes (H)
        wheel_velocity_rr = random.randint(0, 255)  # 2 bytes (H)
        abs_flag = random.randint(0, 255)  # 1 byte (B)
        tcs_flag = random.randint(0, 255)  # 1 byte (B)
        esp_flag = random.randint(0, 255)  # 1 byte (B)
        lka_flag = random.randint(0, 255)  # 1 byte (B)
        acc_mode = random.randint(0, 255)  # 1 byte (B)
        fcw_flag = random.randint(0, 255)  # 1 byte (B)
        ldw_flag = random.randint(0, 255)  # 1 byte (B)
        aeb_flag = random.randint(0, 255)  # 1 byte (B)
        lca_flag = random.randint(0, 255)  # 1 byte (B)
        dms_flag = random.randint(0, 255)  # 1 byte (B)
        soc = random.randint(0, 255)  # 1 byte (B)
        drivemode = random.randint(0, 255)  # 1 byte (B)
        ctrl_id = random.randint(0, 255)  # 4 bytes (I)
        horn_state = random.randint(0, 255)  # 1 byte (B)
        motor_speed = random.randint(0, 255)  # 4 bytes (i)
        epb_flag = random.randint(0, 255)  # 1 byte (B)
        wiper_state = random.randint(0, 255)  # 1 byte (B)
        device_state = random.randint(0, 255)  # 1 byte (B)
        warning_light = random.randint(0, 255)  # 1 byte (B)
        accel_cmd = random.randint(0, 255)  # 2 bytes (H)
        torque_cmd = random.randint(0, 255)  # 4 bytes (i)
        velocity_cmd = random.randint(0, 255)  # 2 bytes (H)
        ad_version_length = 8  # 1 byte (B)
        roll_rate = random.randint(0, 255)  # 2 bytes (H)
        current_fuel = random.randint(0, 255)  # 2 bytes (H)
        fuel_consumption = random.randint(0, 255)  # 2 bytes (H)
        power_consumption = random.randint(0, 255)  # 2 bytes (H)
        manual_intervention_mode = random.randint(0, 255)  # 1 byte (B)
        system_failure = random.randint(0, 255)  # 1 byte (B)
        collision_and_risk = random.randint(0, 255)  # 1 byte (B)
        remote_driving_signal_delay = random.randint(0, 255)  # 2 bytes (H)

        first_level_format = ">8s Q H B I I i I H H B i H H H H B i i B B H H H H H H B B B B B B B B B B B B I B i B B B B H i H B 8s H B H H H B B B H"

        first_level_binary = struct.pack(
            first_level_format,
            vehicle_id,
            timestamp,
            speed,
            gnss_status,
            longitude,
            latitude,
            altitude,
            heading_angle,
            hdop,
            vdop,
            gear_information,
            steering_wheel_angle,
            light_state,
            velocity_can,
            longitudinal_acceleration,
            lateral_acceleration,
            throttle_pedal_opening,
            engine_speed,
            engine_torque,
            driving_brake,
            brake_pedal_opening,
            brake_pressure,
            yaw_rate,
            wheel_velocity_fl,
            wheel_velocity_fr,
            wheel_velocity_rl,
            wheel_velocity_rr,
            abs_flag,
            tcs_flag,
            esp_flag,
            lka_flag,
            acc_mode,
            fcw_flag,
            ldw_flag,
            aeb_flag,
            lca_flag,
            dms_flag,
            soc,
            drivemode,
            ctrl_id,
            horn_state,
            motor_speed,
            epb_flag,
            wiper_state,
            device_state,
            warning_light,
            accel_cmd,
            torque_cmd,
            velocity_cmd,
            ad_version_length,
            b"12345678",
            roll_rate,
            current_fuel,
            fuel_consumption,
            power_consumption,
            manual_intervention_mode,
            system_failure,
            collision_and_risk,
            collision_and_risk,
            remote_driving_signal_delay
        )
        full_binary = head_binary + first_level_binary

        return full_binary
