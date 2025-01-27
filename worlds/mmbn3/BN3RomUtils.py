import re

from .Items import ItemType

ArchiveToSizeUncomp = {0x684F9C: 0xED, 0x7043EC: 0xA25, 0x704E14: 0x4DE, 0x7052F4: 0x236A, 0x707660: 0x13FB, 0x708A5C: 0x70, 0x708ACC: 0x264, 0x708D30: 0x8D0, 0x709600: 0xE96, 0x70A498: 0xEB5, 0x70B350: 0xE9B, 0x70C1EC: 0xE8A, 0x70D078: 0xEC6, 0x70DF40: 0xEE2, 0x70EE24: 0xEAA, 0x70FCD0: 0x9B1, 0x710684: 0x765, 0x710DEC: 0x4F6, 0x7112E4: 0x9C8, 0x711CAC: 0x66A, 0x713F50: 0x48, 0x713F98: 0xDF, 0x714078: 0x17C, 0x7141F4: 0x45F, 0x714654: 0x13F, 0x714794: 0x249B, 0x716C30: 0x2225, 0x718E58: 0x1DA3, 0x71ABFC: 0x1D51, 0x71C950: 0x1495, 0x71DDE8: 0x12B3, 0x71F09C: 0x15B3, 0x720650: 0x607, 0x720C58: 0x3E0, 0x721038: 0x208, 0x721240: 0x428, 0x721668: 0x3FF, 0x721A68: 0x23FE, 0x723E68: 0x117, 0x723F80: 0x64B, 0x7245CC: 0x15A, 0x724728: 0x250C, 0x726C34: 0x1EE4, 0x728B18: 0x1E65, 0x72A980: 0x18F8, 0x72C278: 0xA16, 0x72CC90: 0x4C, 0x72CCDC: 0xE1E, 0x75DBE4: 0x9A, 0x778494: 0x2A8, 0x77873C: 0x303, 0x778A40: 0x1A8, 0x778BE8: 0x74B, 0x779334: 0x2AE, 0x7795E4: 0xB5, 0x77969C: 0x566, 0x779C04: 0x235, 0x779E3C: 0x211, 0x77A050: 0x352, 0x77A3A4: 0x1A8, 0x77A54C: 0x171, 0x77A6C0: 0x124, 0x77A7E4: 0x24D, 0x77AA34: 0x5D9, 0x77B010: 0x167, 0x77B178: 0xD4, 0x77B24C: 0xF0, 0x77B33C: 0x2E9, 0x77B628: 0x12B, 0x77B754: 0x205, 0x77B95C: 0xF6, 0x77BA54: 0xFB, 0x77BB50: 0x326, 0x77BE78: 0x216, 0x77C090: 0x4D0, 0x77C560: 0x1A1, 0x77C704: 0x71, 0x77C778: 0x3D, 0x77C7B8: 0x2D, 0x77C7E8: 0x47, 0x77C830: 0x4C, 0x77C87C: 0x4B, 0x77C8C8: 0x9C, 0x77C964: 0x1FC, 0x77CB60: 0x1A6, 0x77CD08: 0x45D, 0x77D168: 0x2DE, 0x77D448: 0x479, 0x77D8C4: 0x170, 0x77DA34: 0x1CC, 0x77DC00: 0x3E2, 0x77DFE4: 0x158, 0x77E13C: 0x2D6, 0x77E414: 0x195, 0x77E5AC: 0x2C7, 0x77E874: 0x810, 0x77F084: 0xFB, 0x77F180: 0x182, 0x77F304: 0x1FC, 0x77F500: 0xF3, 0x77F5F4: 0xC9, 0x77F6C0: 0x1D0, 0x77F890: 0x114, 0x77F9A4: 0x503, 0x77FEA8: 0x517, 0x7803C0: 0x99, 0x78045C: 0x43C, 0x780898: 0x20C, 0x780AA4: 0x1B8, 0x780C5C: 0x342, 0x780FA0: 0x1A5, 0x781148: 0x70, 0x7811B8: 0x521, 0x7816DC: 0x5F8, 0x781CD4: 0x3E3, 0x7820B8: 0x7C8, 0x782880: 0x280, 0x782B00: 0x77D, 0x783280: 0x1C8, 0x783448: 0x72E, 0x783B78: 0x4C0, 0x784038: 0x3DB, 0x784414: 0x3B0, 0x7847C4: 0x1EC, 0x7849B0: 0x4F1, 0x784EA4: 0x544, 0x7853E8: 0x1B4, 0x78559C: 0x1DB, 0x785778: 0x1E3, 0x78595C: 0x162, 0x785AC0: 0x2A3, 0x785D64: 0x41B, 0x786180: 0x4AB, 0x78662C: 0x1C6, 0x7867F4: 0x202, 0x7869F8: 0x52F, 0x786F28: 0x236, 0x787160: 0x479, 0x7875DC: 0x259, 0x787838: 0x1D0, 0x787A08: 0x720, 0x788128: 0x299, 0x7883C4: 0x3C0, 0x788784: 0xB6F, 0x7892F4: 0x3D0, 0x7896C4: 0x362, 0x789A28: 0x244, 0x789C6C: 0x496, 0x78A104: 0x36F, 0x78A474: 0x2B6, 0x78A72C: 0x1D8, 0x78A904: 0x1D9, 0x78AAE0: 0x1EC, 0x78ACCC: 0x1DA, 0x78AEA8: 0x557, 0x78B400: 0x11C, 0x78B51C: 0x5A8, 0x78BAC4: 0x420, 0x78BEE4: 0x10D, 0x78BFF4: 0x505, 0x78C4FC: 0x7FB, 0x78CCF8: 0x546, 0x78D240: 0x74F, 0x78D990: 0x12B, 0x78DABC: 0x69D, 0x78E15C: 0x91A, 0x78EA78: 0x820, 0x78F298: 0x662, 0x78F8FC: 0x52F, 0x78FE2C: 0x4AD, 0x7902DC: 0x572, 0x790850: 0x393, 0x790BE4: 0x662, 0x791248: 0x506, 0x791750: 0x98, 0x7917E8: 0x8AF, 0x792098: 0x1C1, 0x79225C: 0x610, 0x79286C: 0x6A3, 0x792F10: 0xFC, 0x79300C: 0x317, 0x793324: 0x750, 0x793A74: 0x216, 0x793C8C: 0x762, 0x7943F0: 0x4B7, 0x7948A8: 0x68E, 0x794F38: 0x233, 0x79516C: 0x24A, 0x7953B8: 0x1CD, 0x795588: 0x2FA, 0x795884: 0x454, 0x795CD8: 0x90, 0x795D68: 0x61, 0x795DCC: 0x10B, 0x795ED8: 0xD8, 0x795FB0: 0x723, 0x7966D4: 0x4D, 0x796724: 0x367, 0x796A8C: 0x81, 0x796B10: 0x2A2, 0x796DB4: 0x93, 0x796E48: 0x2D2, 0x79711C: 0x577, 0x797694: 0x69A, 0x797D30: 0x34F, 0x798080: 0x582, 0x798604: 0x528, 0x798B2C: 0x60A, 0x799138: 0x1A9, 0x7992E4: 0x1CB, 0x7994B0: 0x711, 0x799BC4: 0x3A3, 0x799F68: 0x4B2, 0x79A41C: 0x11E, 0x79A53C: 0xEA, 0x79A628: 0x298, 0x79A8C0: 0x1F3, 0x79AAB4: 0x24E, 0x79AD04: 0x42E, 0x79B134: 0x1E1, 0x79B318: 0x8FF, 0x79BC18: 0x120, 0x79BD38: 0x107, 0x79BE40: 0x116, 0x79BF58: 0x11C, 0x79C074: 0x1FE, 0x79C274: 0x18B, 0x79C400: 0x189, 0x79C58C: 0x28A, 0x79C818: 0x1A2, 0x79C9BC: 0x22F, 0x79CBEC: 0x542, 0x79D130: 0x89B, 0x79D9CC: 0x220, 0x79DBEC: 0x245, 0x79DE34: 0x417, 0x79E24C: 0x14E, 0x79E39C: 0x6BE, 0x79EA5C: 0xA2D, 0x79F48C: 0x90B, 0x79FD98: 0x688, 0x7A0420: 0x585, 0x7A09A8: 0x196, 0x7A0B40: 0x28F, 0x7A0DD0: 0x4BC, 0x7A128C: 0x32E, 0x7A15BC: 0x353, 0x7A1910: 0x5CD, 0x7A1EE0: 0x4E0, 0x7A23C0: 0xDD, 0x7A24A0: 0x220, 0x7A26C0: 0x16C, 0x7A282C: 0xA20, 0x7A324C: 0x31D, 0x7A356C: 0x6B4, 0x7A3C20: 0x125, 0x7A3D48: 0x6DA, 0x7A4424: 0x601, 0x7A4A28: 0x147, 0x7A4B70: 0x1BF, 0x7A4D30: 0x445, 0x7A5178: 0xFC, 0x7A5274: 0x260, 0x7A54D4: 0x31A, 0x7A57F0: 0xA5F, 0x7A6250: 0x440, 0x7A6690: 0x26A, 0x7A68FC: 0x795, 0x7A7094: 0x354, 0x7A73E8: 0xC14, 0x7A7FFC: 0x5FA, 0x7A85F8: 0x198, 0x7A8790: 0x72F, 0x7A8EC0: 0x149, 0x7A900C: 0x8FB, 0x7A9908: 0x739, 0x7AA044: 0x300, 0x7AA344: 0x45C, 0x7AA7A0: 0xB6, 0x7AA858: 0x3B8, 0x7AAC10: 0x209, 0x7AAE1C: 0x117, 0x7AAF34: 0x113, 0x7AB048: 0x275, 0x7AB2C0: 0x3A, 0x7AB2FC: 0x1AC, 0x7AB4A8: 0x11D, 0x7AB5C8: 0x55E, 0x7ABB28: 0xA0, 0x7ABBC8: 0x27F, 0x7ABE48: 0x57, 0x7ABEA0: 0x48C, 0x7AC32C: 0x14B, 0x7AC478: 0x7E, 0x7AC4F8: 0xB6, 0x7AC5B0: 0x2CB, 0x7AC87C: 0x7C, 0x7AC8F8: 0x151, 0x7ACA4C: 0x305, 0x7ACD54: 0x685, 0x7AD3DC: 0x1CE, 0x7AD5AC: 0x745, 0x7ADCF4: 0x518, 0x7AE20C: 0x1BA, 0x7AE3C8: 0xB65, 0x7AEF30: 0x7E8, 0x7AF718: 0x4C2, 0x7AFBDC: 0x24BC, 0x7B2098: 0x7CA, 0x7B2864: 0x861, 0x7B30C8: 0x255, 0x7B3320: 0x1B1, 0x7B34D4: 0x240, 0x7B3714: 0x11F, 0x7B3834: 0x43D, 0x7B3C74: 0x522, 0x7B4198: 0x2ED, 0x7B4488: 0x58C, 0x7B4A14: 0x5BA, 0x7CB3F0: 0x9B3, 0x7EA2C8: 0xBE5, 0x7EAEB0: 0xF0, 0x7EAFA0: 0x1FA, 0x7EB19C: 0x7D7, 0x7EB974: 0x133, 0x7EBAA8: 0xB58, 0x7EC600: 0x959, 0x7EF468: 0x672, 0x7F0B40: 0x6F, 0x7F95F8: 0x21, 0x7F961C: 0x2D1, 0x7F98F0: 0x181, 0x7FAC00: 0x4C1}
ArchiveToSizeComp = {0x712318: 0xB24, 0x712E3C: 0x4D5, 0x713314: 0xC3C, 0x72DAFC: 0x1F7F, 0x72FA7C: 0x1E2A, 0x7318A8: 0x9B9, 0x732264: 0xD72, 0x732FD8: 0x41C, 0x7333F4: 0x57A, 0x733970: 0x95B, 0x7342CC: 0x7DB, 0x734AA8: 0xC89, 0x735734: 0xBBF, 0x7362F4: 0x1340, 0x737634: 0xC7C, 0x7382B0: 0x9B4, 0x738C64: 0x91A, 0x739580: 0xBCA, 0x73A14C: 0x6A9, 0x73A7F8: 0x426, 0x73AC20: 0xDA7, 0x73B9C8: 0x158A, 0x73CF54: 0x1A8E, 0x73E9E4: 0xD55, 0x73F73C: 0x1BF, 0x73F8FC: 0xDA1, 0x7406A0: 0x269F, 0x742D40: 0x2747, 0x745488: 0x10ED, 0x746578: 0xE7F, 0x7473F8: 0x721, 0x747B1C: 0xD77, 0x748894: 0xBAE, 0x749444: 0x162A, 0x74AA70: 0x1096, 0x74BB08: 0x1B3, 0x74BCBC: 0x5BF, 0x74C27C: 0x1F08, 0x74E184: 0x1927, 0x74FAAC: 0x79B, 0x750248: 0xA52, 0x750C9C: 0x472, 0x751110: 0x89E, 0x7519B0: 0x13CE, 0x752D80: 0xCC5, 0x753A48: 0x466, 0x753EB0: 0x4E1, 0x754394: 0x96C, 0x754D00: 0x1372, 0x756074: 0xBAC, 0x756C20: 0xB01, 0x757724: 0xFD2, 0x7586F8: 0x30D, 0x758A08: 0xC6, 0x758AD0: 0x8B4, 0x759384: 0x33D, 0x7596C4: 0x34B, 0x759A10: 0x1A3, 0x759BB4: 0x44, 0x759BF8: 0x4BC, 0x75A0B4: 0x743, 0x75A7F8: 0x5AD, 0x75ADA8: 0x842, 0x75B5EC: 0x8C4, 0x75BEB0: 0x9B1, 0x75C864: 0x4FE, 0x75CD64: 0x29F, 0x75D004: 0x1B8, 0x75D1BC: 0x21F, 0x75D3DC: 0x252, 0x75D630: 0x15E, 0x75D790: 0x15A, 0x75D8EC: 0x17A, 0x75DA68: 0x136, 0x75DBA0: 0x44, 0x75DC80: 0x44, 0x75DCC4: 0x1E0, 0x75DEA4: 0x171, 0x75E018: 0x2BB, 0x75E2D4: 0x119, 0x75E3F0: 0x44B, 0x75E83C: 0x56D, 0x75EDAC: 0x58D, 0x75F33C: 0x59C, 0x75F8D8: 0x5B7, 0x75FE90: 0x458, 0x7602E8: 0x110, 0x7603F8: 0x1A2, 0x76059C: 0x146, 0x7606E4: 0x1A3, 0x760888: 0x5A, 0x7608E4: 0x264, 0x760B48: 0x335, 0x760E80: 0x615, 0x761498: 0x4BB, 0x761954: 0x16B, 0x761AC0: 0x14E, 0x761C10: 0x1EE, 0x761E00: 0x94A, 0x76274C: 0x2B8, 0x762A04: 0x2EA, 0x762CF0: 0x43B, 0x76312C: 0x188, 0x7632B4: 0x16A, 0x763420: 0x1DC, 0x7635FC: 0x17D, 0x76377C: 0x18B, 0x763908: 0x1A9, 0x763AB4: 0x1D3, 0x763C88: 0x24E, 0x763ED8: 0x2C9, 0x7641A4: 0x211, 0x7643B8: 0x1542, 0x7658FC: 0x11E1, 0x766AE0: 0xE46, 0x767928: 0x1B8B, 0x7694B4: 0x103E, 0x76A4F4: 0x14B0, 0x76B9A4: 0x180A, 0x76D1B0: 0xAD0, 0x76DC80: 0xE62, 0x76EAE4: 0x1484, 0x76FF68: 0xB27, 0x770A90: 0x7BA, 0x77124C: 0x164A, 0x772898: 0x7E4, 0x77307C: 0x682, 0x773700: 0x7A6, 0x773EA8: 0x820, 0x7746C8: 0x8FF, 0x774FC8: 0x3C5, 0x775390: 0x5A1, 0x775934: 0x643, 0x775F78: 0x1254, 0x7771CC: 0x6BC, 0x777888: 0x651, 0x777EDC: 0x5B8, 0x7E7618: 0xAD5, 0x7E80F0: 0xABA, 0x7E8BAC: 0x3EC, 0x7E8F98: 0x132E, 0x7EE108: 0x1D2, 0x7EE2DC: 0x1DD, 0x7EE4BC: 0x2DB, 0x7EE798: 0x1D2, 0x7EE96C: 0x1DD, 0x7EEB4C: 0x1D4, 0x7EED20: 0x1CB, 0x7EEEEC: 0x1D1, 0x7EF0C0: 0x1D1, 0x7EF294: 0x1D2, 0x7F0BB0: 0x220, 0x7F0DD0: 0x19BB, 0x7F278C: 0x261, 0x7F29F0: 0x1138, 0x7F3B28: 0x210, 0x7F3D38: 0x1228, 0x7F4F60: 0x1E8, 0x7F5148: 0xEF0, 0x7F6038: 0x1BF, 0x7F61F8: 0xD87, 0x7F6F80: 0x1B3, 0x7F7134: 0xA73, 0x7F7BA8: 0x117, 0x7F7CC0: 0x770, 0x800000: 0xE87}
ArchiveToReferences = {0x684F9C: [0x02E38C, 0x12BC7C, 0x1301B8], 0x7043EC: [0x00E858, 0x00E998, 0x00ED8C, 0x010774, 0x010FA0, 0x0157F8, 0x027ABC, 0x02E398, 0x0334DC, 0x0337D8, 0x033B44, 0x0445FC], 0x704E14: [0x00E85C, 0x00E99C, 0x00ED90, 0x010778, 0x010FA4, 0x0157FC, 0x027AC0, 0x02E39C, 0x0334E0, 0x0337DC, 0x033B48, 0x044600], 0x7052F4: [0x00E46C, 0x02E3A4, 0x030368, 0x0447D4], 0x707660: [0x00E470, 0x02E3A8, 0x03036C, 0x0447D8], 0x708A5C: [0x00E860, 0x01580C, 0x027AC4, 0x04460C], 0x708ACC: [0x0069B4, 0x006DF8, 0x00E3CC, 0x00E5C0, 0x00E624, 0x010AA0, 0x0111B4, 0x0156C8], 0x708D30: [0x016094], 0x709600: [0x015BE4], 0x70A498: [0x015BE8], 0x70B350: [0x015BEC], 0x70C1EC: [0x015BF0], 0x70D078: [0x015BF4], 0x70DF40: [0x015BF8], 0x70EE24: [0x015BFC], 0x70FCD0: [0x00A168], 0x710684: [0x00A16C], 0x710DEC: [0x00A170], 0x7112E4: [0x0110D0, 0x027AD0, 0x13036C, 0x1306C4], 0x711CAC: [0x027AB8, 0x031F48, 0x033384, 0x035D54, 0x03D974, 0x044568], 0x712318: [0x033970, 0x0443CC], 0x712E3C: [0x033974], 0x713314: [], 0x713F50: [], 0x713F98: [0x12B914], 0x714078: [0x12B354], 0x7141F4: [0x12F4E0], 0x714654: [0x12D9B0], 0x714794: [0x028B1C, 0x028B20, 0x028B24, 0x028B28, 0x028B2C, 0x028B30, 0x028B34, 0x028B38, 0x028B3C], 0x716C30: [0x028B40, 0x028B44, 0x028B48, 0x028B4C, 0x028B50, 0x028B54, 0x028B58], 0x718E58: [0x028B5C, 0x028B60, 0x028B64, 0x028B68, 0x028B6C], 0x71ABFC: [0x028B70, 0x028B74, 0x028B78, 0x028B7C, 0x028B80, 0x028B84, 0x028B88, 0x028B8C, 0x028B90, 0x028B94], 0x71C950: [0x028B98, 0x028B9C, 0x028BA0, 0x028BA4, 0x028BA8, 0x028BAC, 0x028BB0], 0x71DDE8: [0x028BB4, 0x028BB8, 0x028BBC, 0x028BC0], 0x71F09C: [0x028BC4, 0x028BC8, 0x028BCC, 0x028BD0, 0x028BD4, 0x028BD8], 0x720650: [0x028BDC, 0x028BE0, 0x028BE4, 0x028BE8, 0x028BEC, 0x028BF0], 0x720C58: [0x028BF4, 0x028BF8], 0x721038: [0x028BFC, 0x028C00, 0x028C04, 0x028C08], 0x721240: [0x028C0C, 0x028C10, 0x028C14, 0x028C18, 0x028C1C], 0x721668: [0x028C20, 0x028C24, 0x028C28, 0x028C2C, 0x028C30], 0x721A68: [0x028C34, 0x028C38, 0x028C3C, 0x028C40, 0x028C44, 0x028C54, 0x028C58, 0x028C5C, 0x028C60, 0x028C64, 0x028C68], 0x723E68: [0x028C6C, 0x028C70, 0x028C74, 0x028C78, 0x028C7C, 0x028C80, 0x028C84, 0x028C88, 0x028C8C, 0x028C90, 0x028C94, 0x028C98, 0x028C9C, 0x028CA0, 0x028CA4, 0x028CA8], 0x723F80: [0x028CAC, 0x028CB0, 0x028CB4, 0x028CB8, 0x028CBC, 0x028CC0, 0x028CC4, 0x028CC8, 0x028CCC, 0x028CD0, 0x028CD4, 0x028CD8, 0x028CDC, 0x028CE0, 0x028CE4, 0x028CE8], 0x7245CC: [0x028CEC, 0x028CF0, 0x028CF4, 0x028CF8, 0x028CFC], 0x724728: [0x028D00, 0x028D04, 0x028D08, 0x028D0C], 0x726C34: [0x028D10, 0x028D14, 0x028D18], 0x728B18: [0x028D1C, 0x028D20, 0x028D24], 0x72A980: [0x028D28, 0x028D2C, 0x028D30, 0x028D34], 0x72C278: [0x028D38, 0x028D3C, 0x028D40, 0x028D44, 0x028D48, 0x028D4C, 0x028D50, 0x028D54], 0x72CC90: [0x028D58, 0x028D5C, 0x028D60], 0x72CCDC: [0x0266F8], 0x72DAFC: [0x028854], 0x72FA7C: [0x02664C], 0x7318A8: [0x028858], 0x732264: [0x02885C], 0x732FD8: [0x028860], 0x7333F4: [0x028864], 0x733970: [0x028868], 0x7342CC: [0x02886C], 0x734AA8: [0x028870], 0x735734: [0x028874], 0x7362F4: [0x028878], 0x737634: [0x02887C], 0x7382B0: [0x028880], 0x738C64: [0x028884], 0x739580: [0x028888], 0x73A14C: [0x02888C], 0x73A7F8: [0x028890], 0x73AC20: [0x028894], 0x73B9C8: [0x028898], 0x73CF54: [0x02889C], 0x73E9E4: [0x0288A0], 0x73F73C: [0x0288A4], 0x73F8FC: [0x0288A8], 0x7406A0: [0x0288AC], 0x742D40: [0x026654], 0x745488: [0x0288B0], 0x746578: [0x0288B4], 0x7473F8: [0x0288B8], 0x747B1C: [0x0288BC], 0x748894: [0x0288C0], 0x749444: [0x0288C4], 0x74AA70: [0x0288C8], 0x74BB08: [0x0288CC], 0x74BCBC: [0x0288D0], 0x74C27C: [0x0288D4], 0x74E184: [0x0288D8], 0x74FAAC: [0x0288DC], 0x750248: [0x0288E0], 0x750C9C: [0x0288E4], 0x751110: [0x0288E8], 0x7519B0: [0x0288EC], 0x752D80: [0x0288F0], 0x753A48: [0x0288F4], 0x753EB0: [0x0288F8], 0x754394: [0x0288FC], 0x754D00: [0x028900], 0x756074: [0x028904], 0x756C20: [0x028908], 0x757724: [0x02890C], 0x7586F8: [0x028910], 0x758A08: [0x028914], 0x758AD0: [0x028918], 0x759384: [0x02891C], 0x7596C4: [0x028920], 0x759A10: [0x028924], 0x759BB4: [0x028928], 0x759BF8: [0x02892C], 0x75A0B4: [0x028930], 0x75A7F8: [0x028934], 0x75ADA8: [0x028938], 0x75B5EC: [0x02893C], 0x75BEB0: [0x028940], 0x75C864: [0x028944], 0x75CD64: [0x028948], 0x75D004: [0x02894C], 0x75D1BC: [0x028950], 0x75D3DC: [0x028954], 0x75D630: [0x028958], 0x75D790: [0x02895C], 0x75D8EC: [0x028960], 0x75DA68: [0x028964], 0x75DBA0: [0x028968], 0x75DBE4: [0x12A5E8, 0x12A7B4], 0x75DC80: [0x02896C], 0x75DCC4: [0x028970], 0x75DEA4: [0x028974], 0x75E018: [0x028978], 0x75E2D4: [0x02897C], 0x75E3F0: [0x02898C], 0x75E83C: [0x028990], 0x75EDAC: [0x028994], 0x75F33C: [0x028998], 0x75F8D8: [0x02899C], 0x75FE90: [0x0289A0], 0x7602E8: [0x0289A4], 0x7603F8: [0x0289A8], 0x76059C: [0x0289AC], 0x7606E4: [0x0289B0], 0x760888: [0x0289C4], 0x7608E4: [0x0289E4], 0x760B48: [0x0289E8], 0x760E80: [0x0289EC], 0x761498: [0x0289F0], 0x761954: [0x0289F4], 0x761AC0: [0x0289F8], 0x761C10: [0x0289FC], 0x761E00: [0x028A00], 0x76274C: [0x028A04], 0x762A04: [0x028A08], 0x762CF0: [0x028A0C], 0x76312C: [0x028A10], 0x7632B4: [0x028A14], 0x763420: [0x028A18], 0x7635FC: [0x028A1C], 0x76377C: [0x028A20], 0x763908: [0x028A24], 0x763AB4: [0x028A28], 0x763C88: [0x028A2C], 0x763ED8: [0x028A30], 0x7641A4: [0x028A34], 0x7643B8: [0x028A38], 0x7658FC: [0x028A3C], 0x766AE0: [0x028A40], 0x767928: [0x028A44], 0x7694B4: [0x028A48], 0x76A4F4: [0x028A4C], 0x76B9A4: [0x028A50], 0x76D1B0: [0x028A54], 0x76DC80: [0x028A58], 0x76EAE4: [0x028A5C], 0x76FF68: [0x028A60], 0x770A90: [0x028A64], 0x77124C: [0x028A68], 0x772898: [0x028A6C], 0x77307C: [0x028A70], 0x773700: [0x028A74], 0x773EA8: [0x028A78], 0x7746C8: [0x028A7C], 0x774FC8: [0x028A80], 0x775390: [0x028A84], 0x775934: [0x028A88], 0x775F78: [0x028A8C], 0x7771CC: [0x028A90], 0x777888: [0x028A94], 0x777EDC: [0x028A98], 0x778494: [0x0FE9FC], 0x77873C: [0x0FEB6C], 0x778A40: [0x0FECA4], 0x778BE8: [0x0FEFEC], 0x779334: [0x0FF208], 0x7795E4: [0x0FF3FC], 0x77969C: [0x0FF654], 0x779C04: [0x0FF7D4], 0x779E3C: [0x0FFA70], 0x77A050: [0x0FFD84, 0x1001B8], 0x77A3A4: [0x10038C], 0x77A54C: [0x100584], 0x77A6C0: [0x100724], 0x77A7E4: [0x10096C], 0x77AA34: [0x100E04], 0x77B010: [0x100F50], 0x77B178: [0x10126C], 0x77B24C: [0x10139C], 0x77B33C: [0x101E1C], 0x77B628: [0x101F40], 0x77B754: [0x102090], 0x77B95C: [0x1023A4], 0x77BA54: [0x101514], 0x77BB50: [0x101B68], 0x77BE78: [0x101DAC], 0x77C090: [0x102680, 0x102994], 0x77C560: [0x102BB8], 0x77C704: [0x102C24], 0x77C778: [0x102C2C], 0x77C7B8: [0x102C34], 0x77C7E8: [0x102C28], 0x77C830: [0x102C30], 0x77C87C: [0x102C38], 0x77C8C8: [0x102E98], 0x77C964: [0x1031A0], 0x77CB60: [0x1034D8], 0x77CD08: [0x103704], 0x77D168: [0x1038D0], 0x77D448: [0x103B80], 0x77D8C4: [0x103D84], 0x77DA34: [0x103ED4], 0x77DC00: [0x104190], 0x77DFE4: [0x104270], 0x77E13C: [0x1044C8], 0x77E414: [0x1046E4], 0x77E5AC: [0x104B84], 0x77E874: [0x1050D8], 0x77F084: [0x105288], 0x77F180: [0x105430], 0x77F304: [0x105608], 0x77F500: [0x1057E4], 0x77F5F4: [0x105A10], 0x77F6C0: [0x105C44], 0x77F890: [0x105E48], 0x77F9A4: [0x106090, 0x106450, 0x1065B4], 0x77FEA8: [0x106AEC], 0x7803C0: [0x106C20], 0x78045C: [0x106DD0], 0x780898: [0x10705C], 0x780AA4: [0x1074D0], 0x780C5C: [0x10777C], 0x780FA0: [0x107970], 0x781148: [0x108074, 0x10818C], 0x7811B8: [0x108490], 0x7816DC: [0x10859C], 0x781CD4: [0x108720], 0x7820B8: [0x108A50], 0x782880: [0x108C0C], 0x782B00: [0x108DC0], 0x783280: [0x10901C], 0x783448: [0x109308], 0x783B78: [0x10956C], 0x784038: [0x1097F0], 0x784414: [0x109940], 0x7847C4: [0x109A60], 0x7849B0: [0x109D40], 0x784EA4: [0x10A190], 0x7853E8: [0x10A350], 0x78559C: [0x10A538], 0x785778: [0x10A768], 0x78595C: [0x10A8FC], 0x785AC0: [0x10AAB0], 0x785D64: [0x10B100], 0x786180: [0x10B4C8], 0x78662C: [0x10B728], 0x7867F4: [0x10B888], 0x7869F8: [0x10BBA8], 0x786F28: [0x10BDB4], 0x787160: [0x10BF8C, 0x10C030, 0x10C418], 0x7875DC: [0x10C584], 0x787838: [0x10C748], 0x787A08: [0x10C9F0], 0x788128: [0x10CCB8], 0x7883C4: [0x10CFA0], 0x788784: [0x10D534], 0x7892F4: [0x10D7B0], 0x7896C4: [0x10DAA8], 0x789A28: [0x10DC4C], 0x789C6C: [0x10DFF0], 0x78A104: [0x10E4C0], 0x78A474: [0x10E6E8], 0x78A72C: [0x10E968], 0x78A904: [0x10E96C], 0x78AAE0: [0x10E970], 0x78ACCC: [0x10E974], 0x78AEA8: [0x10ED04], 0x78B400: [0x10EDE4], 0x78B51C: [0x10F17C], 0x78BAC4: [0x10F620], 0x78BEE4: [0x10F8D4], 0x78BFF4: [0x10FBD0], 0x78C4FC: [0x10FFB8], 0x78CCF8: [0x11023C], 0x78D240: [0x1104A8], 0x78D990: [0x110598], 0x78DABC: [0x110C0C], 0x78E15C: [0x110FE4], 0x78EA78: [0x1113D4], 0x78F298: [0x1116E4], 0x78F8FC: [0x111964], 0x78FE2C: [0x111CC4], 0x7902DC: [0x111E18], 0x790850: [0x112054], 0x790BE4: [0x11226C], 0x791248: [0x112484], 0x791750: [0x112624], 0x7917E8: [0x11295C], 0x792098: [0x112BCC], 0x79225C: [0x112EDC], 0x79286C: [0x113030], 0x792F10: [0x113248], 0x79300C: [0x11350C], 0x793324: [0x113834], 0x793A74: [0x113A70], 0x793C8C: [0x113CA0], 0x7943F0: [0x113EF4], 0x7948A8: [0x114068], 0x794F38: [0x11420C], 0x79516C: [0x114428], 0x7953B8: [0x1147BC], 0x795588: [0x114AB4], 0x795884: [0x114DF0], 0x795CD8: [0x114F18], 0x795D68: [0x115034], 0x795DCC: [0x1151F8], 0x795ED8: [0x115364], 0x795FB0: [0x115844], 0x7966D4: [0x11596C], 0x796724: [0x115B20], 0x796A8C: [0x115C7C], 0x796B10: [0x115E30], 0x796DB4: [0x115F48], 0x796E48: [0x1160A0], 0x79711C: [0x116508], 0x797694: [0x116A54], 0x797D30: [0x116C20], 0x798080: [0x116E68], 0x798604: [0x11715C], 0x798B2C: [0x117510], 0x799138: [0x117688], 0x7992E4: [0x11768C], 0x7994B0: [0x11796C, 0x117CAC], 0x799BC4: [0x117E50], 0x799F68: [0x118050], 0x79A41C: [0x118210], 0x79A53C: [0x11838C], 0x79A628: [0x11858C], 0x79A8C0: [0x1188D4], 0x79AAB4: [0x118B30], 0x79AD04: [0x118DC8], 0x79B134: [0x118F54], 0x79B318: [0x119154], 0x79BC18: [0x119270], 0x79BD38: [0x119274], 0x79BE40: [0x119278], 0x79BF58: [0x11927C], 0x79C074: [0x1193C8], 0x79C274: [0x119538], 0x79C400: [0x119844], 0x79C58C: [0x119C80], 0x79C818: [0x119E9C], 0x79C9BC: [0x11A044], 0x79CBEC: [0x11A19C, 0x11A530], 0x79D130: [0x11A868, 0x11ABD8], 0x79D9CC: [0x11AE90], 0x79DBEC: [0x11B124], 0x79DE34: [0x11B320], 0x79E24C: [0x11B460], 0x79E39C: [0x11B6C0], 0x79EA5C: [0x11B984], 0x79F48C: [0x11BCD0], 0x79FD98: [0x11BE40], 0x7A0420: [0x11C188], 0x7A09A8: [0x11C348], 0x7A0B40: [0x11C448], 0x7A0DD0: [0x11C668], 0x7A128C: [0x11CA00], 0x7A15BC: [0x11CBD0], 0x7A1910: [0x11CCF4], 0x7A1EE0: [0x11CFFC], 0x7A23C0: [0x11D23C], 0x7A24A0: [0x11D344], 0x7A26C0: [0x11D43C], 0x7A282C: [0x11D9D4, 0x11DCF4], 0x7A324C: [0x11DEEC], 0x7A356C: [0x11E00C], 0x7A3C20: [0x11E338], 0x7A3D48: [0x11E6A0], 0x7A4424: [0x11E85C], 0x7A4A28: [0x11EA30, 0x11EE30], 0x7A4B70: [0x11EF9C], 0x7A4D30: [0x11F124, 0x11F570], 0x7A5178: [0x11F714], 0x7A5274: [0x11F9EC], 0x7A54D4: [0x11FCCC], 0x7A57F0: [0x11FF04], 0x7A6250: [0x120010, 0x1203E8], 0x7A6690: [0x12053C], 0x7A68FC: [0x1208C4], 0x7A7094: [0x1209CC], 0x7A73E8: [0x120CA4], 0x7A7FFC: [0x120E6C], 0x7A85F8: [0x120FC4], 0x7A8790: [0x121338], 0x7A8EC0: [0x1215A8], 0x7A900C: [0x121A68], 0x7A9908: [0x121ED0], 0x7AA044: [0x122120], 0x7AA344: [0x122508], 0x7AA7A0: [0x12263C], 0x7AA858: [0x12288C], 0x7AAC10: [0x122BB4], 0x7AAE1C: [0x122CC8], 0x7AAF34: [0x122E8C], 0x7AB048: [0x123098, 0x123490], 0x7AB2C0: [0x1235A0], 0x7AB2FC: [0x1236F8], 0x7AB4A8: [0x1239F0], 0x7AB5C8: [0x123BD0, 0x123FD0], 0x7ABB28: [0x12420C], 0x7ABBC8: [0x1246F8], 0x7ABE48: [0x124808], 0x7ABEA0: [0x124B30], 0x7AC32C: [0x124DF4], 0x7AC478: [0x124EE0], 0x7AC4F8: [0x12503C], 0x7AC5B0: [0x1254C0], 0x7AC87C: [0x1255E4], 0x7AC8F8: [0x125728], 0x7ACA4C: [0x125ACC], 0x7ACD54: [0x125C68, 0x125CD8, 0x125D68, 0x126188], 0x7AD3DC: [0x12647C], 0x7AD5AC: [0x1268C8], 0x7ADCF4: [0x1269F0, 0x126A3C, 0x126A8C, 0x126CD8], 0x7AE20C: [0x127030], 0x7AE3C8: [0x1271A8, 0x1271DC, 0x12722C, 0x127298, 0x1276CC], 0x7AEF30: [0x127B18], 0x7AF718: [0x127C2C, 0x127CB8, 0x127CEC, 0x127D44, 0x127FE8, 0x128130], 0x7AFBDC: [0x128648, 0x128CB0, 0x128F8C, 0x129248, 0x129664], 0x7B2098: [0x04A8E8, 0x04A91C, 0x04A930, 0x04A944, 0x04A980, 0x04A994], 0x7B2864: [0x12A34C, 0x12A570], 0x7B30C8: [0x129BB0], 0x7B3320: [0x129FC0], 0x7B34D4: [0x129BB4], 0x7B3714: [0x129FC4], 0x7B3834: [0x129BB8], 0x7B3C74: [0x129FC8], 0x7B4198: [0x129BBC, 0x12ABD8], 0x7B4488: [0x129FCC, 0x12B038], 0x7B4A14: [0x12F9A4, 0x12FB44, 0x12FBBC, 0x12FC04, 0x12FC24, 0x12FCFC, 0x12FE34, 0x12FE54, 0x12FE7C, 0x12FEB0, 0x130158], 0x7CB3F0: [0x02BA8C], 0x7E7618: [0x033968], 0x7E80F0: [0x03396C], 0x7E8BAC: [0x035908], 0x7E8F98: [0x035910], 0x7EA2C8: [0x030360], 0x7EAEB0: [0x027AC8, 0x0333D0], 0x7EAFA0: [0x027ACC, 0x02E854, 0x02F63C, 0x031AA8, 0x032CEC, 0x033540, 0x037664, 0x044664], 0x7EB19C: [0x02EA7C, 0x0404B4, 0x040AAC, 0x0447E0], 0x7EB974: [0x02EA84], 0x7EBAA8: [0x03C258], 0x7EC600: [0x13101C, 0x1311C4], 0x7EE108: [0x043DC0, 0x043DD0, 0x043DF0, 0x043E10, 0x043E40], 0x7EE2DC: [0x043E00], 0x7EE4BC: [0x043F20], 0x7EE798: [0x043DE0, 0x043E20, 0x043E30, 0x043EC0], 0x7EE96C: [0x043E50, 0x043EA0], 0x7EEB4C: [0x043E60, 0x043E80], 0x7EED20: [0x043E70, 0x043E90, 0x043ED0], 0x7EEEEC: [0x043EB0], 0x7EF0C0: [0x043EE0], 0x7EF294: [0x043EF0, 0x043F00, 0x043F10], 0x7EF468: [0x032874, 0x04162C, 0x12D698, 0x12D848], 0x7F0B40: [0x043698], 0x7F0BB0: [0x04335C], 0x7F0DD0: [0x043360], 0x7F278C: [0x043364], 0x7F29F0: [0x043368], 0x7F3B28: [0x04336C], 0x7F3D38: [0x043370], 0x7F4F60: [0x043374], 0x7F5148: [0x043378], 0x7F6038: [0x04337C], 0x7F61F8: [0x043380], 0x7F6F80: [0x043384], 0x7F7134: [0x043388], 0x7F7BA8: [0x04338C], 0x7F7CC0: [0x043390], 0x7F95F8: [0x1305DC, 0x130670], 0x7F961C: [0x1312F0, 0x1313A8], 0x7F98F0: [0x131500, 0x13155C], 0x7FAC00: [0x0486DC], 0x800000: [0x028874]}
#UncompressedArchives = [0x684F9C, 0x7043EC, 0x704E14, 0x7052F4, 0x707660, 0x708A5C, 0x708ACC, 0x708D30, 0x709600, 0x70A498, 0x70B350, 0x70C1EC, 0x70D078, 0x70DF40, 0x70EE24, 0x70FCD0, 0x710684, 0x710DEC, 0x7112E4, 0x711CAC, 0x713F50, 0x713F98, 0x714078, 0x7141F4, 0x714654, 0x714794, 0x716C30, 0x718E58, 0x71ABFC, 0x71C950, 0x71DDE8, 0x71F09C, 0x720650, 0x720C58, 0x721038, 0x721240, 0x721668, 0x721A68, 0x723E68, 0x723F80, 0x7245CC, 0x724728, 0x726C34, 0x728B18, 0x72A980, 0x72C278, 0x72CC90, 0x72CCDC, 0x75DBE4, 0x778494, 0x77873C, 0x778A40, 0x778BE8, 0x779334, 0x7795E4, 0x77969C, 0x779C04, 0x779E3C, 0x77A050, 0x77A3A4, 0x77A54C, 0x77A6C0, 0x77A7E4, 0x77AA34, 0x77B010, 0x77B178, 0x77B24C, 0x77B33C, 0x77B628, 0x77B754, 0x77B95C, 0x77BA54, 0x77BB50, 0x77BE78, 0x77C090, 0x77C560, 0x77C704, 0x77C778, 0x77C7B8, 0x77C7E8, 0x77C830, 0x77C87C, 0x77C8C8, 0x77C964, 0x77CB60, 0x77CD08, 0x77D168, 0x77D448, 0x77D8C4, 0x77DA34, 0x77DC00, 0x77DFE4, 0x77E13C, 0x77E414, 0x77E5AC, 0x77E874, 0x77F084, 0x77F180, 0x77F304, 0x77F500, 0x77F5F4, 0x77F6C0, 0x77F890, 0x77F9A4, 0x77FEA8, 0x7803C0, 0x78045C, 0x780898, 0x780AA4, 0x780C5C, 0x780FA0, 0x781148, 0x7811B8, 0x7816DC, 0x781CD4, 0x7820B8, 0x782880, 0x782B00, 0x783280, 0x783448, 0x783B78, 0x784038, 0x784414, 0x7847C4, 0x7849B0, 0x784EA4, 0x7853E8, 0x78559C, 0x785778, 0x78595C, 0x785AC0, 0x785D64, 0x786180, 0x78662C, 0x7867F4, 0x7869F8, 0x786F28, 0x787160, 0x7875DC, 0x787838, 0x787A08, 0x788128, 0x7883C4, 0x788784, 0x7892F4, 0x7896C4, 0x789A28, 0x789C6C, 0x78A104, 0x78A474, 0x78A72C, 0x78A904, 0x78AAE0, 0x78ACCC, 0x78AEA8, 0x78B400, 0x78B51C, 0x78BAC4, 0x78BEE4, 0x78BFF4, 0x78C4FC, 0x78CCF8, 0x78D240, 0x78D990, 0x78DABC, 0x78E15C, 0x78EA78, 0x78F298, 0x78F8FC, 0x78FE2C, 0x7902DC, 0x790850, 0x790BE4, 0x791248, 0x791750, 0x7917E8, 0x792098, 0x79225C, 0x79286C, 0x792F10, 0x79300C, 0x793324, 0x793A74, 0x793C8C, 0x7943F0, 0x7948A8, 0x794F38, 0x79516C, 0x7953B8, 0x795588, 0x795884, 0x795CD8, 0x795D68, 0x795DCC, 0x795ED8, 0x795FB0, 0x7966D4, 0x796724, 0x796A8C, 0x796B10, 0x796DB4, 0x796E48, 0x79711C, 0x797694, 0x797D30, 0x798080, 0x798604, 0x798B2C, 0x799138, 0x7992E4, 0x7994B0, 0x799BC4, 0x799F68, 0x79A41C, 0x79A53C, 0x79A628, 0x79A8C0, 0x79AAB4, 0x79AD04, 0x79B134, 0x79B318, 0x79BC18, 0x79BD38, 0x79BE40, 0x79BF58, 0x79C074, 0x79C274, 0x79C400, 0x79C58C, 0x79C818, 0x79C9BC, 0x79CBEC, 0x79D130, 0x79D9CC, 0x79DBEC, 0x79DE34, 0x79E24C, 0x79E39C, 0x79EA5C, 0x79F48C, 0x79FD98, 0x7A0420, 0x7A09A8, 0x7A0B40, 0x7A0DD0, 0x7A128C, 0x7A15BC, 0x7A1910, 0x7A1EE0, 0x7A23C0, 0x7A24A0, 0x7A26C0, 0x7A282C, 0x7A324C, 0x7A356C, 0x7A3C20, 0x7A3D48, 0x7A4424, 0x7A4A28, 0x7A4B70, 0x7A4D30, 0x7A5178, 0x7A5274, 0x7A54D4, 0x7A57F0, 0x7A6250, 0x7A6690, 0x7A68FC, 0x7A7094, 0x7A73E8, 0x7A7FFC, 0x7A85F8, 0x7A8790, 0x7A8EC0, 0x7A900C, 0x7A9908, 0x7AA044, 0x7AA344, 0x7AA7A0, 0x7AA858, 0x7AAC10, 0x7AAE1C, 0x7AAF34, 0x7AB048, 0x7AB2C0, 0x7AB2FC, 0x7AB4A8, 0x7AB5C8, 0x7ABB28, 0x7ABBC8, 0x7ABE48, 0x7ABEA0, 0x7AC32C, 0x7AC478, 0x7AC4F8, 0x7AC5B0, 0x7AC87C, 0x7AC8F8, 0x7ACA4C, 0x7ACD54, 0x7AD3DC, 0x7AD5AC, 0x7ADCF4, 0x7AE20C, 0x7AE3C8, 0x7AEF30, 0x7AF718, 0x7AFBDC, 0x7B2098, 0x7B2864, 0x7B30C8, 0x7B3320, 0x7B34D4, 0x7B3714, 0x7B3834, 0x7B3C74, 0x7B4198, 0x7B4488, 0x7B4A14, 0x7CB3F0, 0x7EA2C8, 0x7EAEB0, 0x7EAFA0, 0x7EB19C, 0x7EB974, 0x7EBAA8, 0x7EC600, 0x7EF468, 0x7F0B40, 0x7F95F8, 0x7F961C, 0x7F98F0, 0x7FAC00]


