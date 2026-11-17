import unittest

from metodos_numericos.trapezios import calcular_energias
from projeto_2GQ.analise_energia.energia import calcular_energias as calcular_energia_projeto
from projeto_2GQ.analise_energia.leitura import horas, potencias


class TestCalcularEnergias(unittest.TestCase):
    def test_um_intervalo_com_duracao_diferente_de_duas_horas(self):
        energias, total = calcular_energias([(1, 10), (4, 20)])

        self.assertEqual(energias, [45])
        self.assertEqual(total, 45)

    def test_doze_intervalos_do_projeto(self):
        esperadas = [
            242.23, 245.34, 259.44, 272.75, 294.00, 334.73,
            362.34, 354.14, 329.63, 296.19, 263.89, 249.86,
        ]
        energias, total = calcular_energia_projeto(zip(horas, potencias))

        self.assertEqual(len(energias), len(esperadas))
        for intervalo, (obtida, esperada) in enumerate(zip(energias, esperadas), start=1):
            with self.subTest(intervalo=intervalo):
                self.assertAlmostEqual(obtida, esperada)
        self.assertAlmostEqual(total, sum(energias))
        self.assertAlmostEqual(total, 3504.54)

    def test_sem_arredondamento_durante_o_calculo(self):
        energias, total = calcular_energias([(0, 1), (0.25, 2), (0.75, 2.125)])

        self.assertEqual(energias, [0.375, 1.03125])
        self.assertEqual(total, 1.40625)

    def test_entradas_invalidas(self):
        casos = [
            ([], "pelo menos duas"),
            ([(0, 10)], "pelo menos duas"),
            ([(2, 10), (0, 20)], "estritamente crescente"),
            ([(0, 10), (0, 20)], "estritamente crescente"),
            ([(0, 10), ("2", 20)], "números reais finitos"),
            ([(0, 10), (2, "20")], "números reais finitos"),
            ([(0, 10), (float("inf"), 20)], "números reais finitos"),
            ([(0, 10), (2, float("nan"))], "números reais finitos"),
            ([(0, 10), (2, True)], "números reais finitos"),
            ([(0, 10), (2,)], "deve ser um par"),
        ]
        for medicoes, mensagem in casos:
            with self.subTest(medicoes=medicoes):
                with self.assertRaisesRegex(ValueError, mensagem):
                    calcular_energias(medicoes)
