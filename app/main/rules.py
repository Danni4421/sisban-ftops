from libs.fuzzy import *


def init_rules():
    return (
        # Rule: If Gaji Sangat Sedikit & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Sedikit & Pengeluaran Sedikit THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Sedikit & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Sedikit & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sedikit & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sedikit & Pengeluaran Sedikit THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sedikit & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sedikit & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Banyak & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Banyak & Pengeluaran Sedikit THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Banyak & Pengeluaran Banyak THEN Kondisi Ekonomi Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Banyak & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Kurang
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Banyak & Pengeluaran Sangat Sedikit THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Banyak & Pengeluaran Sedikit THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Banyak & Pengeluaran Banyak THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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

        # Rule: If Gaji Sangat Banyak & Pengeluaran Sangat Banyak THEN Kondisi Ekonomi Sangat Mampu
        FuzzyRule(
            antecedent={
                'gaji': {
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