charDict = {
    ' ': 0x00, '0': 0x01, '1': 0x02, '2': 0x03, '3': 0x04, '4': 0x05, '5': 0x06, '6': 0x07, '7': 0x08, '8': 0x09, '9': 0x0A,
    'A': 0x0B, 'B': 0x0C, 'C': 0x0D, 'D': 0x0E, 'E': 0x0F, 'F': 0x10, 'G': 0x11, 'H': 0x12, 'I': 0x13, 'J': 0x14, 'K': 0x15,
    'L': 0x16, 'M': 0x17, 'N': 0x18, 'O': 0x19, 'P': 0x1A, 'Q': 0x1B, 'R': 0x1C, 'S': 0x1D, 'T': 0x1E, 'U': 0x1F, 'V': 0x20,
    'W': 0x21, 'X': 0x22, 'Y': 0x23, 'Z': 0x24, 'a': 0x25, 'b': 0x26, 'c': 0x27, 'd': 0x28, 'e': 0x29, 'f': 0x2A, 'g': 0x2B,
    'h': 0x2C, 'i': 0x2D, 'j': 0x2E, 'k': 0x2F, 'l': 0x30, 'm': 0x31, 'n': 0x32, 'o': 0x33, 'p': 0x34, 'q': 0x35, 'r': 0x36,
    's': 0x37, 't': 0x38, 'u': 0x39, 'v': 0x3A, 'w': 0x3B, 'x': 0x3C, 'y': 0x3D, 'z': 0x3E, '-': 0x3F, '×': 0x40, '=': 0x41,
    ':': 0x42, '+': 0x43, '÷': 0x44, '※': 0x45, '*': 0x46, '!': 0x47, '?': 0x48, '%': 0x49, '&': 0x4A, ',': 0x4B, '⋯': 0x4C,
    '.': 0x4D, '・': 0x4E, ';': 0x4F, '\'': 0x50, '\"': 0x51, '~': 0x52, '/': 0x53, '(': 0x54, ')': 0x55, '「': 0x56, '」': 0x57,
    "V2": 0x58, "V3": 0x59, "V4": 0x5A, "V5": 0x5B, '@': 0x5C, '♥': 0x5D, '♪': 0x5E, "MB": 0x5F, '■': 0x60, '_': 0x61,
    "circle1": 0x62, "circle2": 0x63, "cross1": 0x64, "cross2": 0x65, "bracket1": 0x66, "bracket2": 0x67, "ModTools1": 0x68,
    "ModTools2": 0x69, "ModTools3": 0x6A, 'Σ': 0x6B, 'Ω': 0x6C, 'α': 0x6D, 'β': 0x6E, '#': 0x6F, '…': 0x70, '>': 0x71,
    '<': 0x72, 'エ': 0x73, "BowneGlobal1": 0x74, "BowneGlobal2": 0x75, "BowneGlobal3": 0x76, "BowneGlobal4": 0x77,
    "BowneGlobal5": 0x78, "BowneGlobal6": 0x79, "BowneGlobal7": 0x7A, "BowneGlobal8": 0x7B, "BowneGlobal9": 0x7C,
    "BowneGlobal10": 0x7D, "BowneGlobal11": 0x7E, '\n': 0xE8, 'ω': 0x6C
}

