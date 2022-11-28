import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1 = Tuote("banaani",1)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.setUp()
        self.assertEqual(self.kori.hinta(), 0)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # def test_yksi_tuote_lisataan_oikein(self):
    #     self.setUp()
    #     self.kori.lisaa_tuote(self.tuote1)
    #     saldo = self.kori.tavaroita_korissa()
    #     self.assertEqual(saldo, 1)

    
