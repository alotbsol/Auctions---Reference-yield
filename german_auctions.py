"""Past german auctions: submitted/won/max bid{project size"""
auctions_supply_demand_test = {"May_17": [214, 70, 70, 11.528],
                          "Aug_17": [293, 67, 70, 15.11],
                         }

auctions_supply_demand = {"2017_05": [256, 70, 70, 11.52371429],
                          "2017_08": [281, 68, 70, 15.01014706],
                          "2017_11": [210, 62, 70, 16.30443548],
                          "2018_02": [132, 83, 63, 8.541277108],
                          "2018_08": [91, 86, 63, 7.749418605],
                          "2019_12": [76, 56, 62, 9.09],
                          "2020_12": [96, 58, 62, 6.89137931],
                          "2021_09": [210, 166, 60, 8.999638554]}

auctions_supply_demand_all = {"2017_05": [256, 70, 70, 11.52371429],
                          "2017_08": [281, 68, 70, 15.01014706],
                          "2017_11": [210, 62, 70, 16.30443548],
                          "2018_02": [132, 83, 63, 8.541277108],
                          "2018_05": [111, 123, 63, 5.442702703],
                          "2018_08": [91, 86, 63, 7.749418605],
                          "2018_10": [62, 105, 63, 6.371929825],
                          "2019_02": [72, 98, 63, 7.108955224],
                          "2019_05": [41, 84, 62, 7.707428571],
                          "2019_08": [33, 100, 62, 6.50625],
                          "2019_09": [22, 59, 62, 8.543333333],
                          "2019_10": [25, 83, 62, 8.1628],
                          "2019_12": [76, 56, 62, 9.09],
                          "2020_02": [67, 114, 62, 7.925],
                          "2020_03": [25, 40, 62, 7.545],
                          "2020_06": [62, 109, 62, 7.606393443],
                          "2020_07": [26, 37, 62, 7.348076923],
                          "2020_09": [25, 28, 62, 12.95],
                          "2020_10": [89, 93, 62, 8.900675676],
                          "2020_12": [96, 58, 62, 6.89137931],
                          "2021_02": [91, 193, 60, 7.769101124],
                          "2021_05": [137, 142, 60, 8.743228346],
                          "2021_09": [210, 166, 60, 8.999638554]}


""" probability densities"""
uniform = {"limits": [0, 1], "values": [5, 9], "name": "uniform"}

A_2015_to_2018 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                  "values": [4.96961689, 6.092707157, 6.582392311, 6.893632889, 7.27610836, 7.583831787,
                             7.791398525, 7.964614773, 8.286667824, 8.537548065, 8.914340019],
                  "name": "A_2015_to_2018"
                  }

Q1_2015 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.492611995, 6.471895695, 6.693545055, 6.951332569, 7.297553921, 7.519855499,
                      7.882286644, 8.374427795, 8.558916092, 8.652050686, 9.535028725],
           "name": "Q1_2015"
          }

Q2_2015 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.677169685, 6.285719204, 6.578142738, 6.893282413, 7.345625973, 7.727066278, 8.238565063,
                      8.377321243, 8.521245956, 8.64702034, 8.900167465],
           "name": "Q2_2015"
          }

Q3_2015 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.931848145, 6.07861495, 6.724209309, 6.881145954, 7.03596735, 7.359204054,
                      7.837345123, 8.266534805, 8.474396706, 8.659362793, 8.900167465],
           "name": "Q3_2015"
          }

Q4_2015 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.895084858, 5.825116634, 6.471895695, 6.829391098, 7.15732336, 7.529127598, 7.824007988,
                      8.110083008, 8.394797325, 8.659362793, 9.117493629],
           "name": "Q4_2015"
          }

Q1_2016 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.833882446, 6.069154549, 6.668482971, 6.959655857, 7.295097828, 7.727127552, 7.83974123,
                      7.952074051, 8.253253937, 8.624503136, 8.900758743],
           "name": "Q1_2016"
          }

Q2_2016 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.670284271, 5.699841976, 6.132593632, 6.491136551, 6.989328384, 7.198141575, 7.669987202,
                      7.926581383, 8.164575577, 8.497216225, 8.778455257],
           "name": "Q2_2016"
          }

Q3_2016 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.377423763, 6.360836506, 6.627770901, 6.891846943, 7.15732336, 7.384797573, 7.703823566,
                      7.950483322, 8.183726311, 8.462020874, 8.683321953],
           "name": "Q3_2016"
          }

Q4_2016 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.845536113, 6.25670886, 6.716199875, 7.00511837, 7.297091961, 7.630745888, 7.951848507,
                      8.174170494, 8.314764977, 8.537548065, 9.136459351],
           "name": "Q4_2016"
          }

Q1_2017 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.180463791, 5.897703457, 6.147987843, 6.705548, 7.07152319, 7.516641617, 7.715362644,
                      7.944247723, 8.278270721, 8.497779942, 8.900758743],
           "name": "Q1_2017"
          }

Q2_2017 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.963686771, 6.05864315, 6.518023014, 7.073859215, 7.329433918, 7.57289362, 7.704456043,
                      7.945357323, 8.203967094, 8.462020874, 8.887006912],
           "name": "Q2_2017"
          }

Q3_2017 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.356339693, 6.447496176, 6.863281727, 7.329150438, 7.549167633, 7.721642733, 7.87047863,
                      8.021325588, 8.38300705, 8.622245789, 9.117493629],
           "name": "Q3_2017"
          }

Q4_2017 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [4.720245914, 6.092707157, 6.473149681, 6.791478157, 7.37794323, 7.593351841, 7.763834,
                      7.978372765, 8.224223137, 8.322464943, 8.737039375],
           "name": "Q4_2017"
          }

Q1_2018 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.046131134, 6.1224823, 6.627829552, 6.988927841, 7.436254501, 7.671094894, 7.77713871,
                      7.857042313, 8.024296761, 8.485262585, 8.673085213],
           "name": "Q1_2018"
          }

Q2_2018 = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
           "values": [5.307470798, 6.247206402, 6.50150528, 6.664869308, 6.96649456, 7.381894588, 7.683456898,
                      7.763860607, 7.954223728, 8.537548065, 8.793770771],
           "name": "Q2_2018"
          }

quartals = [Q1_2015, Q2_2015, Q3_2015, Q4_2015, Q1_2016, Q2_2016, Q3_2016, Q4_2016, Q1_2017, Q2_2017, Q3_2017, Q4_2017,
            Q1_2018, Q2_2018]






