undernet_item_indices = [27, 28, 29, 30, 31, 32, 58, 34, 34]


def read_u16_le(data, offset) -> int:
    low_byte = data[offset]
    high_byte = data[offset+1]
    return (high_byte << 8) + low_byte


def read_u32_le(data, offset) -> int:
    low_byte = data[offset]
    high_byte = data[offset+1]
    higher_byte = data[offset+2]
    highest_byte = data[offset+3]
    return (highest_byte << 24) + (higher_byte << 16) +(high_byte << 8) + low_byte


def int32_to_byte_list_le(x) -> bytearray:
    byte32_string = "{:08x}".format(x)
    data = bytearray.fromhex(byte32_string)
    data.reverse()
    return data


def int16_to_byte_list_le(x) -> bytearray:
    byte32_string = "{:04x}".format(x)
    data = bytearray.fromhex(byte32_string)
    data.reverse()
    return data


def generate_text_bytes(message) -> bytearray:
    return bytearray(char_to_hex(c) for c in message)


def char_to_hex(c) -> int:
    if c in charDict:
        return charDict[c]
    else:
        # If the character doesn't exist, return one of the mod tools error characters
        # Yes, it _is_ a coincidence this happens to be 69
        return 0x69

def generate_chip_get(chip, code, amt) -> bytearray:
    chip_bytes = int16_to_byte_list_le(chip)
    byte_list = [0xF6, 0x10, chip_bytes[0], chip_bytes[1], code, amt]
    byte_list.extend(generate_text_bytes("Got a chip for\n\""))
    byte_list.extend([0xF9, 0x00, chip_bytes[0], 0x01 if chip < 256 else 0x02, 0x00, 0xF9, 0x00, code, 0x03])
    byte_list.extend(generate_text_bytes("\"!!"))
    return bytearray(byte_list)


