import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class

from ..KontoFirmowe import KontoFirmowe


class TestKredytFirmowy(unittest.TestCase):
    nazwa_firmy = "Bamboleo sp. z o.o."
    nip = "1234567890"
    
    @patch('app.KontoFirmowe.KontoFirmowe.walidacja_nip_api', return_value=True)
    def setUp(self, mock):
        self.konto = KontoFirmowe(self.nazwa_firmy, self.nip)

    @parameterized.expand([
        ([12000, -1775], 5000,  True, 5000),  # ok
        ([-1775], 6000, False, 0),  # bez warunku 1
        ([10000], 4000, False, 0),  # bez warunku 2
        ([3000, -1775], 3000, False, 0)  # bez obu warunków
    ])
    def test_kredyt_firmowy_przyznanie(self, historia, kwota, przyznanie, saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, przyznanie)
        self.assertEqual(self.konto.saldo, saldo)
