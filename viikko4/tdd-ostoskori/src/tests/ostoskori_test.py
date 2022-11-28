import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1 = Tuote("banaani",1)
        self.tuote2 = Tuote("leivos",2)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.setUp()
        self.assertEqual(self.kori.hinta(), 0)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yksi_tuote_lisataan_oikein(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        saldo = self.kori.tavaroita_korissa()
        self.assertEqual(saldo, 1)

    def test_yksi_tuote_lisataan_ja_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        hinta = self.kori.hinta()
        self.assertEqual(hinta, 1)

    def test_kaksi_eri_tuotetta_lisataan_ja_ostoskorin_lkm_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        saldo = self.kori.tavaroita_korissa()
        self.assertEqual(saldo, 2)

    def test_kaksi_eri_tuotetta_lisataan_ja_ostoskorin_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        hinta = self.kori.hinta()
        self.assertEqual(hinta, 3)

    def test_kaksi_samaa_tuotetta_lisataan_ja_ostoskorin_lkm_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        saldo = self.kori.tavaroita_korissa()
        self.assertEqual(saldo, 2)

    def test_kaksi_samaa_tuotetta_lisataan_ja_ostoskorin_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        hinta = self.kori.hinta()
        self.assertEqual(hinta, 2)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.tuote1)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),1)

        # testaa että metodin palauttaman listan pituus 1
    