def generate_key_item_get(item, amt) -> bytearray:
    byte_list = [0xF6, 0x00, item, amt]
    byte_list.extend(generate_text_bytes("Got a \n\""))
    byte_list.extend([0xF9, 0x00, item, 0x00])
    byte_list.extend(generate_text_bytes("\"!!"))
    return bytearray(byte_list)


def generate_sub_chip_get(subchip, amt) -> bytearray:
    # SubChips have an extra bit of trouble.
    # If you have too many, they're supposed to skip to another text bank that doesn't give you the item
    # Instead, I'm going to just let it get eaten. Script indices are at a premium and I can't always add one
    # It's more important to use them for progressive Undernet
    byte_list = [0xF6, 0x20, subchip, amt, 0xFF, 0xFF, 0xFF]
    byte_list.extend(generate_text_bytes("Got a \nSubChip for\n\""))
    byte_list.extend([0xF9, 0x00, subchip, 0x00])
    byte_list.extend(generate_text_bytes("\"!!"))
    return bytearray(byte_list)


def generate_zenny_get(amt) -> bytearray:
    zenny_bytes = int32_to_byte_list_le(amt)
    byte_list = [0xF6, 0x30, *zenny_bytes, 0xFF, 0xFF, 0xFF]
    byte_list.extend(generate_text_bytes(f"Got \n\"{amt} Zennys\"!!"))
    return bytearray(byte_list)


