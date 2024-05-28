from libs.fuzzy import *

RULES_SUMMARY = [
    "Jika Penghasilan Sangat Sedikit dan Pengeluaran Sangat Sedikit, Maka Kurang.",
    "Jika Penghasilan Sangat Sedikit dan Pengeluaran Sedikit, Maka Sangat Kurang.",
    "Jika Penghasilan Sangat Sedikit dan Pengeluaran Banyak, Maka Sangat Kurang.",
    "Jika Penghasilan Sangat Sedikit dan Pengeluaran Sangat Banyak, Maka Sangat Kurang.",
    "Jika Penghasilan Sedikit dan Pengeluaran Sangat Sedikit, Maka Kurang.",
    "Jika Penghasilan Sedikit dan Pengeluaran Sedikit, Maka Kurang.",
    "Jika Penghasilan Sedikit dan Pengeluaran Banyak, Maka Sangat Kurang.",
    "Jika Penghasilan Sedikit dan Pengeluaran Sangat Banyak, Maka Sangat Kurang.",
    "Jika Penghasilan Banyak dan Pengeluaran Sangat Sedikit, Maka Mampu.",
    "Jika Penghasilan Banyak dan Pengeluaran Sedikit, Maka Mampu.",
    "Jika Penghasilan Banyak dan Pengeluaran Banyak, Maka Mampu.",
    "Jika Penghasilan Banyak dan Pengeluaran Sangat Banyak, Maka Kurang.",
    "Jika Penghasilan Sangat Banyak dan Pengeluaran Sangat Sedikit, Maka Sangat Mampu.",
    "Jika Penghasilan Sangat Banyak dan Pengeluaran Sedikit, Maka Sangat Mampu.",
    "Jika Penghasilan Sangat Banyak dan Pengeluaran Banyak, Maka Sangat Mampu.",
    "Jika Penghasilan Sangat Banyak dan Pengeluaran Sangat Banyak, Maka Sangat Mampu.",
]

def init_rules():
    return (
        # Rule: If Penghasilan Sangat Sedikit & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1})
                }
            },
            consequent= {
                'member_name': 'kurang',
                'member': LinearUp(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sangat Sedikit & Pengeluaran Sedikit THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1.5})
                },
                'pengeluaran': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1, 'middle_two': 1.5, 'max': 3})
                }
            },
            consequent={
                'member_name': 'sangat_kurang',
                'member': LinearDown(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sangat Sedikit & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1.5})
                },
                'pengeluaran':  {
                    'member_name': 'banyak',
                    'member': Triangle(config={'min': 1.5, 'middle': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_kurang',
                'member': LinearDown(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sangat Sedikit & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_kurang',
                'member': LinearDown(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sedikit & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1.5, 'middle_two': 2,  'max': 3.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1})
                }
            },
            consequent={
                'member_name': 'kurang',
                'member': LinearUp(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sedikit & Pengeluaran Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1.5, 'middle_two': 2, 'max': 3.5})
                },
                'pengeluaran': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1, 'middle_two': 1.5, 'max': 3})
                }
            },
            consequent={
                'member_name': 'kurang',
                'member': LinearUp(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sedikit & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1.5, 'middle_two': 2, 'max': 3.5})
                },
                'pengeluaran':  {
                    'member_name': 'banyak',
                    'member': Triangle(config={'min': 1.5, 'middle': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_kurang',
                'member': LinearDown(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sedikit & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1.5, 'middle_two': 2, 'max': 3.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_kurang',
                'member': LinearDown(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Banyak & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'banyak',
                    'member': Trapezium(config={'min': 2, 'middle_one': 3.5, 'middle_two': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1})
                }
            },
            consequent={
                'member_name': 'mampu',
                'member': LinearUp(config={'min': 50, 'max': 60})
            }
        ),

        # Rule: If Penghasilan Banyak & Pengeluaran Sedikit THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'banyak',
                    'member': Trapezium(config={'min': 2, 'middle_one': 3.5, 'middle_two': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1, 'middle_two': 1.5, 'max': 3})
                }
            },
            consequent={
                'member_name': 'mampu',
                'member': LinearUp(config={'min': 50, 'max': 60})
            }
        ),

        # Rule: If Penghasilan Banyak & Pengeluaran Banyak THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'banyak',
                    'member': Trapezium(config={'min': 2, 'middle_one': 3.5, 'middle_two': 4, 'max': 6.5})
                },
                'pengeluaran':  {
                    'member_name': 'banyak',
                    'member': Triangle(config={'min': 1.5, 'middle': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'mampu',
                'member': LinearUp(config={'min': 50, 'max': 60})
            }
        ),

        # Rule: If Penghasilan Banyak & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'banyak',
                    'member': Trapezium(config={'min': 2, 'middle_one': 3.5, 'middle_two': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'kurang',
                'member': LinearUp(config={'min': 20, 'max': 30})
            }
        ),

        # Rule: If Penghasilan Sangat Banyak & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_sedikit',
                    'member': LinearDown(config={'min': 0.5, 'max': 1})
                }
            },
            consequent={
                'member_name': 'sangat_mampu',
                'member': LinearUp(config={'min': 75, 'max': 80})
            }
        ),

        # Rule: If Penghasilan Sangat Banyak & Pengeluaran Sedikit THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sedikit',
                    'member': Trapezium(config={'min': 0.5, 'middle_one': 1, 'middle_two': 1.5, 'max': 3})
                }
            },
            consequent={
                'member_name': 'sangat_mampu',
                'member': LinearUp(config={'min': 75, 'max': 80})
            }
        ),

        # Rule: If Penghasilan Sangat Banyak & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 4, 'max': 6.5})
                },
                'pengeluaran':  {
                    'member_name': 'banyak',
                    'member': Triangle(config={'min': 1.5, 'middle': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_mampu',
                'member': LinearUp(config={'min': 75, 'max': 80})
            }
        ),

        # Rule: If Penghasilan Sangat Banyak & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'penghasilan': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 4, 'max': 6.5})
                },
                'pengeluaran': {
                    'member_name': 'sangat_banyak',
                    'member': LinearUp(config={'min': 3, 'max': 5})
                }
            },
            consequent={
                'member_name': 'sangat_mampu',
                'member': LinearUp(config={'min': 75, 'max': 80})
            }
        )
    )
