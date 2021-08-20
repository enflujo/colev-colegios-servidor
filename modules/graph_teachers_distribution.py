import pandas as pd


def build(args):
    # Get number of teachers per education level
    n_teachers_preschool = args.n_teachers_preschool
    n_teachers_primary = args.n_teachers_primary
    n_teachers_highschool = args.n_teachers_highschool

    total_teachers_system = n_teachers_preschool + n_teachers_primary + n_teachers_highschool

    teachers_preschool_ = [int(n_teachers_preschool)]
    teachers_primary_ = [int(n_teachers_primary)]
    teachers_highschool_ = [int(n_teachers_highschool)]

    return {
        "preschool": [teachers_preschool_, sum(teachers_preschool_) / total_teachers_system],
        "primary": [teachers_primary_, sum(teachers_primary_) / total_teachers_system],
        "highschool": [teachers_highschool_, sum(teachers_highschool_) / total_teachers_system],
        "total": total_teachers_system,
    }

# def build(args):
#     teachers_data_BOG = pd.read_csv(args.teachers_data_path, encoding="unicode_escape", delimiter=",")
#     total_teachers_BOG = int(teachers_data_BOG["Total"][1])

#     teachers_preschool_ = [int(teachers_data_BOG["Preescolar"][1])]
#     teachers_primary_ = [int(teachers_data_BOG["Basica_primaria"][1])]
#     teachers_highschool_ = [int(teachers_data_BOG["Basica_secundaria"][1])]

#     return {
#         "preschool": [teachers_preschool_, sum(teachers_preschool_) / total_teachers_BOG],
#         "primary": [teachers_primary_, sum(teachers_primary_) / total_teachers_BOG],
#         "highschool": [teachers_highschool_, sum(teachers_highschool_) / total_teachers_BOG],
#         "total": total_teachers_BOG,
#     }


def cache(args):
    ########################### Static teachers distribution ################################################
    teachers = {
        "bogota": {
            "preschool": [[9701], 0.1507443204773596],
            "primary": [[22662], 0.3521459427541412],
            "highschool": [[19927], 0.3096466420113746],
            "total": 64354,
        }
    }

    return teachers[args.city]