def generate_program_get(program, color, amt) -> bytearray:
    # Programs are bit shifted twice to generate the "give" bit
    byte_list = [0xF6, 0x40, program << 2, amt, color]
    byte_list.extend(generate_text_bytes("Got a Navi\nCustomizer Program:\n\""))
    byte_list.extend([0xF9, 0x00, program, 0x05])
    return bytearray(byte_list)


def generate_bugfrag_get(amt) -> bytearray:
    frag_bytes = int32_to_byte_list_le(amt)
    byte_list = [0xF6, 0x50, frag_bytes[0], frag_bytes[1], frag_bytes[2], frag_bytes[3], 0xFF, 0xFF, 0xFF]
    byte_list.extend(generate_text_bytes("Got:\n\"" + str(amt) + " BugFrags\"!!"))
    return bytearray(byte_list)


# This one is meant to be "silent". The text box has already been displayed.
# So this one just gives the item using the text box syntax
def generate_progressive_undernet(progression_index, next_script) -> bytearray:
    if progression_index >= 8:
        # If we're at max rank, give bugfrags instead
        frag_bytes = int32_to_byte_list_le(20)
        byte_list = [0xF6, 0x50, frag_bytes[0], frag_bytes[1], frag_bytes[2], frag_bytes[3], 0xFF, 0xFF, 0xFF]
        byte_list.extend(generate_text_bytes("The extra data\ndecompiles into:\n\"20 BugFrags\"!!"))
    else:
        # F6 03 - Check for item. If you have it, load next_script, otherwise, continue
        byte_list = [0xf6, 0x03, undernet_item_indices[progression_index], 0x01, next_script, next_script, 0xFF, 0xE9]

        # Otherwise, give the item, with different code depending on if we're at max rank already or not
        byte_list.extend(generate_key_item_get(undernet_item_indices[progression_index], 1))
    byte_list.extend([0xEB, 0xE7]) # End the message
    return bytearray(byte_list)


def generate_get_for_item(item) -> bytearray:
    if item.type == ItemType.Undernet:
        return generate_text_bytes("Got the next\n\"Undernet Rank\"!!")
    elif item.type == ItemType.Chip:
        return generate_chip_get(item.itemID, item.subItemID, item.count)
    elif item.type == ItemType.KeyItem:
        return generate_key_item_get(item.itemID, item.count)
    elif item.type == ItemType.SubChip:
        return generate_sub_chip_get(item.itemID, item.count)
    elif item.type == ItemType.Zenny:
        return generate_zenny_get(item.count)
    elif item.type == ItemType.Program:
        return generate_program_get(item.itemID, item.subItemID, item.count)
    elif item.type == ItemType.BugFrag:
        return generate_bugfrag_get(item.count)

    return generate_text_bytes("Empty Message")


def generate_item_message(item_data) -> bytearray:
    byte_list = [0xF8, 0x04, 0x18]  # Play Animation
    byte_list.extend([0xED, 0x01])  # Hide Mugshot
    byte_list.extend(generate_get_for_item(item_data))
    byte_list.extend([0xF8, 0x0C])
    byte_list.extend([0xEB, 0xE9, 0xF8, 0x08])
    byte_list.extend([0xF8, 0x10])
    return bytearray(byte_list)


def generate_external_item_message(item_name, item_recipient) -> bytearray:
    byte_list = [0xF8, 0x04, 0x18]  # Play Animation
    item_name_pascal = shorten_item_name(item_name)
    byte_list.extend([0xED, 0x01])  # Hide Mugshot
    byte_list.extend([0xFA, 0x00, 0x85, 0x00])  # Play Sound
    byte_list.extend(generate_text_bytes("Sending data for\n" + item_name_pascal + "\nTo " + item_recipient))
    byte_list.extend([0xF8, 0x0C])
    byte_list.extend([0xEB, 0xE9, 0xF8, 0x08])
    byte_list.extend([0xF8, 0x10])
    return bytearray(byte_list)


def shorten_item_name(item_name):
    maxLength = 20
    # If it's short enough, just use it
    if len(item_name) <= maxLength:
        return item_name
    # Next, PascalCase it
    item_name = item_name.replace("_", " ").replace("-", " ").title().replace(" ", "")
    if len(item_name) <= maxLength:
        return item_name
    # If it's still too long, start removing vowels till it's short enough or we run out
    while len(item_name) > maxLength and any(c in item_name for c in ['a', 'e', 'i', 'o', 'u']):
        item_name = re.sub("[aeiou]", "", item_name, 1)
    # If it's somehow still too long, truncate and return
    return item_name[0:maxLength]
